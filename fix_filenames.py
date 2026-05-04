import os

ROOT = r"D:\resources\front_bumper"

for path, dirs, files in os.walk(ROOT):
    for f in files:
        if f.endswith(".JPG"):
            old = os.path.join(path, f)
            new = os.path.join(path, f[:-4] + ".jpg")
            print("Renaming:", old, "->", new)
            os.rename(old, new)