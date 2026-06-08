# .github.io
个人作品集

1. YOLO检测
这里涉及我们大创项目中的视觉检测图像。
作用是能够通过~\.github.io\YOLO检测\datasets\bvm\images\train与~\.github.io\YOLO检测\datasets\bvm\labels\train的图像训练出模型
再利用该模型对~\.github.io\YOLO检测\datasets\bvm\images\val与~\.github.io\YOLO检测\datasets\bvm\labels\val,自动识别并标出绝缘子

绝缘子（英文：insulator）是电力系统中的实现电气绝缘和机械支撑，将导线与杆塔或其他支撑结构隔离，防止电流意外流向地面的特殊绝缘控件。
但其实我们想要做的是检测高铁用的绝缘子，因为尚未找到高铁绝缘子足够多的数据集，所以先拿网上的电网绝缘子图像练手

代码在腾讯云平台中运行可以出结果，直接在本地中运行不行
可能是WIndows系统或者本地上没有GPU的问题