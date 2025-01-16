 <center>
     <h1>王天乐</h1>
 </center>

## 个人信息

* 性 别：男&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; 年 龄：28
* 手 机：18092430560 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;邮 箱：lixiamomo@outlook.com
* 专 业：机器人技术工程 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;岗 位：通软/底软开发工程师

## 工作及教育经历

* 华为&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;&ensp;2022.8~至今&emsp;&emsp;&emsp;&emsp;&emsp; 海思-智慧媒体开发部
* 西安电子科技大学&emsp;&emsp;&emsp;2019.9~2022.7&emsp;&emsp;&emsp;&emsp; 机器人技术工程-研究生
* 西安工业大学&emsp;&emsp;&emsp;&emsp;&emsp;2014.9~2018.7&emsp;&emsp;&emsp;&emsp; 机械电子工程-本科

## 个人介绍

* 性格开朗，具有强烈的技术追求；具备出色的学习能力和求知欲。虽然非人工智能专业出身，但在工作之余积极钻研软件架构技术、学习AI算法及AI Infra。

* **软件开发**：精通C/C++语言的架构设计开发。在职期间获得**华山论剑个人金奖、上海海思优秀作品奖、芯火奖**等多个荣誉。负责AIPQ-Service模块的架构设计与开发，以及AI软件栈的重构方案设计与开发；熟悉驱动开发，具备多颗海思画质芯片的驱动维护与开发经验。

* **AI Infra**：掌握AI Infra相关技术栈，**独立开发Needle神经网络推理库**。了解CUDA和OpenCL算子开发，熟悉反向传播算法及常用高性能算子优化（如Conv、Matmul）。

* **AI算法**：熟悉常用神经网络算法的原理，能够独立复现常见、经典AI算法，曾复现过**Vision Transformer、FCOS**等经典算法。能够熟练运用**迁移学习、模型蒸馏**等模型训练与优化技术。

## 项目经历
### 软件方向

1. 华为/海思 - AIPQ-Service - 方案设计、开发 - 2024.2-2024.6
    * 项目概要：通过GPU运行AI模型，针对不同播放场景，动态计算图像优化参数，进一步优化图像质量
    * 架构设计难点：如何设计架构达到多芯片共代码无耦合；如何设计架构以达到架构的可测试性；如何有效管理资源，防止驱动、GPU、线程、内存等资源泄露；如何设计架构，使多芯片、多算法解耦的同时，避免重复造轮子，达到高内聚低耦合
    * 技术难点：实现OpenCL代码，通过GPU对原始图像进行预处理同时满足性能要求；板端测试、调优、部署神经网络模型，满足性能、精度及软件架构需求；
    * 结果：2个月设计、开发用户态、内核态多个模块代码1.8w行，当前DI版本问题单数量0；
    * 效果：该芯片最大竞争力卖点，待DW版本外发客户；

2. 华为/海思 - AI软件栈南向接口层 - 开发 - 2023.10-2023.12
    * 项目概要：实现AI软件栈南向接口层，使AI软件栈支持多个神经网络加速库；
    * 架构设计难点：如何抽象接口
    * 技术难点：如何将现有架构层与实际实现解耦，同时不影响上游业务
    * 结果：上库source代码6k，测试用例代码2w+，上库当月问题单数量仅2例

3. 华为/海思 - TvOS 5.0 AI-HAL北向 适配层 - 开发 - 2023.6-2023.10
    * 项目概要：完成AI-HAL北向适配层开发，使TVOS支持多神经网络加速库
    * 架构设计难点：如何设计接口，使其兼容现有AI生态（晟腾、TFlite等）
    * 技术难点：通过C语言面向对象的方式设计架构，兼容多生态源码；确保多线程、多模型、异步等复杂场景，计算无误
    * 结果：AI-HAL成为TvOS 的AI生态标准，同年支撑X高端芯片AI特性交付。
    * 获奖情况：AI-HAL是项目组中首个以C语言面向对象方式组织、测试驱动开发为流程的模块，架构clean，代码优秀，获得**上海海思 研发好作品**奖、**TVOS 致谢信**；

### AI Infra

### AI 算法
1. Vision Transformer 项目 
   * 项目概要：实现一个基于Vision Transformer的图像分类模型，提升图像识别精度和效率。
   * 技术概要：不借助torch现有Model，阅读论文从零手写每个细节，包括`Position emb`,`Patch emb`等等，学习Transformer基本原理及实现
   * 结果：实现两个版本；1. 纯手写版本，由于需要重头训练模型，代价较高，在微型数据集上运行了几个epoch确认模型收敛。2. 迁移学习版本，基于Pytorch预训练模型，重训head，在微型数据集上达到99%分类准确性。
   
2. Vision Transformer 项目 
   * 项目概要：实现一个基于Vision Transformer的图像分类模型，提升图像识别精度和效率。
   * 技术概要：不借助torch现有Model，阅读论文从零手写每个细节，包括`Position emb`,`Patch emb`等等，学习Transformer基本原理及实现
   * 结果：实现两个版本；1. 纯手写版本，由于需要重头训练模型，代价较高，在微型数据集上运行了几个epoch确认模型收敛。2. 迁移学习版本，基于Pytorch预训练模型，重训head，在微型数据集上达到99%分类准确性。
   

## 获奖经历
* 华山论剑个人金奖（2024）(所有获奖者中唯一14级，其余获奖者均为16+) [获奖照片](https://github.com/Nicooo-Wang/Resume/blob/main/prizes/HuaShanLunJian.jpg)[华为内网链接](https://wiki.huawei.com/domains/73310/wiki/137756/WIKI202501135712539)
* 上海海思 研发好作品奖 [获奖照片](https://github.com/Nicooo-Wang/Resume/blob/main/prizes/HisiliconHaoZuoPin.jpg)
* 芯星奖 (2024) [华为内网链接](https://wiki.huawei.com/domains/73310/wiki/137756/WIKI202501165749786)
* 互联网+省级金奖 [获奖照片](https://github.com/Nicooo-Wang/Resume/blob/main/prizes/Internet%2Bgold.jpg)
* 互联网+省级银奖 [获奖照片](https://github.com/Nicooo-Wang/Resume/blob/main/prizes/Internet%2Bsilver.jpg)
* 研究生二等奖学金（2020）
* 研究生二等奖学金（2019）

## 个人账号
* blog 地址 [主要分享架构设计、测试驱动开发等内容](https://nicooo-wang.github.io/)
* Wechat && 手机号 18092430560

## 其他信息
* 有技术追求，
* 英语雅思6.5，能够无压力听懂英文课程、讲座等
* 性格开朗，易于相处