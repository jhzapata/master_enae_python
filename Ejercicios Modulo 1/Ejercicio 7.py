# Sube a un repositorio de git hub un programa que encuentre un intervalo que
# tenga 73 números no primos seguidos y compártelo a través de su link en Git Hub.


import numpy as np

def nosoyprimo(x):
    if x < 2:
        return True
    for i in range(2, int(np.sqrt(x)) + 1):
        if x % i == 0:
            return True
    return False
    
count = 0
Noprimo = 1
list_Noprimos = []
while count < 73:
    Noprimo += 1
    if nosoyprimo(Noprimo):
        list_Noprimos.append(Noprimo)
        count += 1
 
print( list_Noprimos[0],list_Noprimos[-1])