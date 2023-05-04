#!/usr/bin/env python3
# import the opencv library
import math

import cv2
import numpy as np

f = open("test.txt","a")

f.write("Program Berjalan \n")
f.write("Semoga harimu tenang")
f.close()

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_BRIGHTNESS, 0.3)
cap.set(cv2.CAP_PROP_CONTRAST, 0.3)

_, frame1 = cap.read()
abupertama = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
abupertama = cv2.GaussianBlur(abupertama, (5, 5), 0)

buah = 0
count = 0
midold = []
cid = [-1]
trackob = {}
track_id = 0
while True:
    _, frame = cap.read()
    count += 1
    
    frameabu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameabu = cv2.GaussianBlur(frameabu, (5, 5), 0)
    difference = cv2.absdiff(abupertama, frameabu)
    _, difference = cv2.threshold(difference, 25, 225, cv2.THRESH_BINARY)
    _,contours,_ = cv2.findContours(difference, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    detections = []
    #menunjukkan fram sekarang
    midnow = []
    cv2.line(frame, (320, 0), (320, 480), (60, 35, 176), 5)
    for cnt in contours:
        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)
        if area > 6000 and area <15000 :
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 225), 3)

            detections.append([x, y, w, h])
            cv2.putText(frame, str(w*h), (x, y+h), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
            cx = int((x + x + w) / 2)
            cy = int((y + y + h) / 2)
            midnow.append((cx, cy))

            cv2.circle(frame, (cx, cy), 5, (0, 0, 225), -1)
            print("cordinat midnow")
            print(midnow)


    if count <= 2:
        for pt in midnow:
            for pt2 in midold:
                distance = math.hypot(pt2[0]-pt[0],pt2[1]-pt[1])
                if distance < 50:
                    trackob[track_id] = pt
                    track_id += 1

    else:

        trackob_copy = trackob.copy()
        midnow_copy = midnow.copy()


        for object_id, pt2 in trackob_copy.items():
            object_exists = False
            for pt in midnow_copy:
                distance = math.hypot(pt2[0] - pt[0], pt2[1] - pt[1])

                #update object position
                if distance < 50:
                    trackob[object_id] = pt
                    object_exists = True
                    if pt in midnow:
                        midnow.remove(pt)
                        continue

                #remove id
            if not object_exists:
                trackob.pop(object_id)

        for pt in midnow:
            trackob[track_id] = pt
            track_id += 1

    for object_id, pt in trackob.items():
        cv2.putText(frame, str(object_id), (pt[0], pt[1]+7), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        if (object_id not in cid and 318<pt[0] and pt[0]<325):
            cid.append(object_id)
            buah +=1

        if (pt[0]==327 and buah%3==0):
            cid.pop(0)

    cv2.putText(frame, str("jumlah buah : "), (30, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.putText(frame, str(buah), (270, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

    print("tracking obeject")
    print(trackob)
    print("cordinat box")
    print(detections)
    print("array")
    print(cid)

    midold = midnow.copy()

    cv2.imshow("Fruits Counter", frame)

    key = cv2.waitKey(30)
    if key == ord('q'):
        break
    if key == ord('p'):
        cv2.waitKey(-1)

cap.releasa()
cv2.destroyALLWindows()


    



