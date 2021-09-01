import cv2

image = cv2.imread("minions.webp")
cv2.imshow("minion", image)
cv2.waitKey(0)

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("New Minion",gray_image)
cv2.waitKey(0)

inverted_Image = 255 - gray_image
cv2.imshow("Inverted",inverted_Image)
cv2.waitKey 

blurr = cv2.GaussianBlur(inverted_Image,(21,21),0)
cv2.imshow("blur image",blurr)
cv2.waitKey(0)

inverted_blur = 255 - blurr
pencil_sketch = cv2.divide(gray_image,inverted_blur,scale = 256.0)
cv2.imshow("sketch",pencil_sketch)
cv2.waitKey(0)

cv2.imshow("original image",image)
cv2.imshow("Pencil Sketch",pencil_sketch)
cv2.waitKey(0)