import matplotlib.pyplot as plp
import numpy as np


def f(u,q):
    return (((1-u**2)**2+((u**2)/(q**2)))**-0.5)

    
u = np.linspace (0,7,1000)
plp.axis ([0,6,0,3.5])
plp.grid()
for q in range (1,10):
    plp.plot (u, f(u,q*2**-1.5))
    
    plp.text(4,3,'Q = '+ str(q)+'/sqrt(2)', backgroundcolor = 'white', color = 'black')
    plp.pause(1)
   
    
    
plp.show()
