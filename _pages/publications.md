---
permalink: /publications/
title: "Publications"
author_profile: true
---

<style>
.pub-year {
  font-size: 1.4em;
  font-weight: bold;
  margin-top: 2em;
  margin-bottom: 0.8em;
  padding-bottom: 0.3em;
  border-bottom: 2px solid #e8e8e8;
  color: #555;
}

.pub-card {
  background: #fafafa;
  border: 1px solid #eaeaea;
  border-radius: 8px;
  padding: 1.2em 1.5em;
  margin-bottom: 1em;
  transition: box-shadow 0.2s ease;
}

.pub-card:hover {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.pub-card-preprint {
  background: #f5f5f5;
  border: 1px dashed #d0d0d0;
}

.pub-venue {
  margin-bottom: 0.5em;
}

.pub-title {
  font-size: 1.05em;
  font-weight: 600;
  margin-bottom: 0.4em;
  line-height: 1.4;
}

.pub-title a {
  color: #333;
  text-decoration: none;
}

.pub-title a:hover {
  color: #0472ab;
}

.pub-authors {
  font-size: 0.92em;
  color: #555;
  margin-bottom: 0.5em;
  line-height: 1.5;
}

.pub-links {
  font-size: 0.88em;
}

.pub-links a {
  display: inline-block;
  margin-right: 0.6em;
  text-decoration: none;
}

.pub-links a:hover {
  text-decoration: underline;
}

.pub-legend {
  font-size: 0.9em;
  color: #777;
  margin-bottom: 1.5em;
  font-style: italic;
}
</style>

# Publications
(`#`: equal contribution, `*`: corresponding author. Full list | [Google Scholar](https://scholar.google.com/citations?user=YkfSFekAAAAJ))

<div class="pub-legend">
  <span class="pub-legend-badge-pub"></span> Published &nbsp;&nbsp;
  <span class="pub-legend-badge-pre"></span> Preprint
</div>

<style>
.pub-legend-badge-pub {
  display: inline-block;
  width: 12px;
  height: 12px;
  background: #0072b2;
  border-radius: 3px;
  vertical-align: middle;
}
.pub-legend-badge-pre {
  display: inline-block;
  width: 12px;
  height: 12px;
  background: #999;
  border-radius: 3px;
  vertical-align: middle;
}
</style>

{% assign current_year = nil %}
{% for pub in site.data.publications %}
  {% unless pub.year == current_year %}
    {% assign current_year = pub.year %}
    <div class="pub-year">{{ current_year }}</div>
  {% endunless %}

  {% if pub.venue_type == 'preprint' %}
    <div class="pub-card pub-card-preprint">
  {% else %}
    <div class="pub-card">
  {% endif %}

    <div class="pub-venue">
      {% if pub.venue_type == 'preprint' %}
        <img src="https://img.shields.io/badge/{{ pub.venue | replace: ' ', '%20' }}-{{ pub.year }}-999999" alt="{{ pub.venue }}">
      {% else %}
        <img src="https://img.shields.io/badge/{{ pub.venue | replace: ' ', '%20' }}-{{ pub.year }}-0072b2" alt="{{ pub.venue }}">
      {% endif %}
    </div>

    <div class="pub-title">
      {% if pub.url and pub.url != '' %}
        <a href="{{ pub.url }}">{{ pub.title }}</a>
      {% else %}
        {{ pub.title }}
      {% endif %}
    </div>

    <div class="pub-authors">
      {% for author in pub.authors %}
        {% if author.highlight %}
          <strong>{{ author.name }}</strong>{% if author.first_author %}#{% endif %}{% if author.corresponding %}*{% endif %}{% unless forloop.last %}, {% endunless %}
        {% else %}
          {{ author.name }}{% if author.first_author %}#{% endif %}{% if author.corresponding %}*{% endif %}{% unless forloop.last %}, {% endunless %}
        {% endif %}
      {% endfor %}
    </div>

    {% if pub.links and pub.links.size > 0 %}
      <div class="pub-links">
        {% if pub.url and pub.url != '' %}
          <a href="{{ pub.url }}">[paper]</a>
        {% endif %}
        {% if pub.links.code %}
          <a href="{{ pub.links.code }}">[code]</a>
        {% endif %}
        {% if pub.links.page %}
          <a href="{{ pub.links.page }}">[page]</a>
        {% endif %}
        {% if pub.links.poster %}
          <a href="{{ pub.links.poster }}">[poster]</a>
        {% endif %}
        {% if pub.links.poster2 %}
          <a href="{{ pub.links.poster2 }}">[poster2]</a>
        {% endif %}
        {% if pub.links.pypi %}
          <a href="{{ pub.links.pypi }}">[PyPI]</a>
        {% endif %}
        {% if pub.links.arxiv %}
          <a href="{{ pub.links.arxiv }}">[arXiv]</a>
        {% endif %}
      </div>
    {% endif %}

  </div>
{% endfor %}
