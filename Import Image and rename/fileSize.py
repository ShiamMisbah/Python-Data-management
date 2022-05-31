import os
from os import listdir
 
def Avg_fileSize(dir):
        # get the path or directory
    folder_dir = dir
    imgDet = {}
    sum = 0
    for images in os.listdir(folder_dir):
        
        # check if the image end swith png or jpg or jpeg
        if (images.endswith(".png") or images.endswith(".jpg")\
            or images.endswith(".jpeg")):
            # display
            imageName = images
            imageSize = os.path.getsize(f'{dir}/{images}')
            imgDet [imageName] = imageSize
            sum += int(imageSize)
        
    avg = sum/len(imgDet)
    print (f'Average size of all files is: {avg} bytes')
    
Avg_fileSize("C:/Users/Admin/Desktop/Shiam/Practice/file Read/photos")