import matplotlib.pyplot as plt

def u (n):
    u = 0
    for k in range(n,2*n+1):
        u += 1/k
    return (u)
    
def tableau(o):
    v= []    
    for l in range(1,o):
        v.append(u(l))
    return (v)

def tracer(p):
    plt.plot([k+1 for k in range(p)],tableau(p+1), 'o')
    plt.plot([k+1 for k in range(p)],tableau(p+1), label = 'Un')
    plt.legend(loc = 'best')
