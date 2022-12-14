# -*- coding: utf-8 -*-
"""matplotlib.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tShRG2KZ1oUtcWxPfpLknjsfey9S43MK
"""

import matplotlib
print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,5])
y=np.array([0,200])

plt.plot(x,y)
plt.show()

ypoints=np.array([2,4,6,1,8,9])
#plt.plot(ypoints,marker='o') #circle
#plt.plot(ypoints,marker='*') #star
#plt.plot(ypoints,marker='x') # cross
#plt.plot(ypoints,marker='X') #filled cross
#plt.plot(ypoints,marker='+') #plus
#plt.plot(ypoints,marker='P') #filled plus
#plt.plot(ypoints,marker='s') #square
plt.plot(ypoints,marker='D') #diamond
#plt.plot(ypoints,marker='d') #thin diamond
#plt.plot(ypoints,marker='p') #pentagon
#plt.plot(ypoints,marker='H') #hxagon
#plt.plot(ypoints,marker='v') #triangle down
#plt.plot(ypoints,marker='^') #triangle up
#plt.plot(ypoints,marker='<') #triangle left
#plt.plot(ypoints,marker='>') #triangle right
#plt.plot(ypoints,marker='1')  #tri down
#plt.plot(ypoints,marker='2')  #tri up
#plt.plot(ypoints,marker='3')   #tri left
#plt.plot(ypoints,marker='4')   # tri right
#plt.plot(ypoints,marker='|')     #vline
#plt.plot(ypoints,marker='_')    #hline

import matplotlib.pyplot as plt
import numpy as np

ypoint=np.array([2,5,8,1])
plt.plot(ypoint,'o-.r')      # fmt= marker|line|color
plt.show()

import matplotlib.pyplot as plt
import numpy as np

ypoint=np.array([2,5,8,1])
plt.plot(ypoint,'o--r')      # fmt= marker|line|color
plt.show()

import matplotlib.pyplot as plt
import numpy as np

ypoint=np.array([2,5,8,1])
plt.plot(ypoint,'o:r')      # fmt= marker|line|color
plt.show()

import matplotlib.pyplot as plt
import numpy as np

ypoint=np.array([2,5,8,6,1])
plt.plot(ypoint,marker='o',ms='30')      # marker= marker style, ms= marker size
plt.show()

import matplotlib.pyplot as plt
import numpy as np

ypoint=np.array([2,5,8,6,1])
plt.plot(ypoint,marker='o',ms='20',mfc='#234590',mec='r')   # 
plt.show()         #mfc=markerface color, mec=markeredge color

import matplotlib.pyplot as plt
import numpy as np

ypoint=np.array([2,5,8,6,1])
plt.plot(ypoint,marker='^',linestyle='dotted',color='r',ms='20',mfc='cyan',mec='red')   # 
plt.show()