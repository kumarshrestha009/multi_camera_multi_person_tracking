import numpy as np
import cv2
from PIL import Image

video_capture_0 = cv2.VideoCapture('top_view1.avi')
video_capture_1 = cv2.VideoCapture('demo1.avi')

while True:
    # Capture frame-by-frame
    ret0, frame0 = video_capture_0.read()
    ret1, frame1 = video_capture_1.read()

    image1 = Image.fromarray(frame1[..., ::-1])  # bgr to rgb

    if (ret0):
        # Display the resulting frame
        cv2.imshow('Cam 0', frame0)

    if (ret1):
        # Display the resulting frame
        cv2.imshow('Cam 1', frame1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture_0.release()
video_capture_1.release()
cv2.destroyAllWindows()