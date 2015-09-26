import matplotlib.pyplot as plp
import numpy as np

x=np.linspace(0,2*np.pi,1000)
plp.axis('equal')

for n in range(100):
    plp.plot(np.cos(x[10*n:10*(n+1)])**3,np.sin(x[10*n:10*(n+1)])**3,color = 'blue')
    plp.plot(np.cos(x[10*n:10*(n+1)]),np.sin(x[10*n:10*(n+1)]),color = 'red')
    plp.plot([0,np.cos(x[10*(n+1)])],[0,np.sin(x[10*(n+1)])])
    plp.pause(0.1)
