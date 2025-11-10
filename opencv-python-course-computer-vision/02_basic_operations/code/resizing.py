# resizing
import os

import cv2

# image_path = os.path.join('..', '..', 'data_global', 'dog.jpg')
image_path = os.path.join('/home/isaac/cv/opencv-python-course-computer-vision/data_global', 'dog.jpg')
img = cv2.imread(image_path)

resized_img = cv2.resize(img, (640, 540)) # (width, height)

print(f"image size: {img.shape}") # (height, width) | Notice the difference
print(f"resized image: {resized_img.shape}")

cv2.imshow('img', img)
cv2.imshow('resized_img', resized_img)
cv2.waitKey(0)
