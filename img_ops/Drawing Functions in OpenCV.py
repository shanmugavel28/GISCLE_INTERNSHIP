#multiple figures in a diagram
import cv2
img=cv2.imread("img_1.jpg",1)
#line
line=cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2.imshow("Display",line)
cv2.imwrite("LINEONIMAGE.jpg",line)
#rectangle
rect=cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv2.imshow("RECTANGLe",rect)
cv2.imwrite("RECTONIMAGE.jpg",rect)
#CIRCLE
circle=cv2.circle(img,(447,63), 63, (0,0,255), 2) 
cv2.imshow("CIRCLe",circle)
cv2.imwrite("CIRCLEONIMAGE.jpg",circle)
#ellipse
el=cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1) 
cv2.imshow("ELLIPSE",el)
cv2.imwrite("ELLIPSEONIMAGE.jpg",el)
#TEXT
font = cv2.FONT_HERSHEY_SIMPLEX
txt=cv2.putText(img,'OpenCV',(20,500), font, 4,(201,220,220),8,cv2.LINE_AA)#cv2.LINE_AA is for anti-aliasing.It is optional
#Step 4:- Display the image
cv2.imshow("TEXT",txt)
#STEP 5:- Save Image
cv2.imwrite("TEXTONIMAGE.jpg",txt)
cv2.waitKey(0)
cv2.destroyAllWindows()







