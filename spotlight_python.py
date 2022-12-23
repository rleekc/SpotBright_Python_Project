import os
from PIL import Image
from PIL.ExifTags import TAGS
import shutil
from datetime import date

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
i = 0
length = len(photos)
today = date.today().strftime("%m-%d-%Y")
foldername = f"Spotlight_Pictures_{today}"
if not os.path.exists(f"C:\\Users\\{home_directory}\\OneDrive\\Desktop\\Spotlight"):
    os.mkdir(f"C:\\Users\\{home_directory}\\OneDrive\\Desktop\\Spotlight")
if not os.path.exists(f"C:\\Users\\{home_directory}\\OneDrive\\Desktop\\Spotlight\\{foldername}"):    
    os.mkdir(f"C:\\Users\\{home_directory}\\OneDrive\\Desktop\\Spotlight\\{foldername}")
print(foldername)
while i < length:
    shutil.copy2(f"C:\\Users\\{home_directory}\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\{photos[i]}",f"C:\\Users\\{home_directory}\\OneDrive\\Desktop\\Spotlight\\{foldername}\\{photos[i]}.jpg")
    i += 1

""" 
os.chdir(f"C:\\Users\\{home_directory}\\OneDrive\\Desktop\\Spotlight\\{foldername}")
i = 0
length = len(photos)
while i < length:
    image = Image.open(photos[i])
    exifdata = image.getexif()
    for tag_id in exifdata:
    # get the tag name, instead of human unreadable tag id
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
    # decode bytes 
        if isinstance(data, bytes):
            data = data.decode()
        print(f"{tag:25}: {data}")
    i += 1
  """

