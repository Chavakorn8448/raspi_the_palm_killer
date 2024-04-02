import shutil
import os
import sys
import cv2
from picture import stretch_image

source_path = 'runs/detect/predict/crops/Palm'
dest_path = '/home/the-palm-killer/raspi_the_palm_killer/cropped_images'
os.makedirs(dest_path, exist_ok=True)

def move_file():
	if not os.path.exists(source_path):
		print("source path doesn't exist")
		sys.exit()
		
	for item in os.listdir(source_path):
		full_source_path = os.path.join(source_path, item)
		stretch_image(full_source_path)
		full_dest_path = os.path.join(dest_path, item)
		shutil.move(full_source_path, full_dest_path)
		
def remove_file():
	os.remove('image.jpg')
	shutil.rmtree('runs/detect/predict')
	for item in os.listdir(dest_path):
		item_path = os.path.join(dest_path, item)
		os.remove(item_path)
