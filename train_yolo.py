from ultralytics import YOLO

# Load your first trained model as a starting point
model = YOLO(r"D:\Downloads\Code\YOLO11m-Car-Damage-Detector\runs\detect\train57\weights\best.pt")

# Train again on the improved dataset
model.train(
    data="dataset.yaml",
    epochs=100,
    imgsz=640,
    device=0,
    workers=0,
    batch=8
)

# Validate
model.val()

# Export to ONNX
model.export(format="onnx")