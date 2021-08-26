import os
import time
import shutil

time.time()
path=input("enter a directory")
listOfFile=os.listdir(path)

for file in listOfFile:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    if ext=="":
        continue
    if os.path.exists(path+"/"+ext):
        shutil.move(path+"/"+file, path+"/"+ext+"/"+file)
    else:
        os.makedirs(path+"/"+ext)
        shutil.move(path+"/"+file, path+"/"+ext+"/"+file)
    