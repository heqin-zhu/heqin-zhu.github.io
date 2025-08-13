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

<span class='anchor' id='about'></span>
<!-- 😊 -->
# About
- I am a Ph.D. student at the University of Science and Technology of China ([USTC](http://en.ustc.edu.cn/)), co-supervised by Prof. [S. Kevin Zhou](https://sz.ustc.edu.cn/en/en_research_show/42.html)(Fellow of IEEE, AIMBE, NAI) and Dr. [Peng Xiong](https://bme.ustc.edu.cn/2023/0322/c28131a596069/page.htm). Prior to this, I received my bachelor degree from USTC in 2020 and obtained my master degree from Institute of Computing Technology ([ICT](http://english.ict.cas.cn/)) and University of Chinese Academy of Sciences ([UCAS](https://english.ucas.ac.cn/)) in 2023.
- My research centers on AI for Science (AI4S), with a specific focus on fundamental challenges in **computational
biology**, from structure prediction to **sequence-structure-function** applications, including:
    - RNA secondary structure and tertiary structure prediction.
    - Structure-guided RNA foundation model (LLM) for sequence understanding and structural prediction.
    - Functional applications such as identification of IRES, exploration of functional RNA motifs within non-coding genomic regions, and AI-driven drug discovery.
- Previously, I worked on medical imaging computing, where I developed universal models and few-shot learning methods for localizing anatomical landmarks.
- I am always welcoming discussions and collaborative opportunities, please feel free to contact me. :)
- **<font color="#ff0000">I am actively seeking postdoctoral and research positions starting in Fall 2026.</font>** Here is my [CV](files/CV_Heqin_Zhu.pdf) ([中文简历](files/算法研究-朱河勤-中国科学技术大学.pdf)). I would appreciate it if you would consider me for an opportunity.

<!-- 🔥 -->
# News
- 2025.08: &nbsp; We release structRFM ([paper](https://www.biorxiv.org/content/early/2025/08/07/2025.08.06.668731), [code](https://github.com/heqin-zhu/structRFM)), a structure-guiede RNA foundation model for structural and functional inference.
- 2025.07: &nbsp; [BPfold](https://www.nature.com/articles/s41467-025-60048-1) has been published in Nature Communications.
- *2024.10*: &nbsp; We release BPfold ([paper](https://www.biorxiv.org/content/10.1101/2024.10.22.619430v1), [code](https://github.com/heqin-zhu/BPfold)), an effective tool for RNA secondary structure prediction.
- *2024.10*: &nbsp; Two papers has been accepted by MICCAI 2024.
- *2024.08*: &nbsp; [One paper](https://ieeexplore.ieee.org/abstract/document/10620395/) has been published in IEEE Transactions on Medical Imaging.
- *2024.08*: &nbsp; [One paper](https://www.sciencedirect.com/science/article/pii/S1361841524001257) has been published in Medical Image Analysis.
- *2023.10*: &nbsp; UOD ([paper](https://arxiv.org/abs/2306.07615), [code](https://github.com/heqin-zhu/UOD_universal_oneshot_detection)), a universal one-shot learning model,  has been accepted by MICCAI 2023.
- *2022.07*: &nbsp; [One paper](https://spj.science.org/doi/full/10.34133/2022/9765095) has been published in BME frontiers.
- *2022.03*: &nbsp; We release DFTR([paper](https://arxiv.org/abs/2203.06429), [code](https://github.com/heqin-zhu/DFTR)), a Depth-supervised hierarchical feature fusion transformer for salient object detection.
- *2021.10*: &nbsp; GU2Net ([paper](https://arxiv.org/abs/2103.04657), [code](https://github.com/MIRACLE-Center/YOLO_Universal_Anatomical_Landmark_Detection)), a universal model for anatomical landmark detection,  has been accepted by MICCAI 2021.


<!-- 📝 -->
# Publications
(`#` equal contribution, `*` corresponding authors. Selected publications | [Google Scholar](https://scholar.google.com/citations?user=YkfSFekAAAAJ))

### RNA Foundation Model
- `bioRxiv 2025` [A fully open structure-guided RNA foundation model for robust structural and functional inference](https://www.biorxiv.org/content/early/2025/08/07/2025.08.06.668731) (Submitted)\
**Heqin Zhu**, Ruifeng Li, Feng Zhang, Fenghe Tang, Tong Ye, Xin Li, Yunjie Gu, Peng Xiong\*, S. Kevin Zhou\*&nbsp;&nbsp;[![](https://img.shields.io/github/stars/heqin-zhu/structRFM.svg?label=Stars&style=social)](https://github.com/heqin-zhu/structRFM)[[code](https://github.com/heqin-zhu/structRFM)][[bioRxiv](https://www.biorxiv.org/content/early/2025/08/07/2025.08.06.668731)]

### RNA Structure Prediction
- `Nat. Commun. 2025` [Deep generalizable prediction of RNA secondary structure via base pair motif energy](https://www.nature.com/articles/s41467-025-60048-1) (Nature Communications)\
**Heqin Zhu**, Fenghe Tang, Quan Quan, Ke Chen, Peng Xiong\*, S. Kevin Zhou\*&nbsp;&nbsp;[![](https://img.shields.io/github/stars/heqin-zhu/BPfold.svg?label=Stars&style=social)](https://github.com/heqin-zhu/BPfold)[[code](https://github.com/heqin-zhu/BPfold)][[paper](https://www.nature.com/articles/s41467-025-60048-1)][[poster](files/poster_BPfold.pdf)]


### Few-shot Learning
- `MIA 2024` [Which images to label for few-shot medical image analysis?](https://www.sciencedirect.com/science/article/pii/S1361841524001257) (Medical Image Analysis)\
Quan Quan\#, Qingsong Yao\#, **Heqin Zhu**, Qiyuan Wang, S. Kevin Zhou &nbsp;&nbsp;[[code](https://github.com/Curli-quan/SCP_SampleChoicePolicy)]
- `MICCAI 2023` [UOD: universal oneshot detection of anatomical landmark](https://link.springer.com/chapter/10.1007/978-3-031-43907-0_3) (International Conference on Medical Image Computing and Computer-Assisted Intervention)(early accept)\
**Heqin Zhu**, Quan Quan, Qingsong Yao, Zaiyi Liu, S. Kevin Zhou &nbsp;&nbsp;[![](https://img.shields.io/github/stars/heqin-zhu/UOD_universal_oneshot_detection.svg?label=Stars&style=social)](https://github.com/heqin-zhu/UOD_universal_oneshot_detection)[[code](https://github.com/heqin-zhu/UOD_universal_oneshot_detection)][[arXiv](https://arxiv.org/abs/2306.07615)][[poster](files/poster_UOD.pdf)]

### Anatomical Landmark Detection
- `IJCARS 2024` [PELE scores: pelvic X-ray landmark detection with pelvis extraction and enhancement](https://link.springer.com/article/10.1007/s11548-024-03089-z) (International Journal of Computer Assisted Radiology and Surgery)\
Zhen Huang\#, Han Li\#, Shitong Shao, **Heqin Zhu**, Huijie Hu, Zhiwei Cheng, Jianji Wang, S. Kevin Zhou &nbsp;&nbsp;[![](https://img.shields.io/github/stars/ECNUACRush/PELEscores.svg?label=Stars&style=social)](https://github.com/ECNUACRush/PELEscores)[[code](https://github.com/ECNUACRush/PELEscores)]
- `BMEF 2022` [Learning to localize cross-anatomy landmarks in x-ray images with a universal model](https://spj.science.org/doi/full/10.34133/2022/9765095) (BME frontiers)\
**Heqin Zhu**, Qingsong Yao, Li Xiao, S. Kevin Zhou &nbsp;&nbsp;[![](https://img.shields.io/github/stars/MIRACLE-Center/YOLO_Universal_Anatomical_Landmark_Detection.svg?label=Stars&style=social)](https://github.com/MIRACLE-Center/YOLO_Universal_Anatomical_Landmark_Detection)[[code](https://github.com/MIRACLE-Center/YOLO_Universal_Anatomical_Landmark_Detection)][[arXiv](https://arxiv.org/abs/2103.04657)]
- `MICCAI 2021` [You Only Learn Once: Universal Anatomical Landmark Detection](https://link.springer.com/chapter/10.1007/978-3-030-87240-3_9) (International Conference on Medical Image Computing and Computer-Assisted Intervention)\
**Heqin Zhu**, Qingsong Yao, Li Xiao, S. Kevin Zhou &nbsp;&nbsp;[![](https://img.shields.io/github/stars/MIRACLE-Center/YOLO_Universal_Anatomical_Landmark_Detection.svg?label=Stars&style=social)](https://github.com/MIRACLE-Center/YOLO_Universal_Anatomical_Landmark_Detection)[[code](https://github.com/MIRACLE-Center/YOLO_Universal_Anatomical_Landmark_Detection)][[arXiv](https://arxiv.org/abs/2103.04657)]

### Unsupervised & Self-supervised Learning
- `TMI 2024` [IGU-Aug: Information-guided unsupervised augmentation and pixel-wise contrastive learning for medical image analysis](https://ieeexplore.ieee.org/abstract/document/10620395/) (IEEE Transactions on Medical Imaging)\
Quan Quan\#, Qingsong Yao\#, **Heqin Zhu**, S. Kevin Zhou &nbsp;&nbsp;[![](https://img.shields.io/github/stars/Curli-quan/IGU-Aug.svg?label=Stars&style=social)](https://github.com/Curli-quan/IGU-Aug)[[code](https://github.com/Curli-quan/IGU-Aug)][[arXiv](https://arxiv.org/abs/2211.07118)]
- `MIDL 2024` [Slide-SAM: medical SAM meets sliding window](https://arxiv.org/html/2311.10121v3) (Medical Imaging with Deep Learning)\
Quan Quan\#, Fenghe Tang\#, Zikang Xu, **Heqin Zhu**, S. Kevin Zhou &nbsp;&nbsp;[![](https://img.shields.io/github/stars/Curli-quan/Slide-SAM.svg?label=Stars&style=social)](https://github.com/Curli-quan/Slide-SAM)[[code](https://github.com/Curli-quan/Slide-SAM)][[arXiv](https://arxiv.org/abs/2311.10121v3)]
- `MICCAI 2024` [Hyspark: Hybrid sparse masking for large scale medical image pre-training](https://link.springer.com/chapter/10.1007/978-3-031-72120-5_31) (International Conference on Medical Image Computing and Computer-Assisted Intervention)\
Fenghe Tang, Ronghao Xu, Qingsong Yao, Xueming Fu, Quan Quan, **Heqin Zhu**, Zaiyi Liu, S. Kevin Zhou &nbsp;&nbsp;[![](https://img.shields.io/github/stars/FengheTan9/HySpark.svg?label=Stars&style=social)](https://github.com/FengheTan9/HySpark)[[code](https://github.com/FengheTan9/HySparK)][[arXiv](https://arxiv.org/abs/2408.05815)]

### Others
- `arXiv 2022` [DFTR: Depth-supervised hierarchical feature fusion transformer for salient object detection](https://arxiv.org/abs/2203.06429)\
**Heqin Zhu**, Xu Sun, Yuexiang Li, Kai Ma, S. Kevin Zhou\*, Yefeng Zheng\*&nbsp;&nbsp;[[code](https://github.com/heqin-zhu/DFTR)][[arXiv](https://arxiv.org/abs/2203.06429)]
- `IJCARS 2021` [Deep learning to segment pelvic bones: large-scale CT datasets and baseline models](https://link.springer.com/article/10.1007/s11548-021-02363-8) (International Journal of Computer Assisted Radiology and Surgery)\
Pengbo Liu, Hu Han, Yuanqi Du, **Heqin Zhu**, Yinhao Li, Feng Gu, Honghu Xiao, Jun Li, Chunpeng Zhao, Li Xiao, Xinbao Wu, S. Kevin Zhou &nbsp;&nbsp;![](https://img.shields.io/github/stars/MIRACLE-Center/CTPelvic1K.svg?label=Stars&style=social)[[link](https://github.com/ICT-MIRACLE-lab/CTPelvic1K)][[arXiv](https://arxiv.org/abs/2012.08721)]

<!-- 📖 -->
# Educations
- *2023.09 - present*, Ph.D. student of Biomedical Engineering, Suzhou Institute for Advanced Research, University of Science and Technology of China ([USTC](http://en.ustc.edu.cn/)), Suzhou, China
- *2020.09 - 2023.06*, Master of Computer Applications, University of Chinese Academy of Sciences (UCAS) & Institute of Computing Technology ([ICT](http://english.ict.cas.cn/)), CAS, Beijing, China
- *2016.09 - 2020.06*, Bachelor of Computer Science and Technology, University of Science and Technology of China ([USTC](http://en.ustc.edu.cn/)), Hefei, China
  - **Hua Xia Talent Program in Computer Science and Technology**

<!-- 🎖 -->
# Honors and Awards
- *2025*,      Suzhou Industrial Park Scholarship, USTC
- *2024*,      First Class Scholarship, USTC
- *2020-2023*, First Class Scholarship, UCAS & ICT
- *2023*,      Merit Student Award, UCAS & ICT
- *2018-2019*, Outstanding Student Award, USTC
- *2017*,      Institute of Chemistry Excellence Scholarship, USTC

<!-- 💻 -->
# Professional Experiences
- *2021.07 - 2021.11*, Research Intern, [Tencent Jarvis Lab](https://jarvislab.tencent.com/index-en.html), Shenzhen, China
- *2019.09 - 2020.04*, Research Intern, Z2sky, Suzhou, China

<!-- 💬 -->
# Professional Services
- *Journal Reviewers*
  - IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)

- *Conference Reviewers:*
  - International Conference on Medical Image Computing and Computer-Assisted Intervention (MICCAI)

<!--
# 💬 Invited Talks
- *2021.06*, TODO 
-->

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
