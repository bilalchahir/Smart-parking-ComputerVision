import pickle as pkl
import numpy as np
import cv2
from skimage.transform import resize


MODEL = pkl.load(open("model.pkl", "rb"))


def process_image(image):
    
    image=resize(image,(15,15))
    image=image.flatten()
    image=np.asarray(image)
    return MODEL.predict([image])
    
