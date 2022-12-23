import os
#change C:\\User\\newrl to C:\\Users\\$your_directory
os.chdir("C:\\Users\\newrl\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets")
listfiles = os.listdir()
print(os.listdir())
length = len(listfiles)
i = 0
photos = []
while i < length:
#    print(listfiles[i])
    if os.path.getsize(listfiles[i]) > 1000000:
        print(listfiles[i])
        photos.append(listfiles[i])
    i += 1
print(photos)
