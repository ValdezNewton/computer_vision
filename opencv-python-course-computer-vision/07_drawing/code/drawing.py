import os

import cv2


img = cv2.imread(os.path.join('.', 'whiteboard.png'))

print(img.shape)

# line
cv2.line(img, (100, 150), (300, 450), (0, 255, 0), 3) # cv2.line(image, start_point, end_point, color, thickness)

# rectangle
cv2.rectangle(img, (200, 350), (450, 600), (0, 0, 255), -1) 
# cv2.rectangle(image, top_left_corner, bottom_right_corner, color, thickness) 
# Note: thickness of -1 fills the rectangle

# circle
cv2.circle(img, (800, 200), 75, (255, 0, 0), 10) # cv2.circle(image, center_coordinates, radius, color, thickness)

# text
cv2.putText(img, 'Hey you!', (600, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (150, 0, 100), 10)
# cv2.putText(image, text, org, font, fontScale, color, thickness)

cv2.imshow('img', img)
cv2.waitKey(0)
