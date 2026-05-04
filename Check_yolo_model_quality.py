from ultralytics import YOLO

model = YOLO(r"D:\Downloads\Code\YOLO11m-Car-Damage-Detector\runs\detect\train57\weights\best.pt")
results = model.val(workers=0, verbose=False)

precision, recall, map50, map5095 = results.mean_results()
# precision, recall, mAP50, mAP50-95.

print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"mAP50: {map50:.2f}")
print(f"mAP50-95: {map5095:.2f}")
