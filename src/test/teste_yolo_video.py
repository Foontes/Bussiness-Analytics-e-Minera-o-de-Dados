from ultralytics import YOLO
import cv2

model = YOLO("../../runs/detect/train8/weights/best.pt") 

cap = cv2.VideoCapture(0)


cap.set(3, 640)
cap.set(4, 480)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow("Detecção em tempo real - YOLOv8", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
