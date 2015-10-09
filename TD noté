##B.arnaud
import matplotlib.pyplot as plp
import numpy as np


z=list()
z.append(complex(1,2))
plp.plot([-2.5,2],[0,0])
plp.plot([0,0],[-2,2.5])
for i in range (1,300):
    z.append(((31**.5)/8)*complex(-1,1)*z[i-1])
    plp.plot ([z[i].real], [z[i].imag],'o')
    plp.pause(0.1)
    print (i)
#     Il semble que l'argumente de 3pi/4 à chaque occurence. aussi, il semble que le module tende vers 0 car il se multiplie à chaque fois par sqrt(31)/8<0
# La suite tend donc vers 0
print (z)
