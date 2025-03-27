from ultralytics import YOLO

# Load a model
model = YOLO("yolov8s.pt")   # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="C:/Users/gonca/Bussiness-Analytics-e-Minera-o-de-Dados/datasets/Dataset01/data.yaml", epochs=100, imgsz=640)
