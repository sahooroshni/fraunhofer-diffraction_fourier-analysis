# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 18:05:51 2022

@author: roshn
"""

#This program generates a diffraction pattern for a rectangular aperture 

import numpy as np 
import matplotlib 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import axes3d 

N = 31       #total sub-intervals 
M = 31        #total sub-intervals
a = 7       #slit width = a 
b = 6       #slit height = b

#rectangular function = spatial domain 
f = np.zeros((N,M))
m = int((N+1)/2)
for i in range(a):
    for j in range(b):
            f[i,j] = (-1)**(i+j)
    
        
         
#print(f)

#frequency domain array 
dft = np.zeros((N,M),complex)

for u in range(N):
    for v in range(M):
        add = 0 
        for x in range(N):
            for y in range(M):
                add += f[x,y]*np.exp(-2j*np.pi*((u*x/M) + (v*y/N)))
                dft[u,v] = add 

#3-D Plotting diffration pattern 
x = np.linspace(0,N,N)
y = np.linspace(0,M,M)
print(len(x))
xx, yy = np.meshgrid(x,y)
fig = plt.figure(1)
ax = fig.add_subplot(1, 2, 1, projection='3d')
p = ax.plot_surface(xx,yy,np.abs(dft)/np.max(np.abs(dft)), cmap='hot')
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.set_zticklabels([])


#3d plotting of rectangular aperture 
f1 = np.zeros((N,M))
a = 1
b = 8
m = int((N+1)/2)
for i in range(m-a-1,m+a):
    for j in range(m-b-1,m+b):
        f1[i,j] = 1
ax = fig.add_subplot(1, 2, 2, projection='3d')
p = ax.plot_surface(xx,yy,f, cmap='hot')
ax.set_ylabel('y')
ax.set_xlabel('x')
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.set_zticklabels([])

fig, ax = plt.subplots()
im = ax.imshow(np.abs(dft), cmap=matplotlib.cm.gray, vmin=abs(dft).min(), vmax=abs(dft).max())
im.set_interpolation('bilinear')
#cb = fig.colorbar(im, ax=ax)
# Turn off tick labels
ax.set_yticklabels([])
ax.set_xticklabels([])
        
