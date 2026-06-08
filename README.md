# .github.io
个人作品集

1. YOLO检测
这里涉及我们大创项目中的视觉检测图像。
作用是能够通过 `datasets/bvm/images/train` 与 `datasets/bvm/labels/train` 的图像训练出模型，
再利用该模型对 `datasets/bvm/images/val` 与 `datasets/bvm/labels/val` 自动识别并标出绝缘子。

绝缘子（英文：insulator）是电力系统中实现电气绝缘和机械支撑，将导线与杆塔或其他支撑结构隔离，防止电流意外流向地面的特殊绝缘控件。
但其实我们想要做的是检测高铁用的绝缘子，因为尚未找到高铁绝缘子足够多的数据集，所以先拿网上的电网绝缘子图像练手。

代码在腾讯云平台中运行可以出结果，直接在本地中运行不行，可能是 Windows 系统或者本地上没有 GPU 的问题。

此外，大创还涉及 ROS2 仿真以及通信等内容，目前处于学习阶段。

2. 数据分析
此处并没有代码的部分，是在网课上学习数据分析和可视化工具的时候做的。
`月度销售数据监控.xlsx` 对源数据 Sheet 中的数据进行分析和可视化报表制作，包含 Excel 图表的月度销售监控看板。
Tableau 交互式图表见：
https://public.tableau.com/app/profile/.20381734/viz/2_17808986866470/1?publish=yes
对应的打包工作簿文件为 `sales.twbx`，需要在 Tableau Desktop 或 Tableau Reader 中打开查看。
