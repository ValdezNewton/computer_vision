# import os
# os.environ["QT_QPA_PLATFORM"] = "xcb"
import cv2
import pyrealsense2 as rs
import numpy as np

# Configure Realsense pipeline
pipeline = rs.pipeline() # Creates a pipeline (RealSense data flow controller). It manages streaming frames from the cam
config = rs.config() # Creates a configuration obj where one specifies cam options (streams, resolution, fps, etc.

# Enable the RGB stream
config.enable_stream(rs.stream.color, 1080, 640, rs.format.bgr8, 30)  
# config.enable_stream() tells RealSense SDK which stream to enable & how to configure it
# rs.stream.color selects the "color (RGB) camera stream" option
# rs.format.bgr8 specifies Image pixel format (8-bit BGR)

# Start streaming
pipeline.start(config) # Starts the cam stream according to the config settings

# Visualize RGB Stream
while True:
    # Wait for the next frame
    frames = pipeline.wait_for_frames()

    # Get the color frame
    color_frame = frames.get_color_frame()
    
    # Convert to a NumPy array
    frame = np.asanyarray(color_frame.get_data())
    # np.asanyarray() converts the image data into a NumPy array for easier manipulation
    # color_frame.get_data() retrieves the raw image data from the color frame
    
    # Display the frame
    cv2.imshow('frame', frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Stop streaming
pipeline.stop()
cv2.destroyAllWindows()
