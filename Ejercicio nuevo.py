#Suma los 200 primeros numeros de la serie aritmetica con incremento 1 que comienza en 1. Es Decir 1,2,3,4,5,6...

x = 0
for i in range(201):
    x+=i
    
print(x)

#Suma los 200 primeros numeros de la serie aritmetica con incremento 1 que comienza en 1 y alternan uno positivo y otro negativo. Es Decir 1,-2,3,-4,5,-6...

x = 0
flag = 0
for i in range(201):
    if flag == 0:
        x+=i
        flag=1
    else:
        x-=i
        flag=0
           
print(x)

#Suma de los 200 primeros valores de n para 1/nS, y representamos estos valores en el eje  y los valores de S entre [-1,5]

import matplotlib.pyplot as plt
import numpy as np

def suma200(s):
   return sum([n**(-s) for n in range(1,201)])

x= np.arange(-1,5-0.1)
y = [suma200(s) for s in list(x)]

plt.plot(x,y)
