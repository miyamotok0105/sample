import cv2
image = cv2.imread('objectid01/2.PNG')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('objectid01/2.PNG',gray_image)
