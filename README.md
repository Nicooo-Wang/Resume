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

* 性格开朗，拥有强烈的技术追求，具备出色的学习能力和求知欲。在工作之余积极钻研软件架构技术，学习 AI 算法及 AI Infra，并有初步的项目积累。

* **软件开发**：精通 C/C++ 语言的架构设计与开发，拥有丰富的多线程编程和性能优化经验。入职两年来获得**华山论剑个人金奖、上海海思优秀作品奖、芯火奖**等多个荣誉。负责AIPQ-Service模块的架构设计与开发，以及AI软件栈的重构方案设计与开发；熟悉驱动开发，具备多颗海思画质芯片的驱动维护与开发经验。

* **AI Infra**：掌握AI Infra相关技术栈，**独立开发Needle神经网络推理库**。了解CUDA和OpenCL算子开发，熟悉反向传播算法及常用高性能算子优化（如Conv、Matmul）。

* **AI算法**：熟悉常用神经网络算法的原理，能够独立复现常见、经典AI算法，曾复现过**Vision Transformer、FCOS**等经典算法。能够熟练运用**迁移学习、模型蒸馏**等模型训练与优化技术。

## 项目经历
### 软件方向

AIPQ-Service - \[华为-海思\] - 软件架构设计、开发 - 2024.2-2024.8

* **项目背景**：通过用户态进程运行分类网络，动态计算图像优化参数，以提升码流播放场景下的图像质量。
* **应用技术**：神经网络部署、OpenCL 算子开发、多线程并行。
* **架构设计**：采用工厂模式和责任链模式实现多芯片、多形态算法流水线的灵活组装，解决架构演进问题；利用 RAII 技术优化高负载多资源模块的资源管理。
* **测试设计**：通过架构分层解耦，显著提高可测试性，设计并实现自动化测试用例6500+。
* **技术难点**：
	* 实现 OpenCL 算子编写，满足模型前后处理需求。
	* 处理多芯片、多形态算法的差异，多算法并行方案调度复杂，资源管理困难。
	* 性能要求极高，单一算法需要多worker协作，完成算法处理，同时保证资源线程安全。
* **算法优化**：通过迁移学习和模型蒸馏，将模型准确率从 **83% 提升至 89%**。
* **性能设计**：设计 DMA 零拷贝方案、模型硬化方案等，有效降低内存拷贝次数，**优化 DDR 带宽 50%**；识别并推动 Cast 取帧方案落地，**优化 CPU 占用 12%**。
* **项目总结**：架构设计获得 **华山论剑个人金奖**；45天从无到有完成方案架构设计，代码开发 9000+ 行，**上线一年仅一例提单**。
* **商业成果**：借助 AIPQ 特性，动态调整画质效果参数，成功使 6x 系低成本芯片与 8x 系芯片竞争力持平。

**AI 软件栈重构 - \[华为-海思\] - 开发 - 2023.10-2024.2**

* **项目概要**：旧有 AI 软件栈架构严重腐化，测试发现 20 余个致命问题，功能基本处于不可用状态。旧有架构实现绑定了 Ascend 生态，需要重新设计和重构该模块，以适配 AI-HAL 模块，完成神经网络推理功能。

* **技术难点**：
  * 安卓架构的通信机制复杂，AI 软件栈需通过 Binder接口 完成 System 和 Vendor 侧进程通信。在向前兼容旧接口的同时，还需支持后续架构演进，对代码架构设计提出了更高的要求。
  * 南向支持安卓 NDK C++ 和 JAVA 接口调用，北向适配 AI-HAL 接口。在待机唤醒、异步推理等场景中需要涉及复杂的资源管理和线程安全。

* **结果**：AI 软件栈顺利完成重构，核心代码上库 6000+ 行，测试用例代码 2 万+ 行，上库当月问题单数量仅 2 例。


**AI-HAL 北向适配层 - \[华为-海思\] - 开发 - 2023.6-2023.10**

* **项目概要**：AI-HAL 是一个 C API 模块，专为 TVOS 和 HL 平台运行神经网络推理而设计。通过 AI-HAL 模块，TVOS 和 HL 平台可以完成多家 AI 生态的导入。

* **技术难点**：设计接口以兼容现有 AI 生态，同时支持多线程、多模型同步、异步推理和 Profiling dump 等功能。

* **结果**：AI-HAL 成为 TVOS 的 AI 生态标准，同年支撑 9XX 高端芯片 AI 特性交付。

* **项目总结**：AI-HAL 是项目组中首个以 C 语言面向对象方式组织、测试驱动开发为流程的模块，架构清晰，代码优秀，获得 **上海海思研发好作品奖**。

### AI Infra
**Needle - 2024.6-2025.1**

* **项目概要**：Needle 是一个简易版 PyTorch 的实现，其项目框架源自 [CMU 10-414/714](https://dlsyscourse.org/) Deep Learning System 课程。通过 Needle，用户能够在 Python 侧使用简洁的接口定义模型，轻松完成神经网络的训练和推理，降低了深度学习模型开发的复杂性。

* **自动微分（Automatic Differentiation）**：通过抽象类 `NDArray`、`Tensor` 和 `Device`，实现了自动梯度推导，支持两种模式：eager mode 和 lazy model，满足多种使用场景。
* **算子支持（Operator Support）**：支持了常用的大多数算子，如 `Stack`、`Permute` 等。其中，`Conv (Im2Col)` 和 `Matmul (2D Tiling)` 算子的性能达到了 NVIDIA cuBLAS 的 68%，在大规模矩阵运算中展现出优越的计算效率，极大提升了模型的运行速度。
* **后端支持（Backend）**：通过 `Device` 的抽象，成功实现了对 `numpy`、`CUDA` 和 `CPU` 三种后端的支持，确保了模型能够在不同硬件环境下高效运行。这种设计使得用户能够根据需求灵活选择计算后端，优化资源利用。
* **优化器（Optimizers）**：实现了 `Adam` 和 `SGD` 两种常用的优化器，提供了多种训练策略以满足不同模型的需求。
* **常用模型（Common Models）**：编写了 `ResNet9` 模型，并在 CIFAR 数据集上成功验证，展示了 Needle 可靠性。

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
* 华山论剑个人金奖（2024）(所有获奖者中唯一14级，其余获奖者均为16+) [\[获奖照片\]](https://github.com/Nicooo-Wang/Resume/blob/main/prizes/HuaShanLunJian.jpg)[\[华为内网链接\]](https://wiki.huawei.com/domains/73310/wiki/137756/WIKI202501135712539)
* 上海海思 研发好作品奖 [\[获奖照片\]](https://github.com/Nicooo-Wang/Resume/blob/main/prizes/HisiliconHaoZuoPin.jpg)
* 芯星奖 (2024) [\[华为内网链接\]](https://wiki.huawei.com/domains/73310/wiki/137756/WIKI202501165749786)
* 互联网+省级金奖 [\[获奖照片\]](https://github.com/Nicooo-Wang/Resume/blob/main/prizes/Internet%2Bgold.jpg)
* 互联网+省级银奖 [\[获奖照片\]](https://github.com/Nicooo-Wang/Resume/blob/main/prizes/Internet%2Bsilver.jpg)
* 研究生二等奖学金（2020）
* 研究生二等奖学金（2019）

## 个人账号
* blog 地址 [主要分享架构设计、测试驱动开发等内容](https://nicooo-wang.github.io/)
* Wechat && 手机号 18092430560

## 其他信息
* 有技术追求，
* 英语雅思6.5，能够无压力听懂英文课程、讲座等
* 性格开朗，易于相处
