#Calcula el septuagésimo tercer (73º) número primo.

import numpy as np

def soyprimo(x):
    if x < 2:
        return False
    for i in range(2, int(np.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
    
count = 0
primo = 1
list_primos = []
while count < 73:
    primo += 1
    if soyprimo(primo):
        list_primos.append(primo)
        count += 1


print(list_primos[-1])
