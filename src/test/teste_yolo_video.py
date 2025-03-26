from ultralytics import YOLO
import cv2

# Carregar o modelo treinado (ajuste o caminho se necessário)
model = YOLO("best.pt")  # Certifique-se de que este caminho está correto

# Abrir a webcam (0 = webcam padrão, tente 1 ou 2 se tiver múltiplas câmeras)
cap = cv2.VideoCapture(0)

# Definir tamanho do vídeo (opcional)
cap.set(3, 640)  # Largura
cap.set(4, 480)  # Altura

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Fazer inferência na imagem da webcam
    results = model(frame)

    # Renderizar os resultados no frame
    annotated_frame = results[0].plot()

    # Mostrar a saída
    cv2.imshow("Detecção em tempo real - YOLOv8", annotated_frame)

    # Pressione 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
