import os

import cv2


# read image
image_path = os.path.join('.', 'data', 'dog.jpg') # '.' means that data folder is in the current directory

img = cv2.imread(image_path)

# write image (using absolute path)

cv2.imwrite(os.path.join('/home/isaac/cv/opencv-python-course-computer-vision/01_io/code/data', 'dog_out.jpg'), img)

# visualize image

cv2.imshow('image', img) 
# cv2.imshow('dog image', img) 
cv2.waitKey(0) # the arugment is the duration (ms) to display the image, 0 means infinite

# cv2.imshow() displays an image in a window, the argument 'image' is the window name, 
# img is the image to be displayed, it is NumPy array, which contains the pixel data of the image

# cv2.waitKey(0) waits for a key press in the window that was opened by cv2.imshow(), 
# '0' means wait indefinitely until a key is pressed
cv2.destroyAllWindows()