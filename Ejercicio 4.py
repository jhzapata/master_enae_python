
# Carga el archivo creado en un nuevo programa.
# a. La última columna m será la media de los valores positivos si p es 1 
#    y la media de los valores negativos si p es 0. 
#    Sugerencia: los métodos groupby y transform pueden encadenarse.
# b. Crea finalmente un data frame de solo dos filas con el sumatorio de los valores
#    negativos de la columna d y el sumatorio de los valores positivos de la columna d.
#    Sugerencia: El método groupby será suficiente.

import pandas as pd


df = pd.read_csv('./archivo.csv', sep=';')

#df.transform(lambda x: x + 1)
#df.groupby(['Animal']).mean()

for i in df['p']:
    if i == 1:
        df['m'] = df[df['d'] > 0]['d'].mean()  # Media de positivos
    else:
        df['m'] = df[df['d'] < 0]['d'].mean()  # Media de negativos

print(df)