
# coding: utf-8

# 2D Convolution ( Image Filtering )
# 
# As in one-dimensional signals, images also can be filtered with various low-pass filters(LPF), high-pass filters(HPF) etc. LPF helps in removing noises, blurring the images etc. HPF filters helps in finding edges in the images.
# 

# In[1]:


import cv2
import numpy as np
from matplotlib import pyplot as plt


# In[2]:


image = cv2.imread('data/logo.jpg')
plt.imshow(image),plt.title('Original')
plt.show()


# AVERAGE FILTER

# In[3]:


# 5X5 ones matrix and divide them with 25 (5X5)
kernel = np.ones((5,5),np.float32)/25
output1 = cv2.filter2D(image,-1,kernel) #Apply kernel as filter using Convolution (Convolution is the most important topic in signal processing)

#prevent GUI Crash
cv2.startWindowThread()
#Step 3:- Display an image to the User
cv2.imshow("Averaging",output1)
#Step 4:- Capture anystroke from the user
cv2.waitKey(0)
#Step 5:- Destroy all the previously created instances
cv2.destroyAllWindows()


# 1) AVERAGE FILTER WITHOUT KERNEL AND CONVOLUTION ( directly using cv2.blur() )

# In[5]:


blur = cv2.blur(image,(5,5)) #apply simplest average filter (blur filter) using 5X5 kernel matrix 
#prevent GUI Crash
cv2.startWindowThread()
#Step 3:- Display an image to the User
cv2.imshow("BLUR",blur)
#Step 4:- Capture anystroke from the user
cv2.waitKey(0)
#Step 5:- Destroy all the previously created instances
cv2.destroyAllWindows()


# 2) GAUSSIAN BLURRING
# 
# In this, instead of box filter, gaussian kernel is used. It is done with the function, cv2.GaussianBlur(). We should specify the width and height of kernel which should be positive and odd. We also should specify the standard deviation in X and Y direction, sigmaX and sigmaY respectively. If only sigmaX is specified, sigmaY is taken as same as sigmaX. If both are given as zeros, they are calculated from kernel size. Gaussian blurring is highly effective in removing gaussian noise from the image.
# 
# If you want, you can create a Gaussian kernel with the function, cv2.getGaussianKernel().

# In[7]:


#Applying Gaussian Blur Filter for removing Gaussian Noise
gaussianBlur = cv2.GaussianBlur(image,(5,5),0)
#prevent GUI Crash
cv2.startWindowThread()
#Step 3:- Display an image to the User
cv2.imshow("Gaussian Blur",gaussianBlur)
#Step 4:- Capture anystroke from the user
cv2.waitKey(0)
#Step 5:- Destroy all the previously created instances
cv2.destroyAllWindows()


# 3) MEDIAN BLURRING
# 
# 
# Here, the function cv2.medianBlur() takes median of all the pixels under kernel area and central element is replaced with this median value. This is highly effective against salt-and-pepper noise in the images. Interesting thing is that, in the above filters, central element is a newly calculated value which may be a pixel value in the image or a new value. But in median blurring, central element is always replaced by some pixel value in the image. It reduces the noise effectively. Its kernel size should be a positive odd integer.
# 
# In this demo, I added a 50% noise to our original image and applied median blur.

# In[8]:


salt_pepper_noised_image = cv2.imread('data/sp_noised.jpg')
median = cv2.medianBlur(salt_pepper_noised_image,5) #Remove salt and pepper noise with median filter


#prevent GUI Crash
cv2.startWindowThread()
#Step 3:- Display an image to the User
cv2.imshow("Noised Image",salt_pepper_noised_image)
cv2.imshow("Median Blur",median)
#Step 4:- Capture anystroke from the user
cv2.waitKey(0)
#Step 5:- Destroy all the previously created instances
cv2.destroyAllWindows()


# 4) BILATERAL FILTERING
# 
# 
# cv2.bilateralFilter() is highly effective in noise removal while keeping edges sharp. But the operation is slower compared to other filters. We already saw that gaussian filter takes the a neighbourhood around the pixel and find its gaussian weighted average. This gaussian filter is a function of space alone, that is, nearby pixels are considered while filtering. It doesn't consider whether pixels have almost same intensity. It doesn't consider whether pixel is an edge pixel or not. So it blurs the edges also, which we don't want to do.
# 
# Bilateral filter also takes a gaussian filter in space, but one more gaussian filter which is a function of pixel difference. Gaussian function of space make sure only nearby pixels are considered for blurring while gaussian function of intensity difference make sure only those pixels with similar intensity to central pixel is considered for blurring. So it preserves the edges since pixels at edges will have large intensity variation.

# In[9]:


bilateral = cv2.bilateralFilter(image,9,75,75) #Bilateral filtering for smoothing and keeping sharp edges

#prevent GUI Crash
cv2.startWindowThread()
#Step 3:- Display an image to the User
cv2.imshow("Median Blur",bilateral)
#Step 4:- Capture anystroke from the user
cv2.waitKey(0)
#Step 5:- Destroy all the previously created instances
cv2.destroyAllWindows()


# More details about bilateral filter , http://people.csail.mit.edu/sparis/bf_course/

# Source : https://docs.opencv.org/3.1.0/d4/d13/tutorial_py_filtering.html
