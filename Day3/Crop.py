import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required = True, help = 'Path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'], 0)
cv2.imshow('original', image)

a = image.shape[1]//2
b = image.shape[0]//2

cropped = image[a-25:a+25, b-30:b+30]
cv2.imshow('Cropped', cropped)

cv2.waitKey(0)
