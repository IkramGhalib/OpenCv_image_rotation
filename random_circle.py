import numpy as np
import cv2
#
canvas = np.zeros((300, 300, 3), dtype = "uint8")

for i in range(0,3):
    radius = np.random.randint(2, high = 300)
    color = np.random.randint(0, high=300, size=(2,)).tolist()
    pt= np.random.randint(0,high=300,size=(2,))

    cv2.circle(canvas, tuple(pt),radius,color,-1)
cv2.imshow("Circle",canvas)
cv2.waitKey(0)
