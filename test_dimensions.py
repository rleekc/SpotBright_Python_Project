# import required module
import cv2
  
# get image
filepath = "C:\\Users\\newrl\\OneDrive\\Desktop\\Spotlight\\Spotlight_Pictures_01-09-2023\\eab6c342f236f06993ea8a43eeac8083d274e56153f9772a30201364d437f605.jpg"
image = cv2.imread(filepath)
#print(image.shape)
  
# get width and height
height, width = image.shape[:2]
  
# display width and height
print("The height of the image is: ", height)
print("The width of the image is: ", width)