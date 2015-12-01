import matplotlib.pyplot as plt
import numpy as np

plt.clf()
x = np.linspace(0,6,1000)

def f(x):
    return(np.sqrt(x))
def escalier(u,n):
    u=[u]
    plt.plot(x,x)
    for k in range(1,n+1):
        u.append(f(u[k-1]))
        plt.pause(1)
        plt.plot([u[k-1],f(u[k-1])],[f(u[k-1]),f(u[k-1])], color ='green')
        plt.plot([f(u[k-1]),f(u[k-1])],[f(u[k-1]),f(u[k])], color= 'green')
    plt.plot(x,f(x))
    
