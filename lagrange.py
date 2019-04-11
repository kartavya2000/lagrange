import math
import numpy as np


def lagrange(n,i):
    def func(i,x):
        if(i==1):
            return math.sin(x)
        elif(i==2):
            return math.sin(abs(x))
        elif(i==3):
            return math.sin(x**1.5)
        elif(i==4):
            return (1+25*(x**2))**(-1)
    
    
    xj=[(-1+2*j/n) for j in range(0,n+1)]
    yj=[func(i,x) for x in xj]

    mat=np.matrix([[x**j for j in range(0,n+1)] for x in xj])
    sol=np.linalg.solve(mat,np.array(yj))

    def P(sol,x,n):
        i=0
        sum=0
        while(i<=n):
            sum=sum+sol[i]*(x**i)
            i=i+1
        return sum
    
    def error(sol,x,i,n):
        return abs(func(i,x)-P(sol,x,n))
    
    xe=[(-1+2*j/1000) for j in range(0,1001)]
    en=max(list([error(sol,x,i,n) for x in xj]))
    
    return en
      
n=int(input("Enter the number n : "))
i=int(input("Enter the index of function you want: "))

en=lagrange(n,i)
en1=lagrange(n-1,i)           
oth=math.log(en/en1)/math.log((n-1)/n)
print("{} {}".format(en,oth))      


