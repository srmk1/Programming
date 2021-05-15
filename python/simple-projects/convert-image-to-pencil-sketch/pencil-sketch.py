from google.colab.patches import cv2_imshow
import cv2 

#Step 1: Loading the image
img = cv2.imread('/Users/srmk/Desktop/aditi/parvati.jpg')

#Step 2: Converting an image into gray_scale image
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Step 3: Invert the image
img_invert = cv2.bitwise_not(img_gray)
#cv2.imwrite('/Users/srmk/Desktop/aditi/parvati.png', img_invert)

#Step 4: Smoothing the image 
img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
#cv2_imshow(img_smoothing)

#Step5: Write image back to png
cv2.imwrite('/Users/srmk/Desktop/aditi/parvati.png', img_smoothing)
