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

# Get the path relative to the main 'root' path of the files to be moved
# e.g., if 'myFiles' is to be moved, /home/joe/myFiles/stuff/ -> stuff/
def getRelativePath(mainRoot, src):
    # If the main root does not end with a "/" (or "\") then add
    # it so that the slash will be removed for the relative source
    if not mainRoot.endswith(os.sep):
        mainRoot += os.sep
    relativePath = src.removeprefix(mainRoot)
    return relativePath

# Checks if there are the requisite folders in the destination for the
# files to be copied, if there aren't, the folders are created
def verifyDestPath(mainRoot, src, dest):
    relativeDirSrc = getRelativePath(mainRoot, src)
    fullDirDest = os.path.join(dest, relativeDirSrc)
    try:
        os.makedirs(fullDirDest)
    except FileExistsError:
        print(f"{fullDirDest} already exists")

# Copy file to the destination folder, preserving the
# original hierarchy from the main 'root'
def copyFile(mainRoot, src, dest):
    relativeSrc = getRelativePath(mainRoot, src)
    fullDest = os.path.join(dest, relativeSrc)
    shutil.copy2(src, fullDest, follow_symlinks = True)
    
fileList, dirList = list(), list()
mainRoot = input("What folder would you like to move? ")
dirList.append(mainRoot)
destDir = input("Where would you like to move the contents to? ")

# Goes through the array of directories (just one directory at
# the beginning), adds each subdirectory to the array, and adds
# the files to the file array. Directories and subdirectories are also created
# in the destination folder before the files are moved. Once the files in a
# directory are added, the directory is removed from the array.
while dirList != []:
    nextDir = dirList[0]
    # Make sure the necessary directories are present while traversing
    # the files and before copying.
    verifyDestPath(mainRoot, nextDir, destDir)
    files, directories = splitFilesAndDir(nextDir)
    fileList.extend(files)
    dirList.extend(directories)
    dirList.pop(0)

print(f"There are {len(fileList)} files to be moved")
response = input("Does that number look correct? (i.e., Do you want to continue?) [Y/n] ")

if response.lower() != "n":
    for item in fileList:
        copyFile(mainRoot, item, destDir)
