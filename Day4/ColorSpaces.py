# Convert to Color
# Chuyen doi khong gian mau

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required = True, help = 'Path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('original', image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('GRAY', gray)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)

lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow('LAB', lab)

cv2.waitKey(0)
