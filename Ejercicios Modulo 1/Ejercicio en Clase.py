#Generar una lista de numeros aleatoreos  entre 0 y 1
#partiendo de ella obtener otra que en las posiciones donde haya un numero mayor que 0.5 
#indique cuantos numeros hay mayores que 0.5 y en las menos de 0.5 indique cuantos elementos hay menores de 0.5 
#Ejemplo [0.1,0.6,0.3][2,1,2]

import numpy as np
n = 5
random_list = np.random.rand(n)
print(random_list)
count_menor = np.sum(random_list < 0.5)
print(count_menor)
count_mayor = np.sum(random_list > 0.5)
print(count_mayor)
result_list = [count_mayor if x > 0.5 else count_menor for x in random_list]
print(result_list)
