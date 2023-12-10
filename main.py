import shutil
import os

files = os.listdir()
for file in files:
    newDirName = file[:-4]
    os.mkdir(newDirName)
    shutil.move(file, newDirName + "/" + file)
        
