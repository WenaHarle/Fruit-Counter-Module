import cv2

# Create the video capture object and set the frame size
cap = cv2.VideoCapture(1)

cap2 = cv2.VideoCapture(2)


# Set the capture resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

cap2.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


# Create the video writer object with a compatible MP4 codec
frame_size = (1280, 720)
codec = cv2.VideoWriter_fourcc(*'mp4v')
fps = 10

Camera1 = cv2.VideoWriter('Camera1.mp4', codec, fps, frame_size)

Camera2 = cv2.VideoWriter('Camera2.mp4', codec, fps, frame_size)



# Start the video capture and writing loop
while True:
    ret, frame = cap.read()

    ret2, frame2 = cap2.read()


    # checking the capture menthod is succesfull
    if ret  and ret2 :
        
        #Write Video File
        Camera1.write(frame)
        Camera2.write(frame2)
   
        #Show Video In Camera
        cv2.imshow('Camera1', frame)
        cv2.imshow('Camera2', frame2)



        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture and writer, and close the window
cap.release()
Camera1.release()
cap2.release()
Camera2.release()


cv2.destroyAllWindows()
