import cv2

def capture_image():
	camera = cv2.VideoCapture(0)
	return_value, image = camera.read()
	cv2.imwrite('capture_img'+'.png', image)
	del(camera)

capture_image()

