
# Carga el archivo creado en un nuevo programa.
# a. La última columna m será la media de los valores positivos si p es 1 
#    y la media de los valores negativos si p es 0. 
#    Sugerencia: los métodos groupby y transform pueden encadenarse.
# b. Crea finalmente un data frame de solo dos filas con el sumatorio de los valores
#    negativos de la columna d y el sumatorio de los valores positivos de la columna d.
#    Sugerencia: El método groupby será suficiente.

import pandas as pd


df = pd.read_csv('master_enae_python/Ejercicios Modulo 1/ejercicio3.csv', sep=';')

for i in df['p']:
    if i == 1:
        df['m'] = df[df['d'] > 0]['d'].mean()  # Media de positivos
    elif i  == 0:
        df['m'] = df[df['d'] < 0]['d'].mean()  # Media de negativos

df2=pd.DataFrame()
lista_neg=[]
lista_pos=[]
for i in df['d']:
    if i < 0:
        lista_neg.append(i)
    else:
        lista_pos.append(i)

negativos = sum(lista_neg)
positivos = sum(lista_pos)

df2['n'] = negativos
df2['p'] = positivos

print(df)

