import cv2
import numpy as np
salt_pepper_noised_image = cv2.imread('thrsh.jpg')
median = cv2.medianBlur(salt_pepper_noised_image,5) 
cv2.imshow("Noised Image",salt_pepper_noised_image)
cv2.imshow("Median Blur",median)
cv2.imwrite("MedianBlur.png",median)

cv2.waitKey(0)
cv2.destroyAllWindows()
