import matplotlib.pyplot as plt
import numpy as np

y = np.linspace(-1,1,100);
x = np.linspace(-3,-1,100);
plt.clf();
plt.axis([-3,1,-10,10]);

for k in range(-5,6):
    plt.plot (x,1+ (np.exp(x)*(x+1))*k);
    plt.plot (y,1+(np.exp(y)/(y+1))*k);

    plt.pause(0.5);
plt.plot([-1,-1],[-100,100]);

plt.show();
plt.grid();

