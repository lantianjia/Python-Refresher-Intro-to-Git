#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,2*np.pi,0.01)
y1,y2=np.sin(x),np.cos(x)

plt.title('The plot of sinx and cosx') 
plt.plot(x,y1,color="green",lw=1)
plt.plot(x,y2,color="orange",lw=1)
plt.legend(['y=sinx','y=cosx'])
plt.show()

y3 = np.tan(x)
plt.plot(x,y3,color="blue")
plt.title('plot of tangent')
plt.legend(['y=tanx'])
plt.show()



