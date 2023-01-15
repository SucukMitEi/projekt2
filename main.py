import cv2
import numpy as np
import pyperclip
from functions import *

name = "5"

img = cv2.imread(f"images/{name}", cv2.IMREAD_UNCHANGED)
img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)

bg = [0, 0, 0]  # change this to your terminal
#                 background color to add
#                 support for transparent
#                 images

for i in chunks(img, 2):
	first_row = i[0]
	second_row = i[1]
	for i in range(len(first_row)):
		color_first = calculateBG(first_row[i], bg)
		color_second = calculateBG(second_row[i], bg)

		color_first_ansi = FG_RGB(*color_first)
		color_second_ansi = BG_RGB(*color_second)

		print(color_first_ansi + color_second_ansi + CHAR, end="")
	print("\x1b[0m")
