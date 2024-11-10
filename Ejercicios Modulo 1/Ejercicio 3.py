#Crea un data frame en pandas con 201 filas y las siguientes columnas:
#  a. Una a la que denominaremos t, con los números entre 0 y 4 separados por intervalos de 0.02. Es decir: 0, 0.02, 0.04, …, 4
#  b. Otra con el seno de t a la que llamaremos s.
#  c. Otra con el seno el valor que tiene el seno de t 10 registros posteriores al que llamaremos s10. Sugerencia: El método shift de un data frame de pandas permite
#  crear columnas a partir del desplazamiento de la posición de otras.
#  d. Otra columna a la que llamaremos d que será la diferencia entre las dos anteriores.
#  e. Otra columna a la que llamaremos p. Esta columna será igual a 1 si el registro de la columna d es positivo y 0 si es negativo.
#  f. Guarda el resultado en un archivo “.csv” separado por “;”.

import pandas as pd
from numpy import sin ,pi

df=pd.DataFrame()
t=[]
d=0
for x in range (201):
    d= d+0.02
    t.append(d)

df['t'] = t
df['s'] = sin(df.t)

lista_s10=[]

for d in range(10):
   lista_s10.append(0)

for i in range(191):
   lista_s10.append(df.s[i])

df['s10'] = lista_s10

df['d'] = df['s'] - df['s10'] 

lista_p =[]

for i in df['d']:
   if i > 0:
      lista_p.append(1)
   else:
      lista_p.append(0)

df['p'] = lista_p

df.to_csv('ejercicio3.csv', sep=';', index=False)

print(df)

