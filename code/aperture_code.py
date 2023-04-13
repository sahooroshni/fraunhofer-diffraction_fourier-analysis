# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 16:39:11 2022

@author: roshn
"""
#This program generates the aperture function, i.e. diffferent aperture shapes 
import numpy as np 
import matplotlib 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import axes3d 

N= 61 
M= 61
f= np.zeros((N,M))
m = int((N+1)/2)
r = 9 
for i in range(N):
    for j in range(M):
        if np.sqrt((i**2)+(j**2))<= r:
            f[i+m,j+m] = 1
            f[m-i,m-j] = 1 
            f[m-i,m+j] = 1 
            f[m+i,m-j] = 1 

#These 3 lines of code are for a keyhole shape aperture. To generate keyhole, remove # before each line 
#for i in range(m-3,m+3+1):
 #   for j in range(m+r,m+r+7+1):
 #       f[i,j] = 1 
        
        
#3d plotting of rectangular aperture 
f1 = np.zeros((N,M))
a = 7
b = 8
m = int((N+1)/2)
for i in range(m-a-1,m+a):
    for j in range(m-b-1,m+b):
        f1[i,j] = 1
            
x = np.linspace(0,N,N)
y = np.linspace(0,M,M)
print(len(x))
xx, yy = np.meshgrid(x,y)
fig = plt.figure(1)
ax = fig.add_subplot(1, 2, 2, projection='3d')
p = ax.plot_surface(xx,yy,f, cmap='hot')
ax.set_ylabel('y')
ax.set_xlabel('x')
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.set_zticklabels([])

fig, ax = plt.subplots()
im = ax.imshow(f, cmap=matplotlib.cm.gray, vmin=abs(f).min(), vmax=abs(f).max())
im.set_interpolation('bilinear')
#cb = fig.colorbar(im, ax=ax)
# Turn off tick labels
ax.set_yticklabels([])
ax.set_xticklabels([])