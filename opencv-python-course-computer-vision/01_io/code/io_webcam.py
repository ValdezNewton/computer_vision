import cv2

# read webcam
webcam = cv2.VideoCapture(4) # 0 is usually the default webcam, change to 1, 2, etc. if multiple webcams are connected
# realsense cam: 2 for points, 4 for color

# visualize webcam

while True:
    ret, frame = webcam.read()

    cv2.imshow('frame', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'): # Press 'q' key to exit
        break

webcam.release()
cv2.destroyAllWindows()
