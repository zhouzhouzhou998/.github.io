from ultralytics import YOLO

if __name__ == '__main__':
    # 加载一个预训练的模型，推荐用于迁移学习
    # 可选: 'yolov8n.pt', 'yolov8s.pt', 'yolov8m.pt', 'yolov8l.pt', 'yolov8x.pt'
    model = YOLO('yolov8n.pt') 

    # 开始训练模型
    results = model.train(
        data="datasets/bvm/insulator.yaml",
        epochs=50,          # GPU训练，增加轮数以提升效果
        imgsz=640,          # 标准分辨率
        batch=16,
        device="cuda",      
        verbose=True,       # 打印详细日志
    )
    print("训练完成!")