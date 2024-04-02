from picture import take_picture
from detect import detect_image
from manage_file import move_file, remove_file

def main():
	#take_picture()
	detect_image()
	move_file()
	
if __name__ == '__main__':
	main()
