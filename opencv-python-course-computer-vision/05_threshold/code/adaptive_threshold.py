import os

import cv2


img = cv2.imread(os.path.join('.', 'handwritten.png'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

adaptive_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)
ret, simple_thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)
# cv2.ADAPTIVE_THRESH_GAUSSIAN_C: The threshold value is calculated as a weighted sum of neighborhood values where weights are a Gaussian window.

cv2.imshow('img', img)
cv2.imshow('img_gray', img_gray)
cv2.imshow('adaptive_thresh', adaptive_thresh)
cv2.imshow('simple_thresh', simple_thresh)
cv2.waitKey(0)

# Adaptive thresholding is a technique where the threshold value isn't fixed across the entire image.
# It is computed for each pixel based on its local neighborhood.
# Useful for images with varying lighting conditions, like handwritten text or scanned documents with uneven light.
