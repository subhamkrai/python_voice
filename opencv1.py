#!/usr/bin/python3

import cv2
#importing opencv module

img = cv2.imread('1.jpg', 0)   # o defines NO BGR
cv2.imshow("show",img)
cv2.waitKey(1)
cv2.destroyAllWindows()
