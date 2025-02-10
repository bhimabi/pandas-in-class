import pandas as pd


df = pd.read_csv('./data/gapminder_all.csv', index_col='country')

# # 1
# df_ = df.loc['Serbia']
# print(df_['gdpPercap_2007'])


# # 2
# '''
# 1st line - read the csv file and index is using the column namec 'country'
# 2nd line - filter out the rows where the continent is 'Americas'
# 3rd line = drop the rows that are 'Puerto Rico' in the filtered dataframe
# 4th line - drop the entire column named 'continent' from the third dataframe
# 5th line - save the fourth dataframe as a csv
# '''

# # 3
# '''
# No


# '''

# # 4a
# df_ = df['gdpPercap_1982']
# print(df_)

# #4b
# df_ = df.loc['Denmark']
# df_ = df_.filter(regex='gdpPercap_.*')
# print(df_.values)

# #4c
# df_ = df.filter(regex='gdpPercap_(198[6-9]|199.|200.)')
# print(df_)

# 4d
df_ = df[['gdpPercap_1952','gdpPercap_2007']]
print(df_['gdpPercap_2007'] / df_['gdpPercap_1952'])