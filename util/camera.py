import re
import cv2
import numpy as np
from datetime import datetime

def capture_one():
    """
    capture is used to capture pictures
    """
    capture = cv2.VideoCapture(0)
    while(capture.isOpened()):
        ret, image = capture.read()
        if ret is not True:
            print("can not open camera")
            break
        cv2.imshow("capture", image)
        key = cv2.waitKey(20) & 0xff
        if  key == ord('q') or key == ord('Q') :
            break
    print('cap.isOpened():',capture.isOpened())
    capture.release()
    print('cap.isOpened():',capture.isOpened())

def video():
    """
    video is used to open a camera window and capture frames
    """
    capture = cv2.VideoCapture(0)
    while(True):
        ret, frame = capture.read()
        frame = cv2.flip(frame, 1)
        cv2.imshow("video", frame)
        c = cv2.waitKey(50)
        if c == 27:
            break