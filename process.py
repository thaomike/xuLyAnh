import sys 

import cv2
import numpy as np
def xamhoa(key):
     img = cv2.imread(key,0)
     
     keyArr = key.split('\\')

     keyArr[1] = 'xam' + keyArr[1]; 
     save = keyArr[0] + '\\' + keyArr[1]
     cv2.imwrite(save,img);
     return;
def tachbien(key):
     img = cv2.imread(key,0)
     img2= cv2.Canny(img,100,200)
     # cv2.imwrite(key,img2);

     keyArr = key.split('\\')
     keyArr[1] = 'bien' + keyArr[1];     
     key = keyArr[0]+'\\' + keyArr[1];
     cv2.imwrite(key,img2)
     # cv2.imshow(key,img2)
     # cv2.imshow(key,img)
     # cv2.waitKey(0)
     # cv2.destroyAllWindows()
     return;
def tachvatthe(a,b,c,key):
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


print(sys.argv[1]);

cmp= int(sys.argv[2]);

if cmp == 1:
    xamhoa(sys.argv[1])
    tachbien(sys.argv[1])
    catanh(sys.argv[1])
if cmp == 2:
     a= int(sys.argv[3])
     b= int(sys.argv[4])
     c= int(sys.argv[5])
     key=sys.argv[1]
     tachvatthe(a,b,c,key)
if cmp==3:
     key=sys.argv[1]
     a = int(sys.argv[3])
     xoayanh(key,a)
