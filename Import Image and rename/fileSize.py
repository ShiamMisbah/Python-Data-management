import os
from os import listdir
 
def Avg_fileSize(dir):
        # get the path or directory
    folder_dir = dir
    imgDet = {}
    sum = 0
    maxi = 0
    maxiInd = 0
    mini = 10000000
    miniInd = 0
    for images in os.listdir(folder_dir):
        
        # check if the image end swith png or jpg or jpeg
        if (images.endswith(".png") or images.endswith(".jpg")\
            or images.endswith(".jpeg")):
            # display
            imageName = images
            imageSize = os.path.getsize(f'{dir}/{images}')
            imgDet [imageName] = imageSize
            sum += int(imageSize)
            if imageSize>maxi:
                maxi = imageSize
                maxiInd = imageName
            elif imageSize<mini:
                mini = imageSize
                miniInd = imageName
                
        
    avg = sum/len(imgDet)
    print (f'Average size: {avg} bytes\nMinimun size: {mini} bytes\tFile Name: {miniInd}\nMaximum Size: {maxi} bytes\tFile Name: {maxiInd}')
    
Avg_fileSize("C:/Users/Admin/Desktop/Shiam/Practice/file Read/photos")