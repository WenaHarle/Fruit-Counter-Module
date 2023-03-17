import cv2
import numpy as np

bright = 0.4
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_BRIGHTNESS, bright)
_, frame1 = cap.read()
abupertama = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
abupertama = cv2.GaussianBlur(abupertama, (5, 5), 0)
# Fps = 30 
# fps = cap.get(cv2.CAP_PROP_FPS)
# print(fps)
# luas frame tinggi = 480 lebar = 640
# height, width, _ = frame.shape
# print(height, width)

count = 0

while True:
    cap.set(cv2.CAP_PROP_BRIGHTNESS, bright)
    _, frame = cap.read()


    frameabu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameabu = cv2.GaussianBlur(frameabu, (5, 5), 0)
    difference = cv2.absdiff(abupertama, frameabu)
    _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)
    _, contours, hierarchy = cv2.findContours(difference, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    #detections = []
    #midnow = []
    cv2.line(frame, (320, 0), (320, 480), (60, 35, 176), 2)

    #menemukan kontur dan membuat persegi
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 14000:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (225, 0, 0), 2)

            #detections.append([x, y, w, h])
            cv2.putText(frame, str(w*h), (x, y+h), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
            cx = int((x + x + w) / 2)
            cy = int((y + y + h) / 2)
            #midnow.append((cx, cy))
            cv2.circle(frame, (cx, cy), 5, (0, 0, 225), -1)
            
            if cx == 320:
                count += 1

    cv2.putText(frame, str("jumlah buah : "), (30, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.putText(frame, str(count), (270, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

    #print("jumlah buah :", count)
    #print("cordinat midnow", midnow)


    cv2.imshow("Hail", frame)
    cv2.imshow("Background Subtraction", difference) 
    cv2.imshow("Frame Pensubstract", frame1)

    key = cv2.waitKey(30)
    if key == 27:
        break


result.release()
cap.release()

cv2.destroyAllWindows()
