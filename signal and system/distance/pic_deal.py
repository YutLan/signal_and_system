
import os
#图像读取库
from PIL import Image
#矩阵运算库
import numpy as np
import tensorflow as tf
import cv2

data_dir="G:/Deeplearn/distance"
for fname in os.listdir(data_dir):
   try:
        fpath = os.path.join(data_dir, fname)
        print(fpath)
        image=Image.open(fpath)
        image=image.resize((32,32),Image.ANTIALIAS)
        image.save(data_dir+'/_5_'+fname)
        print(image.size)
   except:
       print("not pic")
        #image=image.resize((32,32),Image.ANTIALIAS)
        #cv2.imshow('src1',image)
        #cv2.waitKey()
        #path="G:/Deeplearn/OwnCollection/OwnCollection/non-vehicles/Test4"
        #image.save(path+'/10_'+fname)
