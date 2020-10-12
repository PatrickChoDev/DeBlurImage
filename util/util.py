import os
import numpy as np
import PIL.Image as Image

def isImageFile(fileName : str) -> bool:
    for extension in ['.jpeg','.png','.jpg']:
        if extension in fileName:
            return True
    return False

def listImages(directory) -> list:
    files = sorted(os.listdir(directory))
    return [os.path.join(directory, f) for f in files if isImageFile(f)]

def preprocessImages(image : Image.Image) -> np.ndarray :
    img = np.array(image)/255
    imagePartForward = np.array([],dtype=float)
    for xPart in range(img.shape[0]//256-1):
        for yPart in range(img.shape[1]//256-1):
            pass
    return imagePartForward

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
        'blurPath' : blurImagePath,
        'sharpPath': sharpImagePath
    }

def deprocessImages():
    pass


if __name__ == '__main__':
    a = loadImages('./datasets/',['blurred','sharp'],1)
    print(a['blur'])