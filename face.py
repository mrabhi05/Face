import cv2

# Loading pre-trained Data
trained_face_data = cv2.CascadeClassifier('D:\Abhi\Study Zone\Projects\Face Detector\haarcascade_frontalface_default.xml')

# Choose an image to detect faces in 
#img = cv2.imread('sop.png')

# To capture video from webcam
webcam = cv2.VideoCapture(0)

# Iterate for video 
while True:
    # Read the current frame
    successful_capture, frame = webcam.read()

# 
#cv2.imshow('Face Detectiom', frame)

#cv2.waitKey()

# Convert to Greyscale
    grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Detect Faces
    face_coordinates = trained_face_data.detectMultiScale(grayscale_img)

# Draw Rect around the face
    for (x,y,w,h) in face_coordinates:
       cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Face Detectiom', frame)
    key = cv2.waitKey(1)

    # Stop when Q is pressed
    if key==81 or key==113:
        break

#Relaease the Webcam
webcam.release()
