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

df.to_csv('archivo.csv', sep=';', index=False)

print(df)

