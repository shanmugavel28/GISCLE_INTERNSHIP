import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('thrsh.jpg')
bilateral = cv2.bilateralFilter(image,9,75,75) #Bilateral filtering for smoothing and keeping sharp edges

#prevent GUI Crash
cv2.startWindowThread()
#Step 3:- Display an image to the User
cv2.imshow("Mbilateral",bilateral)
cv2.imwrite("image.png",bilateral)
#Step 4:- Capture anystroke from the user
cv2.waitKey(0)
#Step 5:- Destroy all the previously created instances
cv2.destroyAllWindows()
