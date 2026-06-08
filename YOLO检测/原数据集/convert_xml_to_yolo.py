"""
将 Pascal VOC XML 标注转换为 YOLOv8 格式 TXT，
同时合并 Defective_Insulators 的 defect + insulator 标注，
并按比例划分 train/val/test 集。
"""

import xml.etree.ElementTree as ET
import os
import random
import shutil
from pathlib import Path

# ============ 配置 ============
DEFECTIVE_DIR = Path("Defective_Insulators")
NORMAL_DIR = Path("Normal_Insulators")
OUTPUT_DIR = Path("yolo_dataset")

RANDOM_SEED = 42
TRAIN_RATIO = 0.7
VAL_RATIO = 0.15
# TEST_RATIO = 0.15 (余量)

CLASSES = ["defect", "insulator"]  # defect=0, insulator=1

# ============ XML 解析 ============
def parse_voc_xml(xml_path):
    """解析 Pascal VOC XML，返回 [(class_id, x_c, y_c, w, h), ...]（归一化坐标）"""
    tree = ET.parse(xml_path)
    root = tree.getroot()

    width = int(root.find("size/width").text)
    height = int(root.find("size/height").text)

    objects = []
    for obj in root.findall("object"):
        name = obj.find("name").text
        if name not in CLASSES:
            continue
        class_id = CLASSES.index(name)

        bbox = obj.find("bndbox")
        xmin = int(bbox.find("xmin").text)
        ymin = int(bbox.find("ymin").text)
        xmax = int(bbox.find("xmax").text)
        ymax = int(bbox.find("ymax").text)

        # 转 YOLO 格式：class x_center y_center width height（归一化）
        x_center = ((xmin + xmax) / 2) / width
        y_center = ((ymin + ymax) / 2) / height
        w = (xmax - xmin) / width
        h = (ymax - ymin) / height

        objects.append((class_id, x_center, y_center, w, h))

    return objects


# ============ 收集所有样本 ============
def collect_samples():
    """返回 [(image_path, annotations), ...]"""
    samples = []

    # --- Defective_Insulators ---
    defect_xml_dir = DEFECTIVE_DIR / "labels" / "defect"
    insulator_xml_dir = DEFECTIVE_DIR / "labels" / "insulator"
    img_dir = DEFECTIVE_DIR / "images"

    defect_xmls = {p.stem: p for p in defect_xml_dir.glob("*.xml")}
    insulator_xmls = {p.stem: p for p in insulator_xml_dir.glob("*.xml")}
    common_stems = sorted(set(defect_xmls) & set(insulator_xmls))

    for stem in common_stems:
        img_path = img_dir / f"{stem}.jpg"
        if not img_path.exists():
            continue
        # 合并 defect + insulator 标注
        objs = parse_voc_xml(defect_xmls[stem]) + parse_voc_xml(insulator_xmls[stem])
        if objs:
            samples.append((img_path, objs))

    # --- Normal_Insulators ---
    normal_xml_dir = NORMAL_DIR / "labels"
    normal_img_dir = NORMAL_DIR / "images"

    for xml_path in sorted(normal_xml_dir.glob("*.xml")):
        stem = xml_path.stem
        img_path = normal_img_dir / f"{stem}.jpg"
        if not img_path.exists():
            continue
        objs = parse_voc_xml(xml_path)
        if objs:
            samples.append((img_path, objs))

    return samples


# ============ 划分数据集 ============
def split_samples(samples):
    """按比例划分 train/val/test，保证每种类别在各集中都有代表"""
    random.seed(RANDOM_SEED)
    random.shuffle(samples)

    total = len(samples)
    train_end = int(total * TRAIN_RATIO)
    val_end = train_end + int(total * VAL_RATIO)

    return {
        "train": samples[:train_end],
        "val": samples[train_end:val_end],
        "test": samples[val_end:],
    }


# ============ 写入 YOLO 数据集 ============
def write_dataset(splits):
    """写入 YOLO 格式的图片和标签到 OUTPUT_DIR"""
    for split_name, split_samples in splits.items():
        img_out_dir = OUTPUT_DIR / "images" / split_name
        label_out_dir = OUTPUT_DIR / "labels" / split_name
        img_out_dir.mkdir(parents=True, exist_ok=True)
        label_out_dir.mkdir(parents=True, exist_ok=True)

        for img_path, objs in split_samples:
            # 复制图片
            dst_img = img_out_dir / img_path.name
            shutil.copy2(img_path, dst_img)

            # 写标签
            txt_path = label_out_dir / f"{img_path.stem}.txt"
            with open(txt_path, "w", encoding="utf-8") as f:
                for obj in objs:
                    class_id, x_c, y_c, w, h = obj
                    f.write(f"{class_id} {x_c:.6f} {y_c:.6f} {w:.6f} {h:.6f}\n")

        print(f"  {split_name}: {len(split_samples)} 张图片")


def write_yaml():
    """写 dataset.yaml"""
    yaml_path = OUTPUT_DIR / "dataset.yaml"
    yaml_content = f"""# YOLOv8 数据集配置
path: {OUTPUT_DIR.resolve().as_posix()}
train: images/train
val: images/val
test: images/test

nc: {len(CLASSES)}
names: {CLASSES}
"""
    yaml_path.write_text(yaml_content, encoding="utf-8")
    print(f"  dataset.yaml 已生成")


# ============ 主流程 ============
def main():
    print("=== 收集样本 ===")
    samples = collect_samples()
    print(f"  共收集 {len(samples)} 个样本")

    # 统计类别分布
    class_counts = {c: 0 for c in CLASSES}
    for _, objs in samples:
        for obj in objs:
            class_counts[CLASSES[obj[0]]] += 1
    for cls, cnt in class_counts.items():
        print(f"  类别 '{cls}': {cnt} 个标注框")

    print("\n=== 划分数据集 ===")
    splits = split_samples(samples)
    for name, data in splits.items():
        print(f"  {name}: {len(data)} 张")

    print("\n=== 写入 YOLO 数据集 ===")
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    write_dataset(splits)
    write_yaml()

    print(f"\n完成！数据集已保存到: {OUTPUT_DIR.resolve()}")
    print(f"   使用: yolo train data={OUTPUT_DIR / 'dataset.yaml'}")


if __name__ == "__main__":
    main()
