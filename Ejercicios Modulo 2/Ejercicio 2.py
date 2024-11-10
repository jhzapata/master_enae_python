import sqlite3
import pandas as pd


df = pd.read_csv('Ejercicios Modulo 2/big_bang_theory_dataset.csv', sep=',')

conn = sqlite3.connect('Ejercicios Modulo 2/sqlite.db') 
cursor = conn.cursor()

df = df.iloc[:, 1:]

df.to_sql('big_bang_theory', conn, if_exists='replace', index=False)

# 4. Consultar la tabla para verificar que se ha creado
query = "SELECT * FROM big_bang_theory"
result = pd.read_sql(query, conn)
print(result)

conn.close()
