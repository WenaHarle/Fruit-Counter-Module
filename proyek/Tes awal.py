import cv2
import numpy as np
import Backsub

cap = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)
abupertama, frameA = Backsub.first(cap)
abupertama1, frameA1 = Backsub.first(cap1)
count = 0
count1 = 0
while True:
    contours, difference, frame = Backsub.backsub(cap, abupertama)
    cv2.line(frame, (320, 0), (320, 480), (60, 35, 176), 2)
    contours1, difference1, frame1 = Backsub.backsub(cap1, abupertama1)
    cv2.line(frame1, (320, 0), (320, 480), (60, 35, 176), 2)
    # menemukan kontur dan membuat persegi
    for cnt in contours:
        frame, count = Backsub.kotak(cnt, frame, count)
    for cnt1 in contours1:
        frame1, count1 = Backsub.kotak(cnt1, frame1, count1)

    cv2.putText(frame, str("jumlah buah : "), (30, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.putText(frame, str(count), (270, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.putText(frame1, str("jumlah buah : "), (30, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.putText(frame1, str(count1), (270, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    


    cv2.imshow("RaspiCam", frame)
    cv2.imshow("Webcam", frame1)

    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cap1.release()
cv2.destroyAllWindows()