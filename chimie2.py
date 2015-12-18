import matplotlib.pyplot as plt
import numpy as np

def chi(k1,k2):
    
    x = np.linspace(0,2, 1000)
    plt.clf()
    plt.grid()
    plt.text(40,0.7, "k1 ="+str(k1)+"\nk2 = "+str(k2))
    
    plt.plot(x,np.exp(-k1*x), label = 'a')
    plt.plot(x,(k1/(k2-k1))*(np.exp(-k1*x)-np.exp(-k2*x)), label = 'b')
    plt.plot(x, (1/(k2-k1))*(k2*(1-np.exp(-k1*x))-(k1*(1-np.exp(-k2*x)))), label = 'c')
    plt.legend(loc = "best")
