import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
from skimage.color import rgb2hsv,rgb2gray
from skimage.io import imread, imsave
from skimage.filters import threshold_otsu

def blurring(img):
    noiseless_img = cv2.fastNlMeansDenoisingColored(img,0,10,7,21) #noise removal
    return(noiseless_img)

# def check_color(bright, brightHSV, brightYCB, brightLAB):
#     bgr = [40, 158, 16]
#     thresh = 150
    
#     resultRGB = cv2.cvtColor(bright, cv2.COLOR_BGR2RGB)

#     minBGR = np.array([bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh])
#     maxBGR = np.array([bgr[0] + thresh, bgr[1] + thresh, bgr[2] + thresh])
    
#     maskBGR = cv2.inRange(bright,minBGR,maxBGR)
#     resultBGR = cv2.bitwise_and(bright, bright, mask = maskBGR)
    
#     #convert 1D array to 3D, then convert it to HSV and take the first element 
#     # this will be same as shown in the above figure [65, 229, 158]
#     hsv = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2HSV)[0][0]
    
#     minHSV = np.array([hsv[0] - thresh, hsv[1] - thresh, hsv[2] - thresh])
#     maxHSV = np.array([hsv[0] + thresh, hsv[1] + thresh, hsv[2] + thresh])
    
#     maskHSV = cv2.inRange(brightHSV, minHSV, maxHSV)
#     resultHSV = cv2.bitwise_and(brightHSV, brightHSV, mask = maskHSV)
    
#     #convert 1D array to 3D, then convert it to YCrCb and take the first element 
#     ycb = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2YCrCb)[0][0]
    
#     minYCB = np.array([ycb[0] - thresh, ycb[1] - thresh, ycb[2] - thresh])
#     maxYCB = np.array([ycb[0] + thresh, ycb[1] + thresh, ycb[2] + thresh])
    
#     maskYCB = cv2.inRange(brightYCB, minYCB, maxYCB)
#     resultYCB = cv2.bitwise_and(brightYCB, brightYCB, mask = maskYCB)
    
#     #convert 1D array to 3D, then convert it to LAB and take the first element 
#     lab = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2LAB)[0][0]
    
#     minLAB = np.array([lab[0] - thresh, lab[1] - thresh, lab[2] - thresh])
#     maxLAB = np.array([lab[0] + thresh, lab[1] + thresh, lab[2] + thresh])
    
#     maskLAB = cv2.inRange(brightLAB, minLAB, maxLAB)
#     resultLAB = cv2.bitwise_and(brightLAB, brightLAB, mask = maskLAB)
    
#     plt.imshow(resultRGB)
#     plt.show()
#     plt.imshow(resultBGR) #"Result BGR",
#     plt.show()  
#     plt.imshow(resultHSV) #"Result HSV", 
#     plt.show()
#     plt.imshow(resultYCB) #"Result YCB",
#     plt.show() 
#     plt.imshow(resultLAB) #"Output LAB",
#     plt.show()

def test_yellow(img):
   count = 0
   test_set = [[255,255,204],[255,255,153],[255,255,102],[255,255,51],[255,255,0],[204,204,0],[153,153,0],[102,102,0],[51,51,0]]

   for pixel in img.getdata():
      for t in test_set:
         if pixel == t:
            count += 1
   print(count)

def main():
    img = cv2.imread('leaf.JPG')
    destRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    noiseless_img = blurring(img)

   #  plt.imshow(destRGB)
   #  plt.show()
    HSVimg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    plt.imshow(HSVimg)
    plt.show()
   #  test_yellow(Image.open('yellow.jpg'))
   # check_color(noiseless_img, brightHSV, brightYCB, brightLAB)

if __name__ == '__main__':
    main()



