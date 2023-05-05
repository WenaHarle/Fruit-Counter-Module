import cv2



# Create the video capture object and set the frame size
cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(2)
cap3 = cv2.VideoCapture(4)

# Create the video writer object with a compatible MP4 codec
frame_size = (640, 480)
codec = cv2.VideoWriter_fourcc(*'mp4v')
fps = 30

Atas = cv2.VideoWriter('Depan.mp4', codec, fps, frame_size)
Kanan = cv2.VideoWriter('Kanan.mp4', codec, fps, frame_size)
Kiri  = cv2.VideoWriter('Kiri.mp4', codec, fps, frame_size)

# Start the video capture and writing loop
while True:
    ret, frame = cap.read()
    ret2, frame2 = cap2.read()
    ret3, frame3 = cap3.read()
    
    # checking the capture menthod is succesfull
    if ret AND ret2 AND ret3:

        Atas.write(frame)
        Kanan.write(frame2)
        Kiri.write(frame3)
        
        cv2.imshow('Atas', frame)
        cv2.imshow('Kanan', frame2)
        cv2.imshow('Kiri', frame3)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture and writer, and close the window
cap.release()
Depan.release()
cv2.destroyAllWindows()
