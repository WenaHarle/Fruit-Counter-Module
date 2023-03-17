import cv2
import numpy as np
import Backsub

cap = cv2.VideoCapture(0)
abupertama ,frameA= Backsub.first(cap, 0.2)
count = 0
while True:
    contours, difference, frame = Backsub.backsub(cap, abupertama, 0.2)
    cv2.line(frame, (320, 0), (320, 480), (60, 35, 176), 2)
    for cnt in contours:
        frame, count = Backsub.kotak(cnt, frame, count)
    cv2.imshow("backsub", frame)
    cv2.imshow("perbedaan", difference)
    cv2.imshow("pensubstract", frameA)
    print (count)
    key = cv2.waitKey(30)
    if key == 27:
        break


result.release()
cap.release()

cv2.destroyAllWindows()
    
