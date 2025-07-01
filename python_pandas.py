import pandas as pd 
import re
data = pd.read_csv("modified_pokemon.csv")
#data['Total'] = data['HP'] + data['Attack'] + data['Defense'] + data['Sp. Atk'] + data['Sp. Def'] + data['Speed']
#print(data[['Name', 'Type 1','HP']]) 
#print(data.iloc[0:4])
#print(data.describe)
#print(data.sort_values('Name',ascending=False))
#print(data.sort_values(['Type 1','HP',]))
#new_data = data.loc[(data['Type 1'] == 'Fire') & (data['Type 2'] == 'Flying') & (data['HP'] > 70)]
#new_data = data.reset_index()
#new_data.to_csv('modified_pokemon.csv', index=False)
#new_data = data.loc[data['Type 1'].str.contains('Fire|Water' , regex=True)]
#new_data = data.loc[~data['Name'].str.contains('Mega')]
#new_data = data.loc[data['Name'].str.contains('^pi[a-z]' , flags=re.I, regex=True)]
#data.loc[data['Type 1'] == 'Fire','Type 1' ] = 'Flamer'
#data.loc[data['Type 1'] == 'Fire', 'Legendary'] = True
data = data.groupby(['Type 1']).mean(numeric_only=True).sort_values("Total",ascending=False)
#data.to_csv('modified_pokemon.csv')
print(data)