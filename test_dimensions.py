# import required module
import cv2
  
# get image
filepath = "C:\\Users\\newrl\\OneDrive\\Desktop\\Spotlight\\Spotlight_Pictures_08-12-2022\\178764b5981a2aee4c1fc7d893b8a2d95269220d41eede955e9c867ff12350d5.jpg"
image = cv2.imread(filepath)
#print(image.shape)
  
# get width and height
height, width = image.shape[:2]
  
# display width and height
print("The height of the image is: ", height)
print("The width of the image is: ", width)