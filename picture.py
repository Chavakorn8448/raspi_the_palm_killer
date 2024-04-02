from picamera2 import Picamera2
import time

picam2 = Picamera2()
capture_config = picam2.create_still_configuration()

def take_picture():	
	picam2.start(show_preview=True)
	time.sleep(1)
	picam2.switch_mode_and_capture_file(capture_config, "image.jpg")
	
if __name__ == '__main__':
	take_picture()
