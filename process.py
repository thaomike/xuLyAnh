import sys 

import cv2
import numpy as np
def xamhoa(key):
     img = cv2.imread(key)
     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     keyArr = key.split('\\')

     keyArr[1] = 'xam' + keyArr[1]; 
     save = keyArr[0] + '\\' + keyArr[1]
     cv2.imwrite(save,gray);
     return;


def nhiphan(key, extra):
     img = cv2.imread(key)
     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     ret,thresh1 = cv2.threshold(gray, extra, 255, cv2.THRESH_BINARY);
     
     keyArr = key.split('\\')

     keyArr[1] = 'nhiphan' + keyArr[1]; 
     save = keyArr[0] + '\\' + keyArr[1]
     cv2.imwrite(save,thresh1);
     return;


def tachbien(key):
     img = cv2.imread(key,0)
     img2= cv2.Canny(img,100,200)

     keyArr = key.split('\\')
     keyArr[1] = 'bien' + keyArr[1];     
     key = keyArr[0]+'\\' + keyArr[1];
     cv2.imwrite(key,img2)

     return;

def tachvatthe(r,g,bb,key):
     imgg= np.uint8([[[bb,g,r]]])
     img_hsvv= cv2.cvtColor(imgg, cv2.COLOR_BGR2HSV)
     a = img_hsvv[0][0][0]
     b = img_hsvv[0][0][1]
     c = img_hsvv[0][0][2]

     a= int(a)
     b= int(b)
     c= int(c)

     img = cv2.imread(key,1)
     img_hsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
     min_hsv= np.array([a ,b, c])
     max_hsv= np.array([a+1, b, c])
     mask=cv2.inRange(img_hsv,min_hsv,max_hsv)
     final=cv2.bitwise_and(img,img,mask=mask)
     keyArr = key.split('\\')

     keyArr[1] = 'hsv' + keyArr[1]; 
     save = keyArr[0] + '\\' + keyArr[1]
     cv2.imwrite(save, final)

     return;
def catanh(key):
     img= cv2.imread(key,1)
     roi = img[50:350, 60:360]
     keyArr = key.split('\\')

     keyArr[1] = 'cat' + keyArr[1]; 
     save = keyArr[0] + '\\' + keyArr[1]
     cv2.imwrite(save, roi)
     return;

def xoayanh(key,a):
     img = cv2.imread(key,1) 
     (h, w, d) = img.shape 
     center = (w // 2, h // 2) 
     M = cv2.getRotationMatrix2D(center, a, 1.0) 
     rotated = cv2.warpAffine(img, M, (w, h))

     keyArr = key.split('\\')

     keyArr[1] = 'xoay' + keyArr[1]; 
     save = keyArr[0] + '\\' + keyArr[1]

     cv2.imwrite(save, rotated)
     return;

def detectionface(key):
     # Load the cascade
     face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

     # Read the input image
     img = cv2.imread(key)

     # Convert into grayscale
     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

     # Detect faces
     faces = face_cascade.detectMultiScale(gray, 1.1, 4)

     # Draw rectangle around the faces
     for (x, y, w, h) in faces:
         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

     # Display the output
     keyArr = key.split('\\')

     keyArr[1] = 'detect' + keyArr[1]; 
     save = keyArr[0] + '\\' + keyArr[1]

     cv2.imwrite(save, img)
     # cv2.imshow('img', img)
     # cv2.waitKey()
     return;

def lamtron(key, select):
     img = cv2.imread(key,1)
     KERNEL_WIDTH = int(sys.argv[4]) ##kich thuoc cua so bo loc
     KERNEL_HEIGHT = int(sys.argv[5])##kich thuoc cua so bo loc
     if select == 1:
          SIGMA_X = int(sys.argv[6])
          SIGMA_Y = int(sys.argv[7])

          blur_img = cv2.GaussianBlur(img, ksize=(KERNEL_WIDTH, KERNEL_HEIGHT), sigmaX=SIGMA_X, sigmaY=SIGMA_Y)
          
          keyArr = key.split('\\')

          keyArr[1] = 'tron' + keyArr[1]; 
          save = keyArr[0] + '\\' + keyArr[1]

          cv2.imwrite(save, blur_img)
     if select == 2:
          blur_img = cv2.blur(img, ksize=(KERNEL_WIDTH, KERNEL_HEIGHT))
          keyArr = key.split('\\')

          keyArr[1] = 'tron' + keyArr[1]; 
          save = keyArr[0] + '\\' + keyArr[1]

          cv2.imwrite(save, blur_img)
     if select == 3:
          print("sdf")
          blur_img = cv2.medianBlur(img, KERNEL_WIDTH)
          keyArr = key.split('\\')

          keyArr[1] = 'tron' + keyArr[1]; 
          save = keyArr[0] + '\\' + keyArr[1]

          cv2.imwrite(save, blur_img)
     return;

print(sys.argv[1]);

cmp= int(sys.argv[2]);

if cmp == 1:
    xamhoa(sys.argv[1])
    tachbien(sys.argv[1])
    catanh(sys.argv[1])
    detectionface(sys.argv[1])
if cmp == 2:
     r= int(sys.argv[3])
     g= int(sys.argv[4])
     bb= int(sys.argv[5])
     key=sys.argv[1]
     tachvatthe(r,g,bb,key)
if cmp==3:
     key=sys.argv[1]
     a = int(sys.argv[3])
     xoayanh(key,a)
if cmp == 4:
     key=sys.argv[1]
     extra = int(sys.argv[3])
     nhiphan(key,extra)
if cmp == 5:
     key=sys.argv[1]
     select = int(sys.argv[3])
     lamtron(key,select)