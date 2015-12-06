import matplotlib.pyplot as plt
import numpy as np

def exp(sup, dpu):
    plt.clf()
    plt.grid()
    e=[1]
    for k in range(sup*dpu-1):
        e.append(e[k]+e[k]/dpu)
    x = [k/dpu for k in range(sup*dpu)]
    
    plt.plot(x,e)
    plt.plot(x, np.exp(x))
