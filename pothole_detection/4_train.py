from ultralytics import YOLO

# Load a model
model = YOLO("yolov8s.pt") 

# Train the model
results = model.train(
	data = "data.yaml",
	imgsz = 640,
	#epochs = 100,
	epochs = 10,
	#batch = -1
	plots = True
)

