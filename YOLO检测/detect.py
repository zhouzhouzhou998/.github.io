from ultralytics import YOLO

if __name__ == '__main__':
    # 加载训练好的模型（优先使用训练产出的 best.pt）
    model = YOLO('runs/detect/train/weights/best.pt')

    # 对测试集图片进行检测
    results = model.predict(
        source="datasets/bvm/images/test",
        imgsz=640,
        device="cuda",
        save=True,              # 保存标注后的图片
        save_txt=True,          # 保存检测结果 txt
        conf=0.5,               # 置信度阈值
    )
    print("检测完成! 结果保存在 runs/detect/predict/")
