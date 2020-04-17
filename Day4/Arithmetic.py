import numpy as np
import argparse 
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required = True, help = 'Path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('original', image)

# OpenCV chi luu cac gia tri trong doan [0, 255]
print('max of 255: {}'.format(cv2.add(np.uint8([200]), np.uint8([100])))) 
print('min of 0: {}'.format(cv2.add(np.uint8([50]), np.uint8([100])))) 
print('wrap around: {}'.format(np.uint8([200]) + np.uint8([100])))
print('wrap around: {}'.format(np.uint8([50]) - np.uint8([100])))

M =np.ones(image.shape, dtype = 'uint8')*100
added = cv2.add(image, M)
cv2.imshow('Added', added)

M = np.ones(image.shape, dtype = 'uint8')*50
subtracted = cv2.subtract(image, M)
cv2.imshow('Subtracted', subtracted)
print(image.shape)
print(M.shape)

cv2.waitKey(0)
