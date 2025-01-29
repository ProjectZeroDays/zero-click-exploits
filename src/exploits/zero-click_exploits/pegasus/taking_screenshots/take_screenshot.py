# Python program to take
# screenshots

import numpy as np
import cv2
import pyautogui

def capture_screen():

	# take screenshot using pyautogui
	image = pyautogui.screenshot()

	# since the pyautogui takes as a
	# PIL(pillow) and in RGB we need to
	# convert it to numpy array and BGR
	# so we can write it to the disk
	image = cv2.cvtColor(np.array(image),
						cv2.COLOR_RGB2BGR)

	# writing it to the disk using opencv
	cv2.imwrite("screenshot.png", image)

capture_screen()
