from ultralytics import YOLO
import os

model = YOLO(r"best.pt")

images_dir = r"D:/resources/front_bumper/images/train"
labels_dir = r"D:/resources/front_bumper/labels/train"

os.makedirs(labels_dir, exist_ok=True)

results = model.predict(
    source=images_dir,
    save_txt=True,
    save_conf=False,
    save_crop=False,
    project="auto_labels",
    name="yolo"
)