# In this we will learn about Connecting callback functions

import cv2
import numpy as np
import matplotlib.pyplot as plt

##############
## FUNCTION ##
##############

# Code written below is for connecing the call back function with the OpenCV code

def draw_circle(event,x,y,flags,param):
# here, (x,y) are the mouse positions at the image. event is what mouse exactly did (right click, left click etc.)
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 100, (255, 255, 0), -1)

    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 100, (255,0,255), -1)
        
cv2.namedWindow(winname = 'my_drawing')

cv2.setMouseCallback('my_drawing', draw_circle)

###############################
## SHOWING IMAGE WITH OPENCV ##
###############################

# From below mentioned code we will create an blank image.
img = np.zeros((512,512,3), dtype = np.int8)

while True:
    
    cv2.imshow('my_drawing', img)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break 

cv2.destroyAllWindows()