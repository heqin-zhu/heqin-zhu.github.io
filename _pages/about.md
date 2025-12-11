---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<!--
<style>
    body {
        font-family: Palatino, sans-serif;
        font-size: 18px;
    }
</style>
-->

<span class='anchor' id='about'></span>
<!-- 😊 -->
# About
- I am a Ph.D. student at the University of Science and Technology of China ([USTC](http://en.ustc.edu.cn/)), fortunately supervised by Prof. [Shaohua Kevin Zhou](https://sz.ustc.edu.cn/en/en_research_show/42.html) and Dr. [Peng Xiong](https://bme.ustc.edu.cn/2023/0322/c28131a596069/page.htm). Prior to this, I received my bachelor degree from USTC in 2020 and obtained my master degree from Institute of Computing Technology ([ICT](http://english.ict.cas.cn/)) and University of Chinese Academy of Sciences ([UCAS](https://english.ucas.ac.cn/)) in 2023.
- My research centers on AI biology, with focus on fundamental challenges in RNA modeling and design, including (but not limited in):
    - Structure and function prediction.
    - Multimodal biological foundation model
    - Drug discovery and RNA design for therapeutics.
    - Exploration of functional RNA motifs within non-coding genomic regions.
<!-- - Previously, I worked on medical imaging computing, where I developed universal models and few-shot learning methods for localizing anatomical landmarks. -->
- I am always welcoming discussions and collaborative opportunities, please feel free to contact me via [email](mailto:zhuheqin1@gmail.com). :)
- **<font color="#ff0000">I am actively seeking postdoctoral and research positions starting in Fall 2026.</font>** Here is my [CV](files/CV_Heqin_Zhu.pdf) ([中文简历](files/简历-朱河勤-中国科学技术大学.pdf)) for your reference. I would appreciate it if you would consider me for an opportunity.

<!-- 🔥 -->
# News
- 2025-08: &nbsp; We release structRFM ([bioRxiv](https://www.biorxiv.org/content/early/2025/08/07/2025.08.06.668731), [code](https://github.com/heqin-zhu/structRFM)), a structure-guided RNA foundation model for structural and functional inference.
- 2025-07: &nbsp; [BPfold](https://www.nature.com/articles/s41467-025-60048-1) has been published in **Nature Communications**.
- *2024-10*: &nbsp; We release BPfold ([bioRxiv](https://www.biorxiv.org/content/10.1101/2024.10.22.619430v1), [code](https://github.com/heqin-zhu/BPfold)), an effective tool for RNA secondary structure prediction.
- *2024-10*: &nbsp; Two papers have been accepted by **MICCAI 2024**.
- *2024-08*: &nbsp; [One paper](https://ieeexplore.ieee.org/abstract/document/10620395/) has been published in **IEEE Transactions on Medical Imaging**.
- *2024-08*: &nbsp; [One paper](https://www.sciencedirect.com/science/article/pii/S1361841524001257) has been published in **Medical Image Analysis**.
- *2023-10*: &nbsp; UOD ([arXiv](https://arxiv.org/abs/2306.07615), [code](https://github.com/heqin-zhu/UOD_universal_oneshot_detection)), a universal one-shot learning model,  has been accepted by **MICCAI 2023**.
- *2022-07*: &nbsp; [One paper](https://spj.science.org/doi/full/10.34133/2022/9765095) has been published in **BME frontiers**.
- *2022-03*: &nbsp; We release DFTR ([arXiv](https://arxiv.org/abs/2203.06429), [code](https://github.com/heqin-zhu/DFTR)), a depth-supervised hierarchical feature fusion transformer for salient object detection.
- *2021-10*: &nbsp; GU2Net ([arXiv](https://arxiv.org/abs/2103.04657), [code](https://github.com/MIRACLE-Center/YOLO_Universal_Anatomical_Landmark_Detection)), a universal model for anatomical landmark detection, has been accepted by **MICCAI 2021**.


<!-- 📝 -->
# Publications
(`#` equal contribution, `*` corresponding authors. Selected publications | [Google Scholar](https://scholar.google.com/citations?user=YkfSFekAAAAJ))

### RNA Foundation Model
- ![citations](https://img.shields.io/badge/Nature portfolio, Under Revision-2025-blue) [A fully open structure-guided RNA foundation model for robust structural and functional inference](https://www.biorxiv.org/content/early/2025/08/07/2025.08.06.668731).\
**Heqin Zhu**, Ruifeng Li, Feng Zhang, Fenghe Tang, Tong Ye, Xin Li, Yunjie Gu, Peng Xiong\*, S. Kevin Zhou\*&nbsp;&nbsp;[![](https://img.shields.io/github/stars/heqin-zhu/structRFM.svg?label=Stars&style=social)](https://github.com/heqin-zhu/structRFM)[[code](https://github.com/heqin-zhu/structRFM)][[bioRxiv](https://www.biorxiv.org/content/early/2025/08/07/2025.08.06.668731)]

### RNA Structure Prediction
- ![citations](https://img.shields.io/badge/Under Review-2025-blue) Toward Accurate RNA Non-Canonical Structure Prediction: The NC-Bench Benchmark and the NCfold Framework.\
**Heqin Zhu\#**, Ruifeng Li\#, Ao Chang, Mingqian Li, Hongyang Chen\*, Peng Xiong\*, S. Kevin Zhou\*&nbsp;&nbsp;[![](https://img.shields.io/github/stars/heqin-zhu/NCBench.svg?label=Stars&style=social)](https://github.com/heqin-zhu/NCBench)[[code](https://github.com/heqin-zhu/NCBench)][[bioRxiv](https://www.biorxiv.org/content/early/2025/11/17/2025.11.16.688746)]

- ![citations](https://img.shields.io/badge/Nature Communications-2025-blue) [Deep generalizable prediction of RNA secondary structure via base pair motif energy](https://www.nature.com/articles/s41467-025-60048-1).\
**Heqin Zhu**, Fenghe Tang, Quan Quan, Ke Chen, Peng Xiong\*, S. Kevin Zhou\*&nbsp;&nbsp;[![](https://img.shields.io/github/stars/heqin-zhu/BPfold.svg?label=Stars&style=social)](https://github.com/heqin-zhu/BPfold)[[code](https://github.com/heqin-zhu/BPfold)][[paper](https://www.nature.com/articles/s41467-025-60048-1)][[poster](files/poster_BPfold.pdf)][[poster2](files/poster_BPfold_2.jpg)]


### RNA Function Prediction
- ![citations](https://img.shields.io/badge/Under Revision-2025-blue) IRESeek: Structure-informed deep learning method for accurate identification of internal ribosome entry sites in circular RNAs.\
Feng Zhang\#, **Heqin Zhu\#**, Jie Hu, Jiayin Gao, Ke Chen, S. Kevin Zhou\*, and Peng Xiong\*&nbsp;&nbsp;[![](https://img.shields.io/github/stars/f-zhangf/IRESeek.svg?label=Stars&style=social)](https://github.com/f-zhangf/IRESeek)[[code](https://github.com/f-zhangf/IRESeek)]


### Universal Model & Domain Adaptation
- ![citations](https://img.shields.io/badge/MICCAI-2023-blue) [UOD: universal oneshot detection of anatomical landmark](https://link.springer.com/chapter/10.1007/978-3-031-43907-0_3) (**<font color="#ff0000">Early Accept</font>**)\
**Heqin Zhu**, Quan Quan, Qingsong Yao, Zaiyi Liu, S. Kevin Zhou &nbsp;&nbsp;[![](https://img.shields.io/github/stars/heqin-zhu/UOD_universal_oneshot_detection.svg?label=Stars&style=social)](https://github.com/heqin-zhu/UOD_universal_oneshot_detection)[[code](https://github.com/heqin-zhu/UOD_universal_oneshot_detection)][[arXiv](https://arxiv.org/abs/2306.07615)][[poster](files/poster_UOD.pdf)]
- ![citations](https://img.shields.io/badge/BMEF-2022-blue) [learning to localize cross-anatomy landmarks in x-ray images with a universal model](https://spj.science.org/doi/full/10.34133/2022/9765095).\
**Heqin Zhu**, Qingsong Yao, Li Xiao, S. Kevin Zhou &nbsp;&nbsp;[![](https://img.shields.io/github/stars/MIRACLE-Center/YOLO_Universal_Anatomical_Landmark_Detection.svg?label=Stars&style=social)](https://github.com/MIRACLE-Center/YOLO_Universal_Anatomical_Landmark_Detection)[[code](https://github.com/MIRACLE-Center/YOLO_Universal_Anatomical_Landmark_Detection)][[arXiv](https://arxiv.org/abs/2103.04657)]
- ![citations](https://img.shields.io/badge/MICCAI-2021-blue) [You Only Learn Once: Universal Anatomical Landmark Detection](https://link.springer.com/chapter/10.1007/978-3-030-87240-3_9).\
**Heqin Zhu**, Qingsong Yao, Li Xiao, S. Kevin Zhou &nbsp;&nbsp;[![](https://img.shields.io/github/stars/MIRACLE-Center/YOLO_Universal_Anatomical_Landmark_Detection.svg?label=Stars&style=social)](https://github.com/MIRACLE-Center/YOLO_Universal_Anatomical_Landmark_Detection)[[code](https://github.com/MIRACLE-Center/YOLO_Universal_Anatomical_Landmark_Detection)][[arXiv](https://arxiv.org/abs/2103.04657)]

### Unsupervised & Self-supervised & Few-shot learning
- ![citations](https://img.shields.io/badge/Medical Image Analysis-2024-blue) [Which images to label for few-shot medical image analysis?](https://www.sciencedirect.com/science/article/pii/S1361841524001257).\
Quan Quan\#, Qingsong Yao\#, **Heqin Zhu**, Qiyuan Wang, S. Kevin Zhou &nbsp;&nbsp;[[code](https://github.com/Curli-quan/SCP_SampleChoicePolicy)]
- ![citations](https://img.shields.io/badge/IEEE Transactions one Medical Imaging-2024-blue) [IGU-Aug: Information-guided unsupervised augmentation and pixel-wise contrastive learning for medical image analysis](https://ieeexplore.ieee.org/abstract/document/10620395/).\
Quan Quan\#, Qingsong Yao\#, **Heqin Zhu**, S. Kevin Zhou &nbsp;&nbsp;[![](https://img.shields.io/github/stars/Curli-quan/IGU-Aug.svg?label=Stars&style=social)](https://github.com/Curli-quan/IGU-Aug)[[code](https://github.com/Curli-quan/IGU-Aug)][[arXiv](https://arxiv.org/abs/2211.07118)]
- ![citations](https://img.shields.io/badge/MIDL-2024-blue) [Slide-SAM: medical SAM meets sliding window](https://arxiv.org/html/2311.10121v3).\
Quan Quan\#, Fenghe Tang\#, Zikang Xu, **Heqin Zhu**, S. Kevin Zhou &nbsp;&nbsp;[![](https://img.shields.io/github/stars/Curli-quan/Slide-SAM.svg?label=Stars&style=social)](https://github.com/Curli-quan/Slide-SAM)[[code](https://github.com/Curli-quan/Slide-SAM)][[arXiv](https://arxiv.org/abs/2311.10121v3)]
- ![citations](https://img.shields.io/badge/MICCAI-2024-blue) [Hyspark: Hybrid sparse masking for large scale medical image pre-training](https://link.springer.com/chapter/10.1007/978-3-031-72120-5_31).\
Fenghe Tang, Ronghao Xu, Qingsong Yao, Xueming Fu, Quan Quan, **Heqin Zhu**, Zaiyi Liu, S. Kevin Zhou &nbsp;&nbsp;[![](https://img.shields.io/github/stars/FengheTan9/HySpark.svg?label=Stars&style=social)](https://github.com/FengheTan9/HySpark)[[code](https://github.com/FengheTan9/HySparK)][[arXiv](https://arxiv.org/abs/2408.05815)]

### Others
- ![citations](https://img.shields.io/badge/IJCARS-2024-blue) [PELE scores: pelvic X-ray landmark detection with pelvis extraction and enhancement](https://link.springer.com/article/10.1007/s11548-024-03089-z).\
Zhen Huang\#, Han Li\#, Shitong Shao, **Heqin Zhu**, Huijie Hu, Zhiwei Cheng, Jianji Wang, S. Kevin Zhou &nbsp;&nbsp;[![](https://img.shields.io/github/stars/ECNUACRush/PELEscores.svg?label=Stars&style=social)](https://github.com/ECNUACRush/PELEscores)[[code](https://github.com/ECNUACRush/PELEscores)]
- ![citations](https://img.shields.io/badge/arXiv-2022-blue) [DFTR: Depth-supervised hierarchical feature fusion transformer for salient object detection](https://arxiv.org/abs/2203.06429).\
**Heqin Zhu**, Xu Sun, Yuexiang Li, Kai Ma, S. Kevin Zhou\*, Yefeng Zheng\*&nbsp;&nbsp;[[code](https://github.com/heqin-zhu/DFTR)][[arXiv](https://arxiv.org/abs/2203.06429)]
- ![citations](https://img.shields.io/badge/IJCARS-2021-blue) [Deep learning to segment pelvic bones: large-scale CT datasets and baseline models](https://link.springer.com/article/10.1007/s11548-021-02363-8).\
Pengbo Liu, Hu Han, Yuanqi Du, **Heqin Zhu**, Yinhao Li, Feng Gu, Honghu Xiao, Jun Li, Chunpeng Zhao, Li Xiao, Xinbao Wu, S. Kevin Zhou &nbsp;&nbsp;![](https://img.shields.io/github/stars/MIRACLE-Center/CTPelvic1K.svg?label=Stars&style=social)[[link](https://github.com/ICT-MIRACLE-lab/CTPelvic1K)][[arXiv](https://arxiv.org/abs/2012.08721)]

<!--
[![GitHub followers](https://img.shields.io/github/followers/heqin-zhu)](https://github.com/heqin-zhu)
[![GitHub followers](https://img.shields.io/github/starts/heqin-zhu)](https://github.com/heqin-zhu)
-->

<!-- 📖 -->
# Educations
- *2023-09 - present*, Ph.D. student of Biomedical Engineering, Suzhou Institute for Advanced Research, University of Science and Technology of China ([USTC](http://en.ustc.edu.cn/)), Suzhou, China
- *2020-09 - 2023-06*, Master of Computer Applications, University of Chinese Academy of Sciences (UCAS) & Institute of Computing Technology ([ICT](http://english.ict.cas.cn/)), CAS, Beijing, China
- *2016-09 - 2020-06*, Bachelor of Computer Science and Technology, University of Science and Technology of China ([USTC](http://en.ustc.edu.cn/)), Hefei, China
  - <span style="background: #d6eef8;">Hua Xia Talent Program in Computer Science and Technology</span>

<!-- 🎖 -->
# Honors and Awards
- *2025*,      <span style="background: #d6eef8;">National Scholarship</span>, Chinese Ministry of Education
- *2025*,      Suzhou Industrial Park Scholarship, USTC
- *2024*,      First Class Scholarship, USTC
- *2020-2023*, First Class Scholarship, UCAS & ICT
- *2023*,      Merit Student Award, UCAS & ICT
- *2018-2019*, Outstanding Student Award, USTC
- *2017*,      Institute of Chemistry Excellence Scholarship, USTC

<!-- 💻 -->
# Professional Experiences
- *2021-07 - 2021-11*, Research Intern, [Tencent JARVIS Lab](https://jarvislab.tencent.com/index-en.html), Shenzhen, China
- *2019-09 - 2020-04*, Research Intern, Z2sky, Suzhou, China

# Professional Services
- *Journal Reviewers*
  - IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)

- *Conference Reviewers:*
  - International Conference on Medical Image Computing and Computer-Assisted Intervention (MICCAI)

<!-- 💬 -->
# Invited Talks
- *2025-05*, Deep generalizable prediction of RNA secondary structure via base pair motif energy, The 3rd National Conference on Biomolecular Structure Prediction and Simulation.
- *2023-03*, Universal one-shot detection of anatomical landmarks, ICT.

# Teaching & Volunteer Experiences
- *2024*, Volunteer: Medical Augmented Reality Summer School, Suzhou
- *Fall 2023*, Teaching Assistant: Electronic information openness practices, USTC
- *2023*, Volunteer: Dushu Lake Forum Dushu Lake Symposium on Medical lmage Computing, Suzhou

<p align="center">
<script type='text/javascript' id='clustrmaps' src='//cdn.clustrmaps.com/map_v2.js?cl=ffffff&w=400&t=tt&d=023YIyttHQR8s08hPoPU7sutWj4yjTkXupp7BXqCOjM'></script>
<!--
<a href="https://clustrmaps.com/site/1bkj0" title="Visit tracker"><img src="//clustrmaps.com/map_v2.png?cl=ffffff&w=400&am=a&amp;t=tt&amp;d=023YIyttHQR8s08hPoPU7sutWj4yjTkXupp7BXqCOjM" /></a>
-->
</p>
