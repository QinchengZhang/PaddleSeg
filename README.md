English | [简体中文](README_CN.md)

# PaddleSeg

[![Build Status](https://travis-ci.org/PaddlePaddle/PaddleSeg.svg?branch=master)](https://travis-ci.org/PaddlePaddle/PaddleSeg)
[![License](https://img.shields.io/badge/license-Apache%202-blue.svg)](LICENSE)
[![Version](https://img.shields.io/github/release/PaddlePaddle/PaddleSeg.svg)](https://github.com/PaddlePaddle/PaddleSeg/releases)
![python version](https://img.shields.io/badge/python-3.6+-orange.svg)
![support os](https://img.shields.io/badge/os-linux%2C%20win%2C%20mac-yellow.svg)

<img src="./docs/images/seg_news_icon.png" width="50"/> *[2020-12-18] PaddleSeg has released the v2.0.0-rc version, which supports the dynamic graph by default. The static-graph codes have been moved to [legacy](./legacy). See detailed [release notes](./docs/release_notes.md).*

![demo](./docs/images/cityscapes.gif)

Welcome to PaddleSeg! PaddleSeg is an end-to-end image segmentation development kit developed based on [PaddlePaddle](https://www.paddlepaddle.org.cn), which covers a large number of high-quality segmentation models in different directions such as *high-performance* and *lightweight*. With the help of modular design, one can conveniently complete the entire image segmentation application from training to deployment through configuration calls or API calls.

## Core features

**High performance model**: Based on the high-performance backbone trained by Baidu's self-developed [semi-supervised label knowledge distillation scheme (SSLD)](https://paddleclas.readthedocs.io/zh_CN/latest/advanced_tutorials/distillation/distillation.html#ssld), combined with the state of the art segmentation technology, we provides 50+ high-quality pre-training models, which are better than other open source implementations.

**Modular design**: PaddleSeg support 15+ mainstream *segmentation networks*, developers can start based on actual application scenarios and assemble diversified training configurations combined with modular design of *data enhancement strategies*, *backbone networks*, *loss functions* and other different components to meet different performance and accuracy requirements.

**High efficiency**: PaddleSeg provides multi-process asynchronous I/O, multi-card parallel training, evaluation and other acceleration strategies, combined with the memory optimization function of the PaddlePaddle, which can greatly reduce the training overhead of the segmentation model, all this allowing developers to lower cost and more efficiently train image segmentation model.

## Model Zoo

|Model\Backbone|ResNet50|ResNet101|HRNetw18|HRNetw48|
|-|-|-|-|-|
|[ANN](./configs/ann)|✔|✔|||
|[BiSeNetv2](./configs/bisenet)|-|-|-|-|
|[DANet](./configs/danet)|✔|✔|||
|[Deeplabv3](./configs/deeplabv3)|✔|✔|||
|[Deeplabv3P](./configs/deeplabv3p)|✔|✔|||
|[Fast-SCNN](./configs/fastscnn)|-|-|-|-|
|[FCN](./configs/fcn)|||✔|✔|
|[GCNet](./configs/gcnet)|✔|✔|||
|[GSCNN](./configs/gscnn)|✔|✔|||
|[HarDNet](./configs/hardnet)|-|-|-|-|
|[OCRNet](./configs/ocrnet/)|||✔|✔|
|[PSPNet](./configs/pspnet)|✔|✔|||
|[U-Net](./configs/unet)|-|-|-|-|
|[U<sup>2</sup>-Net](./configs/u2net)|-|-|-|-|
|[Att U-Net](./configs/attention_unet)|-|-|-|-|
|[U-Net++](./configs/unet_plusplus)|-|-|-|-|
|[EMANet](./configs/emanet)|✔|✔|-|-|
|[ISANet](./configs/isanet)|✔|✔|-|-|
## Dataset

- [x] Cityscapes
- [x] Pascal VOC
- [x] ADE20K
- [ ] Pascal Context
- [ ] COCO stuff

## Installation

#### step 1. Install PaddlePaddle

System Requirements:
* PaddlePaddle >= 2.0.0rc
* Python >= 3.6+

Highly recommend you install the GPU version of PaddlePaddle, due to large overhead of segmentation models, otherwise it could be out of memory while running the models. For more detailed installation tutorials, please refer to the official website of [PaddlePaddle](https://www.paddlepaddle.org.cn/documentation/docs/zh/2.0-beta/install/index_cn.html)。


#### step 2. Install PaddleSeg

```shell
pip install paddleseg
```


#### step 3. Download PaddleSeg repo

```shell
git clone https://github.com/PaddlePaddle/PaddleSeg
```

## Quick Training
```shell
python train.py --config configs/quick_start/bisenet_optic_disc_512x512_1k.yml
```

## Tutorials

* [Get Started](./docs/quick_start.md)
* [API Tutorial](https://aistudio.baidu.com/aistudio/projectdetail/1339458)
* [Data Preparation](./docs/data_prepare.md)
* [Training Configuration](./configs/)
* [API references](./docs/apis)
* [Add New Components](./docs/add_new_model.md)


## Feedbacks and Contact
* The dynamic version is still under development, if you find any issue or have an idea on new features, please don't hesitate to contact us via [GitHub Issues](https://github.com/PaddlePaddle/PaddleSeg/issues).
* PaddleSeg User Group (QQ): 850378321 or 793114768

## Acknowledgement
* Thanks [jm12138](https://github.com/jm12138) for contributing U<sup>2</sup>-Net.
* Thanks [zjhellofss](https://github.com/zjhellofss) (Fu Shenshen) for contributing Attention U-Net, and Dice Loss.
* Thanks [liuguoyu666](https://github.com/liguoyu666) for contributing U-Net++.
