# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:04:23 2019

@author: ACER
 """

import cv2
image = cv2.imread("C:/Users/ACER/Desktop/python/Open_CV/p1.jpg", 1)

resize = cv2.resize(image , (int(image.shape[1]/2), int(image.shape[0]/2)))



print(resize)
print(resize.shape)


face_cascade = cv2.CascadeClassifier("C:\\Users\\ACER\\Desktop\\python\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml")
gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img , scaleFactor = 1.05 , minNeighbors=5)
print(type(faces))
print(faces)

for x,y,w,h in faces:
    image = cv2.rectangle(image , (x,y), (x+w, y+h), (0,255,0),3 )
cv2.imshow("Gray",image)
cv2.waitKey(0)
