from picamera2 import Picamera2
import time
import cv2
import numpy as np

picam2 = Picamera2()
capture_config = picam2.create_still_configuration()

def take_picture():	
	picam2.start(show_preview=True)
	time.sleep(1)
	picam2.switch_mode_and_capture_file(capture_config, "image.jpg")
	
def stretch_image(image_path):
    img = cv2.imread(image_path)
    resized_img = cv2.resize(img, (1280, 1280))

    height, width, _ = resized_img.shape
    max_size = max(height, width)
    square_canvas = np.zeros((max_size, max_size, 3), dtype=np.uint8)

    y_offset = (max_size - height) // 2
    x_offset = (max_size - width) // 2

    square_canvas[y_offset:y_offset+height, x_offset:x_offset+width] = resized_img

    cv2.imwrite(image_path, square_canvas)
