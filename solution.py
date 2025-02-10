import pandas as pd

# 1
df = pd.read_csv('./data/gapminder_all.csv')

df = df[df['country'] == 'Serbia']
print(df['gdpPercap_2007'].values[0])


# 2
'''
1st line - read the csv file and index is using the column namec 'country'
2nd line - filter out the rows where the continent is 'Americas'
3rd line = drop the rows that are 'Puerto Rico' in the filtered dataframe
4th line - drop the entire column named 'continent' from the third dataframe
5th line - save the fourth dataframe as a csv
'''

# 3
'''
No


'''

# 4a
df = pd.read_csv('./data/gapminder_all.csv', index_col='country')
df_ = df['gdpPercap_1982']
print(df_)

#4b
print(df)
print(df.loc['Denmark'])
df_ = df.filter(regex='gdpPercap_(198[7-9]|199.|200.)')
print(df_)