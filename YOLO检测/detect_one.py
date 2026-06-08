from ultralytics import YOLO

if __name__ == '__main__':
    # 加载一个预训练的模型，推荐用于迁移学习
    # 可选: 'yolov8n.pt', 'yolov8s.pt', 'yolov8m.pt', 'yolov8l.pt', 'yolov8x.pt'
    model = YOLO('yolov8n.pt') 

    # 开始训练模型
    results = model.train(
        data=r"D:\YOLO检测一张图片\datasets\bvm\insulator.yaml",
        epochs=10,          # 10轮足够感受过程
        imgsz=320,          # 更小分辨率，CPU 跑得快
        batch=2,
        device="cpu",       # 明确用 CPU
        verbose=True,       # 打印详细日志
    )
    print("训练完成!")