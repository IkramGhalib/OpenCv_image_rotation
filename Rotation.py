import cv2
import argparse
import imutils


ap=argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="adrian.png",
                help="Path to input image")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
cv2.imshow("Original",image)

(h,w)=image.shape[:2]
(cX,cY)=(w//2, h//2)

# Get dimension and roatate by 45 degree and scale

M =  cv2.getRotationMatrix2D((cX, cY),45,1.0)
rotated = cv2.warpAffine(image, M,(w,h))
cv2.imshow("Rotated by 45 Degree",rotated)

M= cv2.getRotationMatrix2D((cX, cY), -90, 2.0)
rotated = cv2.warpAffine(image,M, (w,h))
cv2.imshow("90 degree Rotated", rotated)

M = imutils.rotate(image,45)
cv2.imshow("Imutils 180 degree", M)

# without croping image rotate
rotated = imutils.rotate_bound(image, 45)
cv2.imshow("Withou cropping image 45", rotated)
cv2.waitKey(0)