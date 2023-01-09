import os
import shutil
from datetime import date
import cv2

#change C:\\User\\newrl to C:\\Users\\$your_directory
home_directory = "newrl"

#creates list of photos over 1000000 bytes
os.chdir(f"C:\\Users\\{home_directory}\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets")
listfiles = os.listdir()
print(os.listdir())
length = len(listfiles)
i = 0
photos = []
while i < length:
    if os.path.getsize(listfiles[i]) > 1000000:
        print(listfiles[i])
        photos.append(listfiles[i])
    i += 1
print(photos)

#copy photos to new folder and renames photo with jpg

today = date.today().strftime("%m-%d-%Y")
foldername = f"Spotlight_Pictures_{today}"
if not os.path.exists(f"C:\\Users\\{home_directory}\\OneDrive\\Desktop\\Spotlight"):
    os.mkdir(f"C:\\Users\\{home_directory}\\OneDrive\\Desktop\\Spotlight")
if not os.path.exists(f"C:\\Users\\{home_directory}\\OneDrive\\Desktop\\Spotlight\\{foldername}"):    
    os.mkdir(f"C:\\Users\\{home_directory}\\OneDrive\\Desktop\\Spotlight\\{foldername}")
print(foldername)
i = 0
length = len(photos)
while i < length:
    shutil.copy2(f"C:\\Users\\{home_directory}\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\{photos[i]}",f"C:\\Users\\{home_directory}\\OneDrive\\Desktop\\Spotlight\\{foldername}\\{photos[i]}.jpg")
    i += 1

#creates a folder for landscape photos
if not os.path.exists(f"C:\\Users\\{home_directory}\\OneDrive\\Desktop\\Spotlight\\_Landscape_Photos"):    
    os.mkdir(f"C:\\Users\\{home_directory}\\OneDrive\\Desktop\\Spotlight\\_Landscape_Photos")
if not os.path.exists(f"C:\\Users\\{home_directory}\\OneDrive\\Desktop\\Spotlight\\_Landscape_Photos\\_Landscape_{foldername}"):    
    os.mkdir(f"C:\\Users\\{home_directory}\\OneDrive\\Desktop\\Spotlight\\_Landscape_Photos\\_Landscape_{foldername}")

#copy only landscape photos to _Landscape_Photos
i = 0
length = len(photos)
while i < length:
    cv_filepath = f"C:\\Users\\{home_directory}\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\{photos[i]}"
    image = cv2.imread(cv_filepath)
    height, width = image.shape[:2]
    if width == 1920:
        shutil.copy2(f"C:\\Users\\{home_directory}\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\{photos[i]}",f"C:\\Users\\{home_directory}\\OneDrive\\Desktop\\Spotlight\\_Landscape_Photos\\_Landscape_{foldername}\\{photos[i]}.jpg")
    i += 1