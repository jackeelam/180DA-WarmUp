#Detecting blue and drawing a rectangle around the the majority of blue
#Was not altered from https://answers.opencv.org/question/200861/drawing-a-rectangle-around-a-color-as-shown/

import numpy as np
import cv2  

#Parameter is device index or the name of a video file
#Device index is just the number to specify which camera
cap = cv2.VideoCapture(0)

#This is the blue that we want to look for.
# rgb 0, 51, 255. Need to reverse to bgr
bgr_blue = np.uint8([[[255, 51, 0]]])
hsv_blue = cv2.cvtColor(bgr_blue,cv2.COLOR_BGR2HSV)

print(hsv_blue[0][0][0])

while True:
    # ret is a bool. If frame read correctly, returns True
    # frame is an numpy array of arrays
    ret, frame = cap.read()
    
    # Convert BGR to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define range of blue color in HSV
    lower_blue = np.array([hsv_blue[0][0][0] - 10, 50, 50]) #np.array([100,50,50])
    upper_blue =  np.array([hsv_blue[0][0][0] + 10, 255, 255]) #np.array([130,255,255])
    
    # Threshold the HSV image to get only blue colors
    # inRange(src, lower_bound_hsv, upper_bound_hsv)
    # In OpenCV, for HSV, Hue range is [0,179], Saturation range is [0,255] and Value range is [0,255]
    mask = cv2.inRange (hsv, lower_blue, upper_blue)
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
