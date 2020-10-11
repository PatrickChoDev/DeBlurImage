import os
import numpy as np
import PIL.Image as Image

def isImageFile(file):
    EXTENSION = ['.jpg','.png','.jpeg']
    if EXTENSION in file :
        return True
    return False

def list_image(directory,n_images):
    files = sorted(os.listdir(directory))
    return [os.path.join(directory, f) for f in files if isImageFile(f)]

def loadImages(path):
    return Image.open(path)

def preprocessImages(image):
    image = image.resize(256,256)
    img = np.array(image)
    
    return img

def deprocessImages():
    pass