import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

conn = sqlite3.connect('Ejercicios Modulo 2/sqlite.db') 

query = "SELECT * FROM big_bang_theory"
big_bang_theory = pd.read_sql(query, conn)

big_bang_theory['Text'] = big_bang_theory['Text'].fillna('')

big_bang_theory['Penny_count'] = big_bang_theory['Text'].str.contains('Penny', case=False).astype(int)

df_grouped = big_bang_theory.groupby(['Season', 'Speaker'])['Penny_count'].sum().reset_index(name='Penny_count')

df_grouped['Group_Index'] = df_grouped.groupby(['Season', 'Speaker']).ngroup()


print(df_grouped)


label_encoder = LabelEncoder()


df_grouped['Speaker_encoded'] = label_encoder.fit_transform(df_grouped['Speaker'])
df_grouped['Season_encoded'] = label_encoder.fit_transform(df_grouped['Season'])


X = df_grouped[['Season_encoded', 'Speaker_encoded']]  
y = df_grouped['Penny_count']  

scaler = StandardScaler()


X_scaled = scaler.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)


logreg = LogisticRegression(max_iter=1000)  


logreg.fit(X_train, y_train)


y_pred = logreg.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy de la regresión logística: {accuracy:.2f}')


print(f'Predicciones: {y_pred}')