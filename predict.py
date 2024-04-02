from ultralytics import YOLO

model = YOLO('yolov8n.pt')
model = YOLO('best.pt')

result = model('image.jpg', save=True)
#print(result)
#result.save(filename='result.jpg')
