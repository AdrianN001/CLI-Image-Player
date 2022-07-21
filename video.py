from main import CliPlayer
from PIL import Image
import cv2
import time
import os

video = cv2.VideoCapture("sample.mp4")

frames = []

while True:
    success, frame = video.read()

    if success:
        frames.append(frame)
    else:
        break

print(frames[0])
images = []
for frame in frames:
    color_coverted = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(color_coverted)
    images.append(pil_image)


for index in range(len(images)):
    CliPlayer(image = images[index]).show()