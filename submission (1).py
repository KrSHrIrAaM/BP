# -*- coding: utf-8 -*-
"""Submission.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yTe-HnkchGhx7QWP2JBf5APvxoE2CN-A
"""

!pip install ultralytics

from ultralytics import YOLO
import os

# Commented out IPython magic to ensure Python compatibility.

!mkdir -p /content/datasets
# %cd /content/datasets
!curl -L "https://github.com/ultralytics/yolov5/releases/download/v1.0/coco128.zip" -o coco128.zip
!unzip -q coco128.zip

data_yaml = """
path: /content/datasets/coco128
train: images/train
val: images/val

names:
  0: person
  1: bicycle
  2: car
  3: motorcycle
  4: airplane
  5: bus
  6: train
  7: truck
  8: boat
  9: traffic light
 10: fire hydrant
 11: stop sign
 12: parking meter
 13: bench
 14: bird
 15: cat
 16: dog
 17: horse
 18: sheep
 19: cow
 20: elephant
 21: bear
 22: zebra
 23: giraffe
 24: backpack
 25: umbrella
 26: handbag
 27: tie
 28: suitcase
 29: frisbee
 30: skis
 31: snowboard
 32: sports ball
 33: kite
 34: baseball bat
 35: baseball glove
 36: skateboard
 37: surfboard
 38: tennis racket
 39: bottle
 40: wine glass
 41: cup
 42: fork
 43: knife
 44: spoon
 45: bowl
 46: banana
 47: apple
 48: sandwich
 49: orange
 50: broccoli
 51: carrot
 52: hot dog
 53: pizza
 54: donut
 55: cake
 56: chair
 57: couch
 58: potted plant
 59: bed
 60: dining table
 61: toilet
 62: tv
 63: laptop
 64: mouse
 65: remote
 66: keyboard
 67: cell phone
 68: microwave
 69: oven
 70: toaster
 71: sink
 72: refrigerator
 73: book
 74: clock
 75: vase
 76: scissors
 77: teddy bear
 78: hair drier
 79: toothbrush
"""
with open("/content/coco128_full.yaml", "w") as f:
    f.write(data_yaml)

import os, shutil, random

# Paths based on your dataset structure
base_dir = "/content/datasets/coco128"
img_dir = os.path.join(base_dir, "images/train2017")
lbl_dir = os.path.join(base_dir, "labels/train2017")
# Output folders
train_img_out = os.path.join(base_dir, "images/train")
val_img_out = os.path.join(base_dir, "images/val")
train_lbl_out = os.path.join(base_dir, "labels/train")
val_lbl_out = os.path.join(base_dir, "labels/val")

os.makedirs(train_img_out, exist_ok=True)
os.makedirs(val_img_out, exist_ok=True)
os.makedirs(train_lbl_out, exist_ok=True)
os.makedirs(val_lbl_out, exist_ok=True)

# Only include images with matching label files
all_images = [
    f for f in os.listdir(img_dir)
    if f.endswith('.jpg') and os.path.exists(os.path.join(lbl_dir, f.replace('.jpg', '.txt')))
]

random.shuffle(all_images)
train_imgs = all_images[:100]
val_imgs = all_images[100:]

# Copy matching image-label pairs
def split_copy(image_list, img_out, lbl_out):
    for img_file in image_list:
        lbl_file = img_file.replace('.jpg', '.txt')
        shutil.copy(os.path.join(img_dir, img_file), os.path.join(img_out, img_file))
        shutil.copy(os.path.join(lbl_dir, lbl_file), os.path.join(lbl_out, lbl_file))

split_copy(train_imgs, train_img_out, train_lbl_out)
split_copy(val_imgs, val_img_out, val_lbl_out)

print(f"Dataset split complete: {len(train_imgs)} train / {len(val_imgs)} val")

from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.train(data="/content/coco128_10class.yaml", epochs=20, imgsz=640, batch=8)

# Validate your trained model
model = YOLO("/content/datasets/runs/detect/train6/weights/best.pt")
metrics = model.val()

from ultralytics import YOLO
from google.colab import files

uploaded = files.upload()


model = YOLO('yolov8n.pt')


for image_name in uploaded.keys():
    results = model.predict(source=image_name, conf=0.25, show=True)

model = YOLO("/content/datasets/runs/detect/train6/weights/best.pt")


metrics = model.val(data="/content/coco128_10class.yaml", split="val")


print("\n Evaluation Metrics:")
print(f"Precision: {metrics.box.map50:.4f}")
print(f"Recall: {metrics.box.map75:.4f}")
print(f"mAP@50: {metrics.box.map50:.4f}")
print(f"mAP@50-95: {metrics.box.map:.4f}")

from google.colab import drive
drive.mount('/content/drive')