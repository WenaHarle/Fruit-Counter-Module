import cv2
#import base64
import math
#import requests



#create subtraction image
def sub(cap, bright):
    cap.set(cv2.CAP_PROP_BRIGHTNESS, bright)
    _, frameA = cap.read()
    abupertama = cv2.cvtColor(frameA, cv2.COLOR_BGR2GRAY)
    abupertama = cv2.GaussianBlur(abupertama, (5, 5), 0)
    return abupertama, frameA

#substrack the video and get contour
def backsub(cap,abupertama,bright):
    cap.set(cv2.CAP_PROP_BRIGHTNESS, bright)
    _, img = cap.read() #used for image thtat send to DB
    _, frame = cap.read()
    frameabu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameabu = cv2.GaussianBlur(frameabu, (5, 5), 0)
    difference = cv2.absdiff(abupertama, frameabu)
    _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)
    _, contours, _ = cv2.findContours(difference, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return contours, difference, frame, img

#create rectangle around the fruit & dinf the middle point
def rect(cnt,frame,detections, midnow):
    area = cv2.contourArea(cnt)
    if area > 6000 and area < 11000:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 225), 3)
        detections.append([x, y, w, h])
        cv2.putText(frame, str(w * h), (x, y + h), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        cx = int((x + x + w) / 2)
        cy = int((y + y + h) / 2)
        midnow.append((cx, cy, w, h))
        cv2.circle(frame, (cx, cy), 5, (0, 0, 225), -1)

    return frame, midnow

#create object tracker and take picture of the fruits
def obtrack(count, midnow, midold, trackob, track_id, frame, cid, buah, frameA, img, output_file):
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

        if (object_id not in cid and 318<pt[0] and pt[0]<323):
            cid.append(object_id)
            buah +=1
            size = pt[2]*pt[3]

            y1 = pt[1]-(pt[3]/2)+35
            y2 = pt[1]+(pt[3]/2)+45
            x1 = pt[0]-(pt[2]/2)+55
            x2 = pt[0]+(pt[2]/2)+65
            y1 = int(y1)
            y2 = int(y2)
            x1 = int(x1)
            x2 = int(x2)
            print(y1,y2,x1,x2)
            region = img[y1: y2, x1: x2]
            subreg = frameA[y1: y2, x1: x2]

            meme = cv2.absdiff(region, subreg)
            cv2.imwrite(output_file, meme)

            #with open('image.jpg', 'rb') as f:
                #image_data = f.read()
            #images = base64.b64encode(image_data).decode('utf-8')
            #data = {'size': size, 'image': images}
            #response = requests.post(url, data=data)


        if (pt[0]==61 and buah%3==0):
            cid.pop(0)

    return frame, midnow, trackob, track_id, cid, buah