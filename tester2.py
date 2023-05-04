import cv2
import Backsub as bs

#Variabel camera atas
cap = cv2.VideoCapture(0)
abupertama, frameA = bs.sub(cap,0.3)
Jbuah = 0                              #Jumlah biah yang telah dihitung
count = 0                              #Penghitung frame untuk inisasi tracking
midold = []                            #Koordinat pusat dari buah frame sebelumnya
cid = [-1]                             #Untuk menyimpan ID buah yang sudah di hitung
trackob = {}                           #Array untuk menyimpan koordinat dan ID buah
track_id = 0                           #ID buah

#url = 'http://localhost/sending/sender.php'


while True:
    #variabel camera atas
    count += 1
    detections = []
    midnow = []       #menyimpan koordinat titik pusat buah pasa frame saaat ini


    contours, difference, frame, img = bs.backsub(cap, abupertama,0.3)
    cv2.line(frame, (320, 0), (320, 480), (60, 35, 176), 2)

    # menemukan kontur dan membuat persegi
    for cnt in contours:
        frame, midnow = bs.rect(cnt, frame, detections, midnow)

    output_file = "output_atas.jpg"
    frame, midnow, trackob, track_id, cid, buah= bs.obtrack(count, midnow, midold, trackob, track_id, frame, cid, buah, frameA, img, output_file )

    cv2.putText(frame, str("jumlah buah : "), (30, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.putText(frame, str(Jbuah), (270, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)


    midold = midnow.copy()


    cv2.imshow("Kamera atas", frame)

    key = cv2.waitKey(30)
    if key == ord('q'):
        break
    if key == ord('p'):
        cv2.waitKey(-1)

cap.release()
cv2.destroyAllWindows()

