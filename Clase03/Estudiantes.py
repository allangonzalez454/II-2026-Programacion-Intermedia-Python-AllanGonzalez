import pandas as pd

df = pd.read_csv('./Clase03/Estudiantes.csv')

print(df['Edad'].max())

print(df['Edad'].min())

print(df['Estatura'].max())

print(df['Estatura'].min())