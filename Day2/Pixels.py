import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, 
	             help = "Path to the image")
args = vars(ap.parse_args())
    
img = cv2.imread(args["image"])

cv2.imshow("Original", img) 

(b, g, r) = img[0, 0]
print('Pixels at (0,0) - Red: {}, Green: {}, Blue: {}'.format(r, g, b))

# OpenCV luu tru cac mau pixel theo BGR (reverse oder), nguoc voi RBG
img[0,0] = (0,0,255)
(b, g, r) = img[0,0]
print('Pixels at (0,0) - Red: {}, Green: {}, Blue: {}'.format(r, g, b))

# OpenCV doc toa do y truoc toa do x (top-left)
# y = [0; 200) , x = [0;100)
corner = img[0:200, 0:100]
cv2.imshow('Corner', corner)

img[0:200, 0:100] = (0, 255, 0)

cv2.imshow('Updated', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


