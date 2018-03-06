import cv2
#only for TrackBar process
def nothing(x):
    pass
image = cv2.imread('horse.jpg')
switch = '0 : OFF \n1 : ON'
cv2.namedWindow('canny')
cv2.createTrackbar(switch, 'canny', 0, 1, nothing)
cv2.createTrackbar('lower', 'canny', 0, 255, nothing)
cv2.createTrackbar('upper', 'canny', 0, 255, nothing)
while(1):

    
    lower = cv2.getTrackbarPos('lower', 'canny')
    upper = cv2.getTrackbarPos('upper', 'canny')
    s = cv2.getTrackbarPos(switch, 'canny')

    if s == 0:
        edges = image
    else:
        edges = cv2.Canny(image, lower, upper)

    
    cv2.imshow('canny', edges)
    cv2.imwrite("canny.jpg",edges)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:   
        break
cv2.destroyAllWindows()

