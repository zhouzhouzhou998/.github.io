# YOLO 绝缘子检测

这里涉及我们大创项目中的视觉检测图像。
作用是能够通过 `datasets/bvm/images/train` 与 `datasets/bvm/labels/train` 的图像训练出模型，
再利用该模型对 `datasets/bvm/images/val` 与 `datasets/bvm/labels/val` 自动识别并标出绝缘子。

绝缘子（英文：insulator）是电力系统中实现电气绝缘和机械支撑，将导线与杆塔或其他支撑结构隔离，防止电流意外流向地面的特殊绝缘控件。
但其实我们想要做的是检测高铁用的绝缘子，因为尚未找到高铁绝缘子足够多的数据集，所以先拿网上的电网绝缘子图像练手。

## 数据集

源数据集取自中国输电线路绝缘子数据集（CPLID），提供由无人机拍摄的正常绝缘子图像和合成的缺陷绝缘子图像。
https://github.com/InsulatorData/InsulatorDataSet

### 数据集结构

```
datasets/bvm/
├── images/
│   ├── train/          # 16 张训练图片
│   └── val/            # 7 张验证图片
├── labels/
│   ├── train/          # 18 个训练标注
│   └── val/            # 7 个验证标注
└── insulator.yaml      # 数据集配置文件，使用相对路径
```

## 使用说明

### 训练模型

```bash
python detect_one.py
```

使用 YOLOv8n 预训练模型进行迁移学习，默认在 CPU 上训练 10 个 epoch。

### 环境要求

- Python 3.8+
- ultralytics
- PyTorch

## 注意事项

- 代码在腾讯云平台中运行可以出结果，直接在本地中运行不行
- 可能是 Windows 系统或者本地上没有 GPU 的问题
- 当前为练手阶段，后续目标为高铁绝缘子检测
