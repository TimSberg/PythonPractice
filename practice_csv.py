import pandas as pd

df = pd.read_csv('Studie_BA_csv.csv')

file_path = 'Studie_BA_csv.csv'
data = pd.read_csv(file_path)
line_count = len(data)

print(line_count)

print(df.head())  

print(df.describe())




