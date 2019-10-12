#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 01:28:56 2019

@author: cihanerman
"""

# libraries
import cv2
import numpy as np

# code

camera = cv2.VideoCapture(1) # 0 use for outher camera, link use for video

while True:
    ret, frame = camera.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    thing = cv2.imread("kalemtras.png", 0) # = for gray scale
    w, h = thing.shape
    res = cv2.matchTemplate(gray_frame, thing, cv2.TM_CCOEFF_NORMED)
    threshold = 0.76
    loc = np.where(res > threshold)
    
    for n in zip(*loc[::-1]):
        cv2.rectangle(frame, n, (n[0] + h, n[1] + w),(0, 255, 0),2)
        cv2.putText(frame,'Kalen Tras',(n[0] + 10, n[1] + 15 ), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 2)
    cv2.imshow("frame",frame)
    
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()