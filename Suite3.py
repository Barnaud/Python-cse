def s(u0, u1):
    u = []
    u.append(u0)
    u.append(u1)
    print(u)
    for k in range(2,10):
        u.append(5*u[k-1]-6*u[k-2])
    return(u)
