#Derived from https://answers.opencv.org/question/200861/drawing-a-rectangle-around-a-color-as-shown/
#Changed from HSV to BGR instead.

import numpy as np
import cv2  

#Parameter is device index or the name of a video file
#Device index is just the number to specify which camera
cap = cv2.VideoCapture(0)

#This is the blue that we want to look for.
# rgb 0, 51, 255. Need to reverse to bgr
bgr_blue = np.array([255, 51, 0], dtype="uint8")
lower_blue_bgr = np.array([133, 39, 5], dtype="uint8")
upper_blue_bgr = np.array([237, 145, 111], dtype="uint8")

while True:
    # ret is a bool. If frame read correctly, returns True
    # frame is an numpy array of arrays
    ret, fr = cap.read()
    
    cv2.imwrite("image.jpg", fr)
    frame = cv2.imread("image.jpg")
    
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange (frame, lower_blue_bgr, upper_blue_bgr)
    bluecnts = cv2.findContours(mask.copy(),
                              cv2.RETR_EXTERNAL,
                              cv2.CHAIN_APPROX_SIMPLE)[-2]
    # For bounding box
    if len(bluecnts)>0:
        blue_area = max(bluecnts, key=cv2.contourArea)
        (xg,yg,wg,hg) = cv2.boundingRect(blue_area)
        cv2.rectangle(frame,(xg,yg),(xg+wg, yg+hg),(0,255,0),2)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)

    k = cv2.waitKey(5) 
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
