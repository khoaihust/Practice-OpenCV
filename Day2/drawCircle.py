import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype = 'uint8') # 500 rows, 700 columns
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2) # centerX, center Y is x, y coordinate 
white = (255, 255, 255)

for r in range(0, 175, 25):
	cv2.circle(canvas, (centerX, centerY), r, white)

cv2.imshow('circle', canvas)

for i in range(0, 25):
	radius = np.random.randint(5, high = 200)
	color = np.random.randint(0, high = 256, size = (3,)).tolist() # list  color 3-dimensional
	pt = np.random.randint(0, high = 300, size = (2,)) 
	cv2.circle(canvas, tuple(pt), radius, color, -1)
cv2.imshow('many circle', canvas)

cv2.waitKey(0)
