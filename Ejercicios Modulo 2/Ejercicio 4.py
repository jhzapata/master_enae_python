import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

conn = sqlite3.connect('Ejercicios Modulo 2/sqlite.db') 

query = "SELECT * FROM big_bang_theory"
big_bang_theory = pd.read_sql(query, conn)

df_pivot = big_bang_theory.groupby(['Location', 'Speaker']).size().unstack(fill_value=0)

df_pivot.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='Set3')

plt.title('Gráfico de Barras Apiladas: Localización y Personajes')
plt.xlabel('Localización')
plt.ylabel('Número de apariciones')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()