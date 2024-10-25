#Calcula el septuagésimo tercer (73º) número primo.

import numpy as np

def nosoyprimo(x):
    if x < 2:
        return True
    for i in range(2, int(np.sqrt(x)) + 1):
        if x % i == 0:
            return True
    return False
    
count = 0
primo = 1
list_primos = []
while count < 73:
    primo += 1
    if nosoyprimo(primo):
        list_primos.append(primo)
        count += 1


print(list_primos)