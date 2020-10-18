import os
import numpy as np
import PIL.Image as Image
from numpy.lib.function_base import append

def isImageFile(fileName: str) -> bool:
    for extension in ['.jpeg', '.png', '.jpg']:
        if extension in fileName:
            return True
    return False

def listImages(directory) -> list:
    files = sorted(os.listdir(directory))
    return [os.path.join(directory, f) for f in files if isImageFile(f)]

def preprocessImages(image):
    img = np.array(image)
    imagePartForward = []
    imagePartBackward = []
    for xPart in range(img.shape[0]//256):
        for yPart in range(img.shape[1]//256):
            forwardPart = img[xPart*256:xPart*256+256]
            forwardPart = forwardPart.transpose(1,0,2)[yPart*256:yPart*256+256].transpose(1,0,2)
            backwardPart = img[(img.shape[1]-xPart)*256-256:(img.shape[1]-xPart)*256]
            backwardPart = backwardPart.transpose(1,0,2)[yPart*256:yPart*256+256].transpose(1,0,2)
            imagePartForward.append(forwardPart)
            imagePartBackward.append(backwardPart)
    return {'Forward':imagePartForward,'Backward':imagePartBackward}

def loadImages(path : str,folders : list,nImage=-1) -> dict:
    if nImage < 0 :
        nImage = float('inf')
    blurPath,sharpPath = os.path.join(path,folders[0]),os.path.join(path,folders[1])
    blurImagePath,sharpImagePath = listImages(blurPath),listImages(sharpPath)
    blurImage,sharpImage = [],[]
    for blur,sharp in zip(blurImagePath,sharpImagePath) :
        blurImage.append(preprocessImages(Image.open(blur)))
        sharpImage.append(preprocessImages(Image.open(sharp)))
        if len(blurImage) > nImage - 1 : break
    return {
        'blur' : blurImage,
        'sharp': sharpImage,
        'blurPath' : blurImagePath[:nImage],
        'sharpPath': sharpImagePath[:nImage]
    }

def deprocessImages():
    pass


##For test Only
if __name__ == '__main__':
    a = loadImages('./datasets/',['blurred','sharp'],1)
    print(a['blur'][0]['Forward'])