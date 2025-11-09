import os

import cv2


# read video
video_path = os.path.join('.', 'data', 'reading.mp4')

video = cv2.VideoCapture(video_path)



# visualize video

ret = True
while ret:
    ret, frame = video.read()

    if ret:
        frame_resized = cv2.resize(frame, (540, 960))  # Resize 
        cv2.imshow('frame_resized', frame_resized)
        cv2.waitKey(40)
    # if ret is False, frame = None

video.release()
cv2.destroyAllWindows() # closes all OpenCV windows that were opened during the execution of the script.
# video.release() releases the resources that were stored for VideoCapture object

# ret, frame = video.read() 
# ret value updates each time we read a frame from the video
# if ret is False, the video comes to an end & no more frames to read