import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, 
	              help = "Path to the image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])
#img = cv2.imread('T20.jpg')

print(type(img))
print(img.shape)
print('width: {} pixels'.format(img.shape[1]))
print('height: {} pixels'.format(img.shape[0]))
print('channels: {}'.format(img.shape[2]))

cv2.imshow("Tham", img)
cv2.waitKey(0)

cv2.imwrite('newimage.jpg', img)
cv2.destroyAllWindows()


