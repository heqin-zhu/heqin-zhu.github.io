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

<span class='anchor' id='about-me'></span>
# 😊 About Me 
- I am a Ph.D. student at the University of Science and Technology of China ([USTC](http://en.ustc.edu.cn/)), co-supervised by Prof. [S. Kevin Zhou](https://sz.ustc.edu.cn/en/en_research_show/42.html) and Dr. [Peng Xiong](https://bme.ustc.edu.cn/2023/0322/c28131a596069/page.htm).
- I received my bachelor degree from USTC in 2020 and obtained my master degree from Institute of Computing Technology ([ICT](http://english.ict.cas.cn/)) and University of Chinese Academy of Sciences ([UCAS](https://english.ucas.ac.cn/)) in 2023.
- My research interests include **computational biology** and medical image analysis, with specific focus on **RNA structure modeling**, anatomical landmark detection.


# 🔥 News
- *2023.5*: &nbsp; One paper accepted to MICCAI-23
- *2021.5*: &nbsp; One paper accepted to MICCAI-21

# 📝 Publications 
(Selected publications, `*` indicates equal contribution and ✉️ represents corresponding author.)

### RNA Secondary Structure Prediction
- `bioRxiv 2024` [Deep generalizable prediction of RNA secondary structure via base pair motif energy](https://doi.org/10.1101/2024.10.22.619430)\
**Heqin Zhu**, Fenghe Tang, Quan Quan, Ke Chen, Peng Xiong✉️, S. Kevin Zhou✉️ &nbsp;&nbsp;[[code](https://github.com/heqin-zhu/BPfold)]


### Few-shot Learning
- `MIA 2024` [Which images to label for few-shot medical image analysis?](https://www.sciencedirect.com/science/article/pii/S1361841524001257) (Medical Image Analysis)\
Quan Quan, Qingsong Yao, **Heqin Zhu**, Qiyuan Wang, S. Kevin Zhou &nbsp;&nbsp;[[code](https://github.com/Curli-quan/SCP_SampleChoicePolicy))
- `MICCAI 2023` [UOD: universal oneshot detection of anatomical landmark](https://link.springer.com/chapter/10.1007/978-3-031-43907-0_3) (International Conference on Medical Image Computing and Computer-Assisted Intervention)\
**Heqin Zhu**, Quan Quan, Qingsong Yao, Zaiyi Liu, S. Kevin Zhou &nbsp;&nbsp;[![](https://img.shields.io/github/stars/heqin-zhu/UOD_universal_oneshot_detection.svg?label=Stars&style=social)](https://github.com/heqin-zhu/UOD_universal_oneshot_detection)[[code](https://github.com/heqin-zhu//UOD_universal_oneshot_detection)][[arXiv](https://arxiv.org/abs/2306.07615)][[poster](files/MICCAI2023_UOD_poster.pdf)]

### Anatomical Landmark Detection
- `MICCAI 2024` [SIX-Net: Spatial-Context Information miX-up for Electrode Landmark Detection](https://link.springer.com/chapter/10.1007/978-3-031-72378-0_32) (International Conference on Medical Image Computing and Computer-Assisted Intervention)\
Xinyi Wang, Zikang Xu, **Heqin Zhu**, Qingsong Yao, Yiyong Sun, S. Kevin Zhou
- `IJCARS 2024` [PELE scores: pelvic X-ray landmark detection with pelvis extraction and enhancement](https://link.springer.com/article/10.1007/s11548-024-03089-z) (International Journal of Computer Assisted Radiology and Surgery)\
Zhen Huang, Han Li, Shitong Shao, **Heqin Zhu**, Huijie Hu, Zhiwei Cheng, Jianji Wang, S. Kevin Zhou &nbsp;&nbsp;[[code](https://github.com/ECNUACRush/PELEscores)]
- `BMEF 2022` [Learning to localize cross-anatomy landmarks in x-ray images with a universal model](https://spj.science.org/doi/full/10.34133/2022/9765095) (BME frontiers)\
**Heqin Zhu**, Qingsong Yao, Li Xiao, S. Kevin Zhou &nbsp;&nbsp;[![](https://img.shields.io/github/stars/MIRACLE-Center/YOLO_Universal_Anatomical_Landmark_Detection.svg?label=Stars&style=social)](https://github.com/MIRACLE-Center/YOLO_Universal_Anatomical_Landmark_Detection)[[code](https://github.com/MIRACLE-Center/YOLO_Universal_Anatomical_Landmark_Detection)][[arXiv](https://arxiv.org/abs/2103.04657)]
- `MICCAI 2021` [You Only Learn Once: Universal Anatomical Landmark Detection](https://link.springer.com/chapter/10.1007/978-3-030-87240-3_9) (International Conference on Medical Image Computing and Computer-Assisted Intervention)\
**Heqin Zhu**, Qingsong Yao, Li Xiao, S. Kevin Zhou &nbsp;&nbsp;[![](https://img.shields.io/github/stars/MIRACLE-Center/YOLO_Universal_Anatomical_Landmark_Detection.svg?label=Stars&style=social)](https://github.com/MIRACLE-Center/YOLO_Universal_Anatomical_Landmark_Detection)[[code](https://github.com/MIRACLE-Center/YOLO_Universal_Anatomical_Landmark_Detection)][[arXiv](https://arxiv.org/abs/2103.04657)]

### Unsupervised & Self-supervised Learning
- `TMI 2024` [IGU-Aug: Information-guided unsupervised augmentation and pixel-wise contrastive learning for medical image analysis](https://ieeexplore.ieee.org/abstract/document/10620395/) (IEEE Transactions on Medical Imaging)\
Quan Quan, Qingsong Yao, **Heqin Zhu**, S. Kevin Zhou &nbsp;&nbsp;[[code](https://github.com/Curli-quan/IGU-Aug)][[arXiv](https://arxiv.org/abs/2211.07118)]
- `MICCAI 2024` [Hyspark: Hybrid sparse masking for large scale medical image pre-training](https://link.springer.com/chapter/10.1007/978-3-031-72120-5_31) (International Conference on Medical Image Computing and Computer-Assisted Intervention)\
Fenghe Tang, Ronghao Xu, Qingsong Yao, Xueming Fu, Quan Quan, **Heqin Zhu**, Zaiyi Liu, S. Kevin Zhou &nbsp;&nbsp;[[code](https://github.com/FengheTan9/HySparK)][[arXiv](https://arxiv.org/abs/2408.05815)]

### Medical Image Segmentation
- `MIDL 2024` [Slide-SAM: medical SAM meets sliding window](https://arxiv.org/html/2311.10121v3) (Medical Imaging with Deep Learning)\
Quan Quan, Fenghe Tang, Zikang Xu, **Heqin Zhu**, S. Kevin Zhou &nbsp;&nbsp;[![](https://img.shields.io/github/stars/Curli-quan/Slide-SAM.svg?label=Stars&style=social)](https://github.com/Curli-quan/Slide-SAM)[[code](https://github.com/Curli-quan/Slide-SAM)][[arXiv](https://arxiv.org/abs/2311.10121v3)]
- `IPMI 2021` [A$^3$DSegNet: Anatomy-Aware Artifact Disentanglement and Segmentation Network for Unpaired Segmentation, Artifact Reduction, and Modality Translation](https://link.springer.com/chapter/10.1007/978-3-030-78191-0_28) (International Conference on Information Processing in Medical Imaging)\
Yuanyuan Lyu, Haofu Liao, **Heqin Zhu**, S. Kevin Zhou &nbsp;&nbsp;[[arXiv](https://arxiv.org/abs/2001.00339)]

### Others
- `arXiv 2022` [DFTR: Depth-supervised hierarchical feature fusion transformer for salient object detection](https://arxiv.org/abs/2203.06429)\
**Heqin Zhu**, Xu Sun, Yuexiang Li, Kai Ma, S. Kevin Zhou✉️, Yefeng Zheng✉️  &nbsp;&nbsp;[[code](https://github.com/heqin-zhu/DFTR)][[arXiv](https://arxiv.org/abs/2203.06429)]
- `IJCARS 2021` [Deep learning to segment pelvic bones: large-scale CT datasets and baseline models](https://link.springer.com/article/10.1007/s11548-021-02363-8) (International Journal of Computer Assisted Radiology and Surgery)\
Pengbo Liu, Hu Han, Yuanqi Du, **Heqin Zhu**, Yinhao Li, Feng Gu, Honghu Xiao, Jun Li, Chunpeng Zhao, Li Xiao, Xinbao Wu, S. Kevin Zhou &nbsp;&nbsp;![](https://img.shields.io/github/stars/MIRACLE-Center/CTPelvic1K.svg?label=Stars&style=social)[[link](https://github.com/ICT-MIRACLE-lab/CTPelvic1K)][[arXiv](https://arxiv.org/abs/2012.08721)]



# 🎖 Honors and Awards
- *2023-2024* Academic First Class Scholarship in USTC
- *2022-2023* Merit Student in ICT, CAS 

# 📖 Educations
- *2023.09 - (now)*, Ph.D. student, Suzhou Institute for Advanced Research, University of Science and Technology of China, Suzhou, China
- *2020.09 - 2023.06*, Master, Institute of Computing Technology (ICT), Chinese Academic of Science (CAS), Beijing, China
- *2016.09 - 2020.06*, Graduate, University of Science and Technology of China (USTC), Hefei, China

# 💬 Professional Services
*Jornel Reviewers:* 
- IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)

*Conference Reviewers:* 
- International Conference on Medical Image Computing and Computer-Assisted Intervention (MICCAI)-2022

<!--
# 💬 Invited Talks
- *2021.06*, TODO 
-->

# 💻 Internships
- *2021.7 - 2021.11*, [Tencent Jarvis Lab](https://jarvislab.tencent.com/index-en.html), Shenzhen, China
- *2019.9 - 2020.4*, Z2sky.ai, Suzhou, China

<p align="center">
<script type='text/javascript' id='clustrmaps' src='//cdn.clustrmaps.com/map_v2.js?cl=ffffff&w=300&t=tt&d=023YIyttHQR8s08hPoPU7sutWj4yjTkXupp7BXqCOjM'></script>
<!--
<a href="https://clustrmaps.com/site/1bkj0" title="Visit tracker"><img src="//clustrmaps.com/map_v2.png?cl=ffffff&w=300&am=a&amp;t=tt&amp;d=023YIyttHQR8s08hPoPU7sutWj4yjTkXupp7BXqCOjM" /></a>
-->
</p>
