# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 11:59:37 2020

@author: Administrator
"""

import cv2 
import os
import imageio


def vedio_to_pic(path):

    vedio_path=os.listdir(path)
    count=0
    for vedio in vedio_path:
    
        videoCapture=cv2.VideoCapture()
        videoCapture.open(os.path.join(path,vedio,vedio+'.flv'))
        fps=videoCapture.get(cv2.CAP_PROP_FPS)
        frames = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
        #fps是帧率，意思是每一秒刷新图片的数量，frames是一整段视频中总的图片数量。
        print("fps=",fps,"frames=",frames)
        print(count)
        for i in range(int(frames)):
            ret,frame=videoCapture.read()
            if ret:
                if i%int(fps/5)==0:        
                    cv2.imwrite("pic/jieni{}_{}.jpg".format(count+1,i),frame)

        count+=1
            
    
def make_gif():
    gif_images=[]
    img_paths=os.listdir('gif')
    img_paths=[os.sep.join(['gif',i]) for i in img_paths]
    for path in img_paths:
        gif_images.append(imageio.imread(path))
    imageio.mimsave("a.gif",gif_images,fps=4)
    
    
make_gif()
# path='E:\\git\\Git\\Reptile\\bilibili_video'
# vedio_to_pic(path)