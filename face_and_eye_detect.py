#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 21:02:37 2019

@author: cihanerman
"""

# libraries
import cv2

# code
camera = cv2.VideoCapture(0) # 0 use for outher camera, link use for video
print("is open: ",camera.isOpened())

while True:
    ret, frame = camera.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    face_casc = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
    faces = face_casc.detectMultiScale(gray_frame,1.04,4)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h),(255, 0, 0),2)
    cv2.imshow("frame",frame)
    
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()