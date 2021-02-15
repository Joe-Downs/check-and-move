import shutil
import os

# Splits a list of files and subdirectories into a list of files
# and a list of subdirectories
def splitFilesAndDir(combinedDir):
    fileList, dirList = list(), list()
    combinedList = os.listdir(combinedDir)
    for item in combinedList:
        item = os.path.join(combinedDir, item)
        if os.path.isdir(item):
            dirList.append(item)
        if os.path.isfile(item):
            fileList.append(item)
    return fileList, dirList

fileList, dirList = list(), list()
dirList = [input("What folder would you like to move? ")]

# Goes through the array of directories (just one directory at
# the beginning), adds each subdirectory to the array, and adds
# the files to the file array. Once the files in a directory are
# added, the directory is removed from the array.
while dirList != []:
    print(dirList)
    nextDir = dirList[0]
    files, directories = splitFilesAndDir(nextDir)
    fileList.extend(files)
    dirList.extend(directories)
    dirList.pop(0)
    
