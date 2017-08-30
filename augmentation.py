#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 20:00:45 2017

@author: anuragrai
"""

import cv2 as cv
import numpy as np
                               
def brightness_aug(image):
    img_hsv = cv.cvtColor(image, cv.COLOR_RGB2HSV);
    img_hsv = img_hsv.astype(np.float64);
    scale_v = .5 + np.random.uniform();
    img_hsv[:,:,2] = img_hsv[:,:,2]*scale_v;
    img_hsv[:,:,2][img_hsv[:,:,2]>255] = 255;
    img_hsv = img_hsv.astype(np.uint8); 
    img_hsv = cv.cvtColor(img_hsv, cv.COLOR_HSV2RGB);                       
    #cv.imshow('image', img_hsv);
    #cv.waitKey(0);
    #cv.destroyWindow('image');
    #print(img_hsv);
    #print(np.shape(img_hsv));
    return img_hsv;
      
  
img = cv.imread('IMG/center_2017_08_30_19_40_55_684.jpg', cv.IMREAD_COLOR );
                  
for i in range(20):
    bg_aug_img = brightness_aug(img);
    cv.imshow('bg_image', bg_aug_img);
    cv.waitKey(5000);
    cv.destroyWindow('bg_image');                         
                
