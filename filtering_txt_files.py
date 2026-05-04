import os

LABELS = r"D:/resources/front_bumper/labels/train"

MIN_AREA = 0.01      # mina area (1%)
MAX_AREA = 0.40      # max area (40%)
MIN_WH = 0.02        # min width height
MAX_WH_RATIO = 6.0   # max width height ratio

for txt in os.listdir(LABELS):
    if not txt.endswith(".txt"):
        continue

    path = os.path.join(LABELS, txt)
    new_lines = []

    with open(path, "r") as f:
        for line in f:
            cls, cx, cy, w, h = line.strip().split()
            cx, cy, w, h = map(float, (cx, cy, w, h))

            area = w * h
            ratio = max(w/h, h/w)

            if area < MIN_AREA:
                continue
            if area > MAX_AREA:
                continue
            if w < MIN_WH or h < MIN_WH:
                continue
            if ratio > MAX_WH_RATIO:
                continue

            new_lines.append(line)

    with open(path, "w") as f:
        f.writelines(new_lines)

print("Filtering done!")