import os
import re

""" rootdir = "/mnt/externa/Torrents/completed"
regex = re.compile('(.*zip$)|(.*rar$)|(.*r01$)')

for root, dirs, files in os.walk(rootdir):
  for file in files:
    if regex.match(file):
       print(file) """

#print(os.listdir("C:\\Users\\newrl\\AppData\\Local\\Packages"))
folders = os.listdir("C:\\Users\\newrl\\AppData\\Local\\Packages")
pattern = re.compile(r"Microsoft\.Windows\.ContentDeliveryManager_([a-zA-Z]+(\d[a-zA-Z]+)+)", re.IGNORECASE)
for folder in folders:
    if pattern.match(folder):
        print(folder)

#test