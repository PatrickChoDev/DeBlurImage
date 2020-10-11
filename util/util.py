import os
import numpy as np
import PIL.Image as Image

def isImageFile(fileName : str) -> bool:
    if ['.jpg','.png','.jpeg'] in fileName :
        return True
    return False

def listImages(directory) -> list:
    files = sorted(os.listdir(directory))
    return [os.path.join(directory, f) for f in files if isImageFile(f)]

def preprocessImages(image):
    image = image.resize(720,720)
    img = np.array(image)
    return img 

def loadImages(path : str,folders : list,nImage=-1) -> dict:
    if nImage < 0 :
        nImage = float('inf')
    blurPath,sharpPath = os.path.join(path,folders[0]),os.path.join(path,folders[1])
    blurImagePath,sharpImagePath = listImages(blurPath),listImages(sharpPath)
    blurImage,sharpImage = [],[]
    for blur,sharp in zip(blurImagePath,sharpImagePath) :
        blurImage.append(preprocessImages(Image.open(blur)))
        sharpImage.append(preprocessImages(Image.open(sharp)))

def deprocessImages():
    pass


if __name__ == '__main__':
    a = listImages('./datasets/sharp')
    print(len(a))