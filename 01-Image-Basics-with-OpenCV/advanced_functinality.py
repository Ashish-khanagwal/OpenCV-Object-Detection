import cv2
import numpy as np
import matplotlib.pyplot as plt

###############
## VARIABLES ##
###############

# True while Mouse button down, False while Mouse button up

Drawing = False
ix, iy = -1, -1

##############
## FUNCTION ##
##############

def draw_rectangle(event,x,y,flgas,param):
    global Drawing, ix, iy
    
    if event == cv2.EVENT_LBUTTONDOWN:
        Drawing = True
        ix, iy = x, y
    
    elif event == cv2.EVENT_MOUSEMOVE:
        if Drawing == True:
            cv2.rectangle(img, (ix, iy), (x, y), (255,255,0), -1)
    
    elif event == cv2.EVENT_LBUTTONUP:
        Drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (255,255,0), -1)        

#######################
## SHOWING THE IMAGE ##
#######################

img = np.zeros((512,512,3))

cv2.namedWindow(winname = 'my_drawing')
cv2.setMouseCallback('my_drawing', draw_rectangle)

while True:
    
    cv2.imshow('my_drawing', img)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()