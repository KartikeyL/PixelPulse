import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg')
img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
high=img1 - (cv2.GaussianBlur(img,(21,21),4)+64)
f,a=plt.subplots(1,2,figsize=(15,9))
a[0].imshow(img1)
a[0].axis("off")
a[0].set_title("orginal")
a[1].imshow(high)
a[1].axis("off")
a[1].set_title("using high pass filtering")


plt.show()