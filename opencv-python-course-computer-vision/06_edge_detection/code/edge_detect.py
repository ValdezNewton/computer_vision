import os

import cv2
import numpy as np

image_path = os.path.join('/home/isaac/cv/opencv-python-course-computer-vision/data_global', 'model.jpg')
img = cv2.imread(image_path)

img_edge = cv2.Canny(img, 100, 400)
# cv2.Canny(src, lower_threshold, upper_threshold)
# lower_threshold: Any pixel which its gradient intensity is less than this value is discarded as an edge 
# upper_threshold: Any pixel which its gradient intensity is more than this value is accepted as a strong edge
# lower_threshold < x < upper_threshold: These pixels are accepted as edges only if they are connected to strong edges

img_edge_d = cv2.dilate(img_edge, np.ones((3, 3), dtype=np.int8)) # Thickens the edges
# cv2.dilate(src, kernel)
# np.ones((3,3), dtype=np.int8) creates a 3x3 matrix of ones & it ensures it is of int8 type
# The kernel determines the shape & size of the "neighborhood" around each pixel during dilation. 
# A larger kernel causes more expansion, while a smaller one has a smaller effect.

img_edge_e = cv2.erode(img_edge_d, np.ones((3, 3), dtype=np.int8)) # Make the edges thinner

cv2.imshow('img', img)
cv2.imshow('img_edge', img_edge)
cv2.imshow('img_edge_d', img_edge_d)
cv2.imshow('img_edge_e', img_edge_e)
cv2.waitKey(0)
