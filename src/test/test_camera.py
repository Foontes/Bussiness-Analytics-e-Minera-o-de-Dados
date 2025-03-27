import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Cannot access the camera")
else:
    print("Camera is working!")
cap.release()
