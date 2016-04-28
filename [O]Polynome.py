def poly(a,n):
    b = [0 for k in range(n+1)]
    b[n] = a
    return(polynome(b))
class polynome:
    def __init__(self, lst = 0):
        
        if(type(lst) == list):
            if (lst == [0 for k in range(len(lst))]):
                self.liste = [0]
                return(None)
            a = len(lst)-1
            
            while(lst[a]==0):
                a-=1
            self.liste = [lst[k] for k in range(a+1)]
        elif (type(lst) == int or type(lst) == float):
            self.liste = [lst]
    def __repr__(self):
        msg = ""
        if(len(self.liste) == 1):
            return(str(self.liste[0]))
        for k in range(1, len(self.liste)-1):
            
            if(self.liste[-k] !=0):
                if (k!=1):
                    msg+="+"
                if(self.liste [-k]!=1):
                    msg+=str(self.liste[-k])
                msg+="x**"
                msg+=str(len(self.liste)-k)
        if(self.liste[1] !=0 ):
            if(len(self) != 2):
                msg+="+"
            if(self.liste[1] !=1):
                msg+=str(self.liste[1])
            msg +="x"
        if(self.liste[0] !=0):
            msg+="+"
            msg+=str(self.liste[0])
        return(msg)
        
    def __len__(self):
        return(len(self.liste))
        
    def getListe(self):
        return(self.liste)
        
    def __getitem__(self,i = None):
        if(i == None):
            return(self.liste)
        else:
            if (i>len(self)-1):
                return(0)
            return(self.liste[i])
    
    def __setitem__(self, i,valeur):
        if(i<len(self)-1):
            self.liste [i] = valeur
            
        else:
            D = poly(valeur, i)
            
            E = self + D
            self.liste = E.liste
            
           
    
    
    def __add__(self, objet):
        if (type(objet) == int or type(objet) == float):
            return(self+polynome([objet]))
        elif(type(objet == polynome)):
            
            return(polynome([self[k]+objet[k] for k in range(max(len(objet), len(self)))]))
    def __sub__(self, objet):
        return(self+objet*(-1))
        
    def __mul__(self, objet):
        if (type(objet) == int or type(objet) == float):
            return(polynome([self.liste[k]*objet for k in range(len(self))]))
        else:
            C = []
            n = max(len(self), len(objet))
            for k in range(2*n):
                C.append(0)
                for i in range(k+1):
                    C[k] +=self[i]*objet[k-i]
                
            return(polynome(C))
    def __truediv__(self, objet):
        return(self*(1/objet))
    
    def __eq__(self, objet):
        if(type(objet) == polynome):
            return(self.liste == objet[None])
        else:
            return(self.liste[0] == objet and len(self) == 1)
    def __ne__(self, objet):
        if(type(objet) == polynome):
            return(self.liste != objet[None])
        else:
            return(self.liste[0] != objet or len(self) != 1)
    def __iadd__(self, objet):
        self = self+objet
        return(self)
    def __isub__(self, objet):
        self = self-objet
        return(self)
    def __imul__(self, objet):
        self = self*objet
        return(self)
    def __pow__(self, nb):
        a = self
        for k in range(nb-1):
            self*=a
        return(self)
    def __floordiv__(self, objet):
        q = polynome()
        r = self
        while(len(objet)<=len(r)):
            
            q+=poly(r[-1]/objet[-1], len(r)-len(objet))
            
            r-=(poly(r[-1]/objet[-1], len(r)-len(objet))*objet)
            
            
            
        return(q)
        
    def __mod__(self, objet):
        q = polynome()
        r = self
        while(len(objet)<=len(r)):
            
            q+=poly(r[-1]/objet[-1], len(r)-len(objet))
            
            r-=(poly(r[-1]/objet[-1], len(r)-len(objet))*objet)
            
            
            
        return(r)
    def img(self,x):
        a = self[-1]
        for k in range(len(self)-1, 0,-1):
            a*=x
            a+=self[k-1]
        
        return(a)
    
    def derive(self):
        return(polynome([(k+1)*self[k+1] for k in range(len(self)-1)]))
        
    def integre(self):
        return(polynome([0]+[self[k-1]/(k) for k in range(1, len(self)+1)]))
            
