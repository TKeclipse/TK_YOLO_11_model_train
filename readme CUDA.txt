Cuda

- remove CPU version if exist

pip uninstall torch torchvision torchaudio -y

- Installing PyTorch with Cuda 11.8 for 1080ti (pascal)

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

- check GPU is working:

import torch
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))

	should return: True
				   NVIDIA GeForce GTX 1080 Ti
				   
- How to use GPU in Yolo model:

	train_results = model.train(
    data="dataset.yaml",
    epochs=100,
    imgsz=640,
    device=0,   # <-- GPU
)


Label images 
file_fix.py
pip install labelImg
label_img()
