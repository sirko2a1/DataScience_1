import pandas as pd

url = "https://uk.wikipedia.org/wiki/%D0%9D%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%BD%D1%8F_%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B8"
tables = pd.read_html(url, attrs={"class": "wikitable collapsible collapsed"})

df = tables[3]

#1
print(f'1: Перше завдання: \n{df.head()}')

#2
print(f'2: Друге завдання: \nShape датафрейму: {df.shape}')

#3
df_3task = df.replace("—", float('nan'))
print(f'3: Третє завдання: \n{df_3task}')

#4
print(f'4: Четверте завдання: \n{df.dtypes}')

#5
non_numeric_cols = df.columns[~df.map(lambda x: isinstance(x, (int, float))).all()]
df_5task = df.copy()
df_5task[non_numeric_cols] = df_5task[non_numeric_cols].apply(pd.to_numeric, errors='coerce')
print(f"5: П'яте завдання: \n{df_5task}")

#6
df_6task = df.isnull().sum() / len(df) * 100
print(f'6: Частка пропусків у кожному стовпці: \n{df_6task}')

#7
df_7task = df.drop(27)
print(f'7: Таблиця без рядка "Україна": \n{df_7task}')

#8
df_numeric = df_3task.apply(pd.to_numeric, errors='coerce')
df_filled = df_numeric.fillna(df_numeric.mean())

df_surgeon1 = df_filled.drop(df.columns[0], axis=1)
df_surgeon2 = df[df.columns[0]]
df_surgeon1.insert(0, 'Регіон', df_surgeon2)
print(f'8: Замінити пусті значення на середнє значення: \n{df_surgeon1}')

#операції з 2019 роком
average_value = df_numeric.iloc[-1, -1]

regions_above_average = df[df_numeric.iloc[:, -1] > average_value]

print(f'9: Регіони де рівень народжуваності за 2019 рік був більше середнього по країні: \n {regions_above_average}')

#операції з 2014 роком
births_2014 = df_3task[['Регіон', '2014']]

births_2014_clean = births_2014.dropna()

births_2014_clean['2014'] = pd.to_numeric(births_2014_clean['2014'])

fastest_birth_rate_2014 = births_2014_clean[births_2014_clean['2014'] == births_2014_clean['2014'].max()]

print(f'10: Регіон, де в 2014 році була найбільша народжуваність: \n{fastest_birth_rate_2014}')
