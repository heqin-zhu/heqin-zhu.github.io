#!/usr/bin/env python3
"""Convert publications.bib to _data/publications.yml.

Reads files/publications.bib, merges with _data/publications_extra.yml,
and outputs _data/publications.yml for Jekyll Liquid template consumption.

Usage:
    python3 scripts/bib_to_yaml.py
"""

import re
import sys
from pathlib import Path

try:
    import bibtexparser
except ImportError:
    print("Error: bibtexparser not installed. Run: pip install bibtexparser", file=sys.stderr)
    sys.exit(1)

try:
    import yaml
except ImportError:
    print("Error: pyyaml not installed. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


PROJECT_ROOT = Path(__file__).resolve().parent.parent
BIB_PATH = PROJECT_ROOT / "files" / "publications.bib"
EXTRA_PATH = PROJECT_ROOT / "_data" / "publications_extra.yml"
OUTPUT_PATH = PROJECT_ROOT / "_data" / "publications.yml"

# Patterns to detect preprints
PREPRINT_KEYWORDS = ["arxiv", "biorxiv", "medrxiv"]

# Patterns to map venue names to short forms
VENUE_SHORT_MAP = {
    "nature communications": "Nature Communications",
    "nar genomics and bioinformatics": "NAR Genomics and Bioinformatics",
    "medical image analysis": "Medical Image Analysis",
    "ieee transactions on medical imaging": "IEEE TMI",
    "international conference on medical image computing": "MICCAI",
    "international journal of computer assisted": "IJCARS",
    "bme frontiers": "BMEF",
    "international conference on information processing": "IPMI",
    "international conference on learning representations": "ICLR",
}

# Patterns to detect conference
CONF_KEYWORDS = [
    "conference on",
    "proceedings",
    "iclr",
    "miccai",
    "ipmi",
    "midl",
    "neurips",
    "cvpr",
    "iccv",
    "eccv",
    "aaai",
    "ijcai",
]


def detect_venue_type(venue: str) -> str:
    """Detect whether the venue is a preprint, journal, or conference."""
    venue_lower = venue.lower()
    if any(kw in venue_lower for kw in PREPRINT_KEYWORDS):
        return "preprint"
    if any(kw in venue_lower for kw in CONF_KEYWORDS):
        return "conference"
    return "journal"


def normalize_author_name(name: str) -> str:
    """Convert 'Last, First' to 'First Last' format."""
    name = name.replace("{", "").replace("}", "").strip()
    if "," in name:
        parts = [p.strip() for p in name.split(",", 1)]
        if len(parts) == 2:
            return f"{parts[1]} {parts[0]}"
    return name


def parse_authors_bib(entry: dict) -> list:
    """Parse authors from a bibtex entry dict (bibtexparser 1.4.x format)."""
    author_field = entry.get("author", "")
    if not author_field:
        return []

    raw_authors = [a.strip() for a in author_field.replace(" and ", "\n").split("\n") if a.strip()]

    authors = []
    for raw in raw_authors:
        # Clean up LaTeX braces and normalize to "First Last" format
        clean = normalize_author_name(raw)
        if clean and clean.lower() != "others":
            authors.append({
                "name": clean,
                "highlight": False,
                "first_author": False,
                "corresponding": False,
            })
    ## no nedd to explicitly mark first author, corresonding author
    # authors[0]['first_author'] = True
    # authors[-1]['corresponding'] = True
    return authors


def merge_annotations(authors: list, extra_authors: list) -> list:
    """Merge bib authors with extra annotations, matching by name."""
    if not extra_authors:
        return authors

    extra_lookup = {}
    for ea in extra_authors:
        # key = ea.get("name", "").lower().replace(".", "").replace("-", " ").replace(",", "")
        key = ea.get("name", "")
        extra_lookup[key] = ea

    merged = []
    for a in authors:
        # key = a["name"].lower().replace(".", "").replace("-", " ").replace(",", "")
        key = a["name"]
        if key in extra_lookup:
            ea = extra_lookup[key]
            a["highlight"] = ea.get("highlight", a["highlight"])
            a["first_author"] = ea.get("first_author", a["first_author"])
            a["corresponding"] = ea.get("corresponding", a["corresponding"])
        merged.append(a)
    return merged


def clean_latex(text: str) -> str:
    """Remove LaTeX formatting from text."""
    return text.replace("{", "").replace("}", "").replace("\\", "")


def convert_entry(entry: dict, extra: dict) -> dict:
    """Convert a single bib entry dict to a YAML-friendly dict."""
    bib_id = entry["ID"]
    extra_data = extra.get(bib_id, {})

    # Title
    title = clean_latex(entry.get("title", ""))

    # Authors
    authors = parse_authors_bib(entry)
    extra_authors = extra_data.get("authors_annotation", [])
    if extra_authors:
        authors = merge_annotations(authors, extra_authors)
    else:
        # Auto-highlight Heqin Zhu if not in extra
        for a in authors:
            if a["name"].lower() == "heqin zhu":
                a["highlight"] = True

    # Year
    year = int(entry.get("year", 0))

    # Venue
    venue = ""
    if entry.get("journal"):
        venue = clean_latex(entry["journal"])
    elif entry.get("booktitle"):
        venue = clean_latex(entry["booktitle"])

    # Venue type (allow extra to override auto-detection)
    venue_type = extra_data.get("venue_type", detect_venue_type(venue))

    # Venue short name (from extra or auto-detect)
    venue_short = extra_data.get("venue_short", "")
    if not venue_short:
        venue_lower = venue.lower()
        for pattern, short in VENUE_SHORT_MAP.items():
            if pattern in venue_lower:
                venue_short = short
                break
        if not venue_short:
            venue_short = venue

    # URL
    url = entry.get("url", "")
    doi = entry.get("doi", "")
    if not url and doi:
        url = f"https://doi.org/{doi}"
    if not url:
        url = extra_data.get("url", "")

    # Links
    links = extra_data.get("links", {})
    if not links:
        links = {}

    return {
        "id": bib_id,
        "title": title,
        "authors": authors,
        "year": year,
        "venue": venue_short,
        "venue_type": venue_type,
        "url": url,
        "links": links,
    }


def main():
    # Load bib (bibtexparser 1.4.x API)
    if not BIB_PATH.exists():
        print(f"Error: {BIB_PATH} not found", file=sys.stderr)
        sys.exit(1)

    with open(BIB_PATH, "r") as f:
        bib_db = bibtexparser.load(f)

    entries = bib_db.entries
    print(f"Parsed {len(entries)} entries from {BIB_PATH}")

    # Load extra annotations
    extra = {}
    if EXTRA_PATH.exists():
        with open(EXTRA_PATH, "r") as f:
            extra = yaml.safe_load(f) or {}
        print(f"Loaded annotations for {len(extra)} papers from {EXTRA_PATH}")
    else:
        print(f"Warning: {EXTRA_PATH} not found, using bib data only")

    # Convert
    publications = []
    for entry in entries:
        pub = convert_entry(entry, extra)
        publications.append(pub)

    # Sort by year descending
    publications.sort(key=lambda x: x["year"], reverse=True)

    # Write output
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        yaml.dump(publications, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"Wrote {len(publications)} publications to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
