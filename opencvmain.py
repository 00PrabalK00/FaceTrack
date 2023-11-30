import cv2
import serial
import numpy as np

ser = serial.Serial('COM4', 9600, timeout=1)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        forehead_x = x + w // 2
        forehead_y = y
        forehead_width = w // 8
        forehead_height = h // 8
        cv2.rectangle(frame, (forehead_x, forehead_y), (forehead_x + forehead_width, forehead_y + forehead_height), (0, 255, 0), 2)
        data = f"{forehead_y},{forehead_x}\n"
        ser.write(data.encode())

    cv2.imshow('Face Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
ser.close()
