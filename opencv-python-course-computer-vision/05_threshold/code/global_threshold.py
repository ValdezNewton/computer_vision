import os

import cv2

# Thresholding: A technique that segments an image based on their intensity. Its goal is to create a binary image fr
# a grayscale image separating pixels into two distinct categories: 1 that meets the threshold condition (foreground)
# , the other doesn't (background)

img = cv2.imread(os.path.join('.', 'bear.jpg'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY) 
# ret, thresh = cv2.threshold(src, thresh_value, max_value, threshold_type)
# Pixels with intensity >= thresh_value are set to 255 (white), others to 0 (black)
# ret, thresh = cv2.threshold(img_gray, 80, 230, cv2.THRESH_BINARY) 
# Here, pixels with intensity >= 80 (including 231~255) are set to 230 (light gray), others to 0 (black)
# ret is the 1st variable, it holds the threshold value (80)
# thresh is the 2nd variable, it holds the thresholded image

thresh_blur = cv2.blur(thresh, (10, 10)) # Blurring the thresholded image to reduce noise and improve segmentation
ret, thresh_blur = cv2.threshold(thresh_blur, 80, 255, cv2.THRESH_BINARY)

cv2.imshow('img', img)
cv2.imshow('img_gray', img_gray)
cv2.imshow('thresh', thresh)
cv2.imshow('thresh_improved', thresh_blur)
cv2.waitKey(0)