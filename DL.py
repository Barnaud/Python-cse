import matplotlib.pyplot as plp
import numpy as np

plp.grid()

x=np.linspace(0,3,100)

for n in range(20):
    plp.plot(x, x**(n+1)-2*x**n+1)
    plp.axis([0,3,-1,1])
    plp.plot([0,3],[0,0])
    plp.plot([2,2],[-1,1],label='borne Sup')
    plp.plot ([(2*n)/(n+1),(2*n)/(n+1)],[-1,1],label='borne Inf')
    plp.legend()
    plp.text(2.6,-0.8,'n={}'.format(n))
    plp.grid()
    plp.show()
    plp.pause(0.5)
    plp.clf()

