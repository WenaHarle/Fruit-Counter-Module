import cv2
import Backsub as bs

#Variabel camera atas
cap = cv2.VideoCapture(0)
bright = 0.3
abupertama, frameA = bs.sub(cap,bright)
buah = 0
count = 0
midold = []
cid = [-1]
trackob = {}
track_id = 0
output_file = "output_atas.jpg"

#Variabel camera Kanan
cap2 = cv2.VideoCapture(2)
bright2 = 0.3 
abupertama2, frameA2 = bs.sub(cap2,bright2)
buah2 = 0
count2 = 0
midold2 = []
cid2 = [-1]
trackob2 = {}
track_id2 = 0
output_file2 = "output_Kanan.jpg"

#Variabel kamera kiri
cap3 = cv2.VideoCapture(4)
bright3 = 0.3
abupertama3, frameA3 = bs.sub(cap3,bright3)
buah3 = 0
count3 = 0
midold3 = []
cid3 = [-1]
trackob3 = {}
track_id3 = 0
output_file3 = "output_kiri.jpg"

#url = 'http://localhost/sending/sender.php'


while True:
    #variabel camera atas
    count += 1
    detections = []
    midnow = []
    
    #variabel camera Kanan
    count2 += 1
    detections2 = []
    midnow2 = []
    
     #variabel camera kiri
    count3 += 1
    detections3 = []
    midnow3 = []


    #camera atas
    contours, difference, frame, img = bs.backsub(cap, abupertama,bright)
    cv2.line(frame, (320, 0), (320, 480), (60, 35, 176), 2)

    #camera kanan
    contours2, difference2, frame2, img2 = bs.backsub(cap2, abupertama2,bright2)
    cv2.line(frame2, (320, 0), (320, 480), (60, 35, 176), 2)
    
    #camera kiri
    contours3, difference3, frame3, img3 = bs.backsub(cap3, abupertama3,bright3)
    cv2.line(frame3, (320, 0), (320, 480), (60, 35, 176), 2)
    
    
    # menemukan kontur dan membuat persegi Kamera atas
    for cnt in contours:
        frame, midnow = bs.rect(cnt, frame, detections, midnow)
    
    # menemukan kontur dan membuat persegi Kamera kanan
    for cnt2 in contours2:
        frame2, midnow2 = bs.rect(cnt2, frame2, detections2, midnow2)
        
    # menemukan kontur dan membuat persegi Kamera Kiri
    for cnt3 in contours3:
        frame3, midnow3 = bs.rect(cnt3, frame3, detections3, midnow3)
      
    #tracking kamera atas
    frame, midnow, trackob, track_id, cid, buah= bs.obtrack(count, midnow, midold, trackob, track_id, frame, cid, buah, frameA, img, output_file)
    
    #tracking kamera Kanan
    frame2, midnow2, trackob2, track_id2, cid2, buah2= bs.obtrack(count2, midnow2, midold2, trackob2, track_id2, frame2, cid2, buah2, frameA2, img2, output_file2)
    
    #tracking kamera atas
    frame3, midnow3, trackob3, track_id3, cid3, buah3= bs.obtrack(count3, midnow3, midold3, trackob3, track_id3, frame3, cid3, buah3, frameA3, img3, output_file3)


    #Put Text pada video output
    cv2.putText(frame, str("jumlah buah : "), (30, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.putText(frame, str(buah), (270, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

    #Put Text pada video output
    cv2.putText(frame2, str("jumlah buah : "), (30, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.putText(frame2, str(buah2), (270, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

    #Put Text pada video output
    cv2.putText(frame3, str("jumlah buah : "), (30, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.putText(frame3, str(buah3), (270, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    
    midold = midnow.copy()
    midold2 = midnow2.copy()
    midold3 = midnow3.copy()


    cv2.imshow("Kamera atas", frame)
    cv2.imshow("Kamera Kanan", frame2)
    cv2.imshow("Kamera Kiri", frame3)
    
    key = cv2.waitKey(30)
    if key == ord('q'):
        break
    if key == ord('p'):
        cv2.waitKey(-1)

cap.release()
cap2.release()
cap3.release()
cv2.destroyAllWindows()
