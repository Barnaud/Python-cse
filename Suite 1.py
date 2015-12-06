import matplotlib.pyplot as plp
import numpy as np

def ex1(U0):
    plt.clf()
    u = U0
    for k in range(20):
        u = (2*u**2)/(1+5*u)
        plp.plot([k+1],[u], 'ro')

