import cv2
import numpy as np
count = 0

def first(cap, bright):
    cap.set(cv2.CAP_PROP_BRIGHTNESS, bright)
    ret, frameA = cap.read()
    abupertama = cv2.cvtColor(frameA, cv2.COLOR_BGR2GRAY)
    abupertama = cv2.GaussianBlur(abupertama, (5, 5), 0)
    return abupertama, frameA

def backsub(cap,abupertama,bright):
    cap.set(cv2.CAP_PROP_BRIGHTNESS, bright)
    ret, frame = cap.read()
    frameabu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameabu = cv2.GaussianBlur(frameabu, (5, 5), 0)
    difference = cv2.absdiff(abupertama, frameabu)
    ret, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)
    ret, contours, hierarchy = cv2.findContours(difference, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return contours, difference, frame

def kotak(cnt,frame,count):
    area = cv2.contourArea(cnt)
    if area > 1000:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (225, 0, 0), 2)
        cv2.putText(frame, str(w * h), (x, y + h), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        cx = int((x + x + w) / 2)
        cy = int((y + y + h) / 2)
        cv2.circle(frame, (cx, cy), 5, (0, 0, 225), -1)
        if cx == 320:
            count += 1
    return frame, count

