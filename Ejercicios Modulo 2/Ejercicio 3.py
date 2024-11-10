import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('Ejercicios Modulo 2/sqlite.db') 

query = "SELECT * FROM big_bang_theory where Speaker = 'Sheldon' and Text = 'Penny.'"
exclusivamente_penny = pd.read_sql(query, conn)

plt.subplot(1, 2, 1)
plt.hist(exclusivamente_penny['Location'], bins=len(exclusivamente_penny['Location']), color='blue', alpha=0.7, edgecolor='black')
plt.title('Localizaciones donde Sheldon dice exclusivamente "Penny."')
plt.xlabel('Localización')
plt.ylabel('Frecuencia')
plt.xticks(rotation=45)

query = "SELECT * FROM big_bang_theory where Speaker = 'Sheldon' and Text like '%Penny%'"
contiene_penny = pd.read_sql(query, conn)

plt.subplot(1, 2, 2)
plt.hist(contiene_penny['Location'], bins=len(contiene_penny['Location']), color='green', alpha=0.7, edgecolor='black')
plt.title('Localizaciones donde Sheldon dice algo que contiene "Penny"')
plt.xlabel('Localización')
plt.ylabel('Frecuencia')
plt.xticks(rotation=45)

conn.close()
# Mostrar los histogramas
plt.tight_layout()
plt.show()