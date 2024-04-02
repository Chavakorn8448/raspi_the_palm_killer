from ultralytics import YOLO

model = YOLO('best.pt')

def detect_image():
	result = model('image.jpg', save_crop=True)
