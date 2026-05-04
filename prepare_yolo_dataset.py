import os
import shutil

ROOT = r"D:\resources\front_bumper"

IMAGES_TRAIN = os.path.join(ROOT, "images", "train")
LABELS_TRAIN = os.path.join(ROOT, "labels", "train")

os.makedirs(IMAGES_TRAIN, exist_ok=True)
os.makedirs(LABELS_TRAIN, exist_ok=True)

IMAGE_EXT = {".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"}

print("Collecting images...")

count = 0

for path, dirs, files in os.walk(ROOT):

    if IMAGES_TRAIN in path or LABELS_TRAIN in path:
        continue

    for f in files:
        ext = os.path.splitext(f)[1]
        if ext in IMAGE_EXT:
            src = os.path.join(path, f)
            dst_img = os.path.join(IMAGES_TRAIN, f)

            if not os.path.exists(dst_img):
                shutil.copy2(src, dst_img)

            label_name = os.path.splitext(f)[0] + ".txt"
            dst_label = os.path.join(LABELS_TRAIN, label_name)

            if not os.path.exists(dst_label):
                open(dst_label, "w").close()

            count += 1

print(f"Ready! Processed images: {count}")

root_fixed = ROOT.replace("\\", "/")

yaml_content = f"""path: {root_fixed}

train: images/train
val: images/train

names:
  0: bumper
  1: window
  2: scratch
  3: dent
  4: crack
"""

with open('dataset.yaml', "w", encoding="utf-8") as f:
    f.write(yaml_content.strip())

print("dataset.yaml created successfully!")