# Create a script that opens the picture and allows you to draw empty red circles whever you click the RIGHT MOUSE BUTTON DOWN.

import cv2
import numpy as np
import matplotlib.pyplot as plt

def draw_circle(event,x,y,flags,param):
    
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 50, (0,0,255), 5)

img = cv2.imread('../Computer-Vision-with-Python/DATA/dog_backpack.jpg')
# fix_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.namedWindow(winname = 'my_img')
cv2.setMouseCallback('my_img', draw_circle)

while True:
    cv2.imshow('my_img', img)
        
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()