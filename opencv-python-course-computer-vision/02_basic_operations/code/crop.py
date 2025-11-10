# crop
import os

import cv2

image_path = os.path.join('..', '..', 'data_global', 'leaf.jpg')
img = cv2.imread(image_path)

print(img.shape)

cropped_img = img[140:470, 80:350] # specify the range of numpy array (height, width)
# The above is a simple method of cropping by using slicing method
cv2.imshow('img', img)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0)
