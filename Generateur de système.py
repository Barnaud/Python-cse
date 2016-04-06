from random import *
x=[randint(-10,10) for k in range(3)]
n=[randint(-10,10) for k in range(9)]
s=[]

for k in range(3):
    a=0
    for i in range(3):
        a+=n[3*k+i]*x[i]
    s.append(a)
print(x)
for k in range(10):
    print()
for k in range(3):
    print(str(n[3*k])+"x +"+str(n[3*k+1])+"y +"+str(n[3*k+2])+"z = "+str(s[k]))
