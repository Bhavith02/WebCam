import numpy as np
import cv2

body_classifier = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_fullbody.xml')

frame = cv2.imread('S5.png')

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

bodies = body_classifier.detectMultiScale(gray,1.2,3)

print(bodies)

for(x,y,w,h) in bodies:
    cv2.rectangle(frame,(x,y),(x+w,y+h), (0,255,255),2)

resized=cv2.resize(frame,(int(frame.shape[1]/3),int(frame.shape[0]/3)))


cv2.imshow('Humans',resized)
cv2.waitKey()
cv2.destroyAllWindows()
