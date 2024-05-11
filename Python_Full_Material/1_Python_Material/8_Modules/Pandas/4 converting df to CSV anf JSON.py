#Converting to csv,json
import pandas as pd

df = pd.read_csv('F:\emp1.csv')
print(df)

df.to_csv('emp1.csv')

df.to_json('emp2.json')
