import cv2

cap = cv2.VideoCapture(0) 

if not cap.isOpened():
    print("ERROR: Cannot open camera!")
else:
    print("Camera is working.")

cap.release()
