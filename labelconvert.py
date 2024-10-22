from pathlib import Path
import json
import cv2

valpath = Path(__file__).parent / "annotation_val.odgt"
trainpath = Path(__file__).parent / "annotation_train.odgt"
valoutpath = Path(__file__).parent / "val.txt"
trainoutpath = Path(__file__).parent / "train.txt"
imgpath = [Path(__file__).parent / f"CrowdHuman_train0{i}" for i in range(1, 4)]
# Open the file in binary mode
data = []
imgs = []
for i in imgpath:
    imgs.append(i.glob("*.jpg"))

with open(valpath, "r") as vin:
    # Load the object from the file
    data.append(json.loads(vin.readline()))

