import cv2
from google.colab.patches import cv2_imshow
image = cv2.imread("1.jpg")
#cv2_imshow(image)
edged = cv2.Canny(image, 10, 250)
#cv2_imshow(edged)
cv2.waitKey(0)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
#cv2_imshow(closed)
cv2.waitKey(0)
(_, cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for c in cnts:
  peri = cv2.arcLength(c, True)
  approx = cv2.approxPolyDP(c, 0.02 * peri, True)
  cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)
#cv2_imshow(image)
cv2.imwrite('part1.jpg',image)
cv2.waitKey(0)
image = cv2.imread("part1.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(image, 10, 250)
(_, cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
idx = 0
for c in cnts:
	x,y,w,h = cv2.boundingRect(c)
	if w>300 and h>300:
		idx+=1
		new_img=image[y:y+h,x:x+w]
		cv2.imwrite(str(idx) + '.png', new_img)
#cv2_imshow(image)
cv2.waitKey(0)
from PIL import Image
im = Image.open('1.png')
width, height = im.size
print(height,"pixels")