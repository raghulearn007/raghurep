# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 06:55:51 2018

@author: click
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import data

#just grayscale color
coins=data.coins()
plt.imshow(coins)
plt.show()
type(coins)
coins.shape

#Colored image
cat=data.chelsea()
plt.imshow(cat)
plt.show()


#subplot image from linear numpy array;
linear0=np.linspace(0,1,2500).reshape(50,50)
linear1=np.linspace(0,255,2500).reshape(50,50).astype(np.uint)

fig,(ax0,ax1)= plt.subplots(1,2)
ax0.imshow(linear0,cmap='gray')
ax1.imshow(linear1,cmap='gray');
fig.show()

#read same image as jet or gray;

image=data.camera()
type(image)
fig,(ax_jet,ax_gray)=plt.subplots(ncols=2,figsize=(10,5))
ax_jet.imshow(image,cmap='jet')
ax_gray.imshow(image,cmap='gray')
fig.show()

#lets subset the face from above image;
face=image[80:160,200:280]
fig,(ax_jet,ax_gray)= plt.subplots(1,2)
ax_jet.imshow(face,cmap='jet')
ax_gray.imshow(face,cmap='gray')
face.show()


#Draw concentric circles;
X,Y=np.ogrid[-5:5:0.1,-5:5:0.1]
R=np.sqrt(X**2+Y**2)
fig,(ax_jet,ax_gray)=plt.subplots(ncols=2)
ax_jet.imshow(R,cmap='jet')
ax_gray.imshow(R,cmap='gray')
fig.show()



