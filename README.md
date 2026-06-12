# .github.io
个人作品集

1. YOLO检测
这里涉及我们大创项目中的视觉检测图像。
作用是能够通过~\.github.io\YOLO检测\datasets\bvm\images\train与~\.github.io\YOLO检测\datasets\bvm\labels\train的图像训练出模型
再利用该模型对~\.github.io\YOLO检测\datasets\bvm\images\val与~\.github.io\YOLO检测\datasets\bvm\labels\val,自动识别并标出绝缘子

绝缘子（英文：insulator）是电力系统中的实现电气绝缘和机械支撑，将导线与杆塔或其他支撑结构隔离，防止电流意外流向地面的特殊绝缘控件。
但其实我们想要做的是检测高铁用的绝缘子，因为尚未找到高铁绝缘子足够多的数据集，所以先拿网上的电网绝缘子图像练手

代码在腾讯云平台中运行可以出结果，直接在本地中运不行.可能是WIndows系统或者本地上没有GPU的问题

2. 数据分析
此处并没有代码的部分，是在网课上学习数据分析和可视化工具的时候做的
`月度销售数据监控.xlsx` 对源数据 Sheet 中的数据进行分析和可视化报表制作，包含 Excel 图表的月度销售监控看板。

点击标题处的月份、区域筛选器可以调整图表的的颗粒度
按住ctrl可以多选

在 Tableau 中，对相同数据源制作可交互性图表：
https://public.tableau.com/app/profile/.20381734/viz/2_17808986866470/1?publish=yes
对应的打包工作簿文件为 `sales.twbx`，但是本地需要下载 Tableau Desktop 或 Tableau Reader 中打开查看。

标题右侧，滑动日期条和选择门店名称可实现筛选功能
同时，点击任何数据（包括 表格单元格 和 饼图扇形区域 和 堆叠图）也可以进行筛选

3. 对于大创，其实还有涉及ROS2仿真以及通信等内容，但是还相处于学习阶段，还相当不成熟

4. 只有个人网页与pdf由AI全盘生成
