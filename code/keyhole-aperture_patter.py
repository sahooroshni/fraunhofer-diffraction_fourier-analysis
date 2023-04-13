# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 17:00:47 2022

@author: roshn
"""

#This program generates the diffraction pattern for a keyhole shaped aperture 

import numpy as np 
import matplotlib 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import axes3d 

N = 81       #total sub-intervals 
M = 81        #total sub-intervals
r = 9

#rectangular function = spatial domain 
f = np.zeros((N,M))
m = int((N+1)/2)
for i in range(N):
    for j in range(M):
        if np.sqrt((i**2)+(j**2))<= r:
            f[i+m,j+m] = (-1)**(i+j+(2*m)) 
            f[m-i,m-j] = (-1)**((2*m)-i-j)
            f[m-i,m+j] = (-1)**((2*m)-i+j)
            f[m+i,m-j] = (-1)**((2*m)+i-j)

for i in range(m-3,m+3+1):
    for j in range(m+r,m+r+7+1):
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
p = ax.plot_surface(xx,yy,np.abs(dft), cmap='hot')
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.set_zticklabels([])


#3d plotting of rectangular aperture 
f1 = np.zeros((N,M))
r  =13 
m = int((N+1)/2)
for i in range(N):
    for j in range(M):
        if np.sqrt((i**2)+(j**2))<= r:
            f1[i+m,j+m] = 1 
            f1[m-i,m-j] = 1 
            f1[m-i,m+j] = 1 
            f1[m+i,m-j] = 1
ax = fig.add_subplot(1, 2, 2, projection='3d')
p = ax.plot_surface(xx,yy,f1, cmap='hot')
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