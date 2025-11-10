import os

import cv2


img = cv2.imread(os.path.join('.', 'birds.jpg'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV) 
# cv2.THRESH_BINARY_INV inverts colors: pixel vales >= 127 are set to 0 (black), pixel values < 127 are set to 255 (white)
# cv2.THRESH_BINARY: pixel vales >= 127 are set to 255 (white), pixel values < 127 are set to 0 (black)
# cv2.threshold() returns two values: ret & thresh
# ret stores the threshold value used (127 here)
# thresh stores the thresholded image
# After thresholding the `img_gray` image, each pixel in the image (either 0 or 255) is stored in `thresh`.

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.RETR_TREE: The contour retrieval mode. It retrieves all the contours and organizes them into a tree structure
# where each contour can have child contours (useful for detecting nested
# cv2.CHAIN_APPROX_SIMPLE: The contour approximation method that compresses horizontal, vertical, and diagonal segments of 
# the contour to save memory. This method stores only the endpoints of the contour segments.

# contours: A list of contours found in the binary image. Each contour is stored as a list of points (coordinates) that 
# form the contour's boundary.
# hierarchy: Information about the hierarchy of contours, telling you the relationship between parent and child contours 
# (if any). You typically don't need to use this in simple applications.

for cnt in contours: # loops thru each contour in countours list
    if cv2.contourArea(cnt) > 200: # If a contour's area is greater than 200 pixels (allows us to remove contours surrounding noise)
        # cv2.drawContours(img, cnt, -1, (0, 255, 0), 1) # Draws the contour cnt on the image img

        x1, y1, w, h = cv2.boundingRect(cnt) # cv2.boundingRect(cnt) calc the bounding rectangle around the contour cnt.
        # The function returns the top-left corner coordinates (x1, y1) and the width (w) and height (h) of the 
        # bounding rectangle. This rectangle is the smallest box that completely encloses the contour

        cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)
