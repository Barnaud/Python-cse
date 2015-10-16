class Polynome:
    
    def __init__(self,a=0,b=0,c=0):
        self.A=a
        self.B=b
        self.C=c
    def __repr__(self):
        return ('{}x^2+{}x+{}'.format(self.A,self.B,self.C))
        
    def solve(self):
        if self.A!= 0:
            delta = (self.B**2)-(4*self.A*self.C)
            return (((-1*self.B-delta**0.5)/2*self.A),(-1*self.B+delta**0.5)/2*self.A)
        else:
            return (-self.C/self.B)
    def __add__(self,P2):
         if type(P2) == int:
             return (Polynome(self.A,self.B,self.C + P2))
         if type(P2) == __main__.Polynome:
            return (Polynome(self.A+P2.A,self.B+P2.B,self.C + P2.C))
         else:
            return (False)
    def __getitem__(self,i):
        if type(i) == int:
            
            return (self.A*i**2+self.B*i+self.C)
        if type(i) == list:
            return([self.A*nb**2+self.B*nb+self.C for nb in i])
            
