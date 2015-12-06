import matplotlib.pyplot as plp
import numpy as np

x=np.linspace(0,2*np.pi,201)
for i in range(201):
    plp.clf()
    plp.subplot(2,2,1)
    plp.axis([-1,1,-1,1])
    plp.plot([-1,1],[0,0],color = 'blue')
    plp.plot([0,0],[-1,1],color = 'blue')
    plp.plot(np.cos(x)**3,np.sin(x)**3)
    plp.plot([0,np.cos(x[i])**3],[0,np.sin(x[i])**3])
    plp.text(0.7,0.7,r'$\theta = $'+str(i) + r'$\times\frac{\pi}{100}$')
#     Merci élise pour le latek, j'aurais pas eu la foie de chercher des docs
    plp.axis('equal')
    plp.subplot(2,2,2)
    plp.title('ABS')
    plp.xticks([0,np.pi/2,np.pi,3*np.pi/2,2*np.pi],[0,r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$'])
    plp.axis([0,2*np.pi,-1,1])
    plp.plot(x[0:i],np.cos(x[0:i])**3)
    plp.grid()
    plp.subplot(2,2,3)
    plp.grid()
    plp.title("ORD")
    plp.xticks([0,np.pi/2,np.pi,3*np.pi/2,2*np.pi],[0,r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$'])
    plp.axis([0,2*np.pi,-1,1])
    plp.plot(x[0:i],np.sin(x[0:i])**3)
    plp.subplot(2,2,4)
    plp.title("Régime pseudo-périodique")
#     Il fait bien combler l'espace vide, quite à ralentir le programme
    plp.plot(x[0:i],np.exp(-x[0:i])*np.cos(x[0:i]*2*np.pi))
    plp.axis([0,2*np.pi,-1,1])
    plp.show()
    plp.grid()
    plp.pause(0.1)


