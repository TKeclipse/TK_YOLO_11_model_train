import os
import yaml

def rename_jpg_to_lowercase(root_dir):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".JPG"):
                old_path = os.path.join(subdir, file)
                new_path = os.path.join(subdir, file[:-4] + ".jpg")
                print(f"Renaming: {old_path} -> {new_path}")
                os.rename(old_path, new_path)

def check_it_working():
    labels = r"D:\resources\front_bumper\labels\train"

    for f in os.listdir(labels):
        if f.endswith(".txt"):
            path = os.path.join(labels, f)
            if os.path.getsize(path) > 0:
                print("OK:", f)
            else:
                print("EMPTY:", f)


def check_empty_labels():
    root = r"D:\resources\front_bumper"
    for path, dirs, files in os.walk(root):
        for f in files:
            if f.endswith(".txt"):
                full = os.path.join(path, f)
                if os.path.getsize(full) == 0:
                    print("EMPTY LABEL:", full)

def label_img():
    labels = r"D:\resources\front_bumper\labels\train"

    for f in os.listdir(labels):
        if f.endswith(".txt"):
            path = os.path.join(labels, f)
            if os.path.getsize(path) > 0:
                print("OK:", f)
            else:
                print("EMPTY:", f)

def label_img2():
    ROOT = r"D:\resources\front_bumper"

    for path, dirs, files in os.walk(ROOT):
        for f in files:
            if f.endswith(".txt") and os.path.getsize(os.path.join(path, f)) > 0:
                print("FOUND NON-EMPTY LABEL:", os.path.join(path, f))


def main():
    yaml_path = "dataset.yaml"

    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    # get all directories fron train и val
    dirs = []

    if "train" in data:
        dirs.extend(data["train"])

    if "val" in data:
        dirs.extend(data["val"])


    for d in dirs:
        if os.path.exists(d):
            print(f"\nScanning: {d}")
            rename_jpg_to_lowercase(d)
        else:
            print(f"Directory not found: {d}")

    check_empty_labels()
    label_img()
    check_it_working()

if __name__ == "__main__":
    main()