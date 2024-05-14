import pandas as pd

url = "https://uk.wikipedia.org/wiki/%D0%9D%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%BD%D1%8F_%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B8"
tables = pd.read_html(url, attrs={"class": "wikitable collapsible collapsed"})

#прописуємо 4 таблицю
df = tables[3]

#1 head
print(f'Перше завдання: \n {df.head()}')

#2 shape
print(f'Друге завдання: \nShape датафрейму: {df.shape}' )

#3 NaN
df_3task = df.apply(pd.to_numeric, errors='coerce')
print(f'Третє завдання: \n{df_3task}')

#4 dtypes
print(f'Четверте завдання: \n{df.dtypes}')

#5 ппц
non_numeric_cols = df.columns[~df.map(lambda x: isinstance(x, (int, float))).all()]
df_5task = df.copy()
df_5task[non_numeric_cols] = df_5task[non_numeric_cols].apply(pd.to_numeric, errors='coerce')
print(f"П'яте завдання: \n{df_5task}")

#6 Обчислення частки пропусків у кожному стовпці
df_6task = df.isnull().sum() / len(df) * 100
print(f'Частка пропусків у кожному стовпці: \n{df_6task}')

#7 видалення рядка
df_7task = df.drop(27)
print(f'Таблиця без рядка "Україна": \n{df_7task}')

#8 замінення середнім заначенням 
df_filled = df_3task.fillna(df_3task.mean())

df_surgeon1 = df_filled.drop(df.columns[0], axis=1)
df_surgeon2 = df.pop(df.columns[0])
df_surgeon1.insert(0, 'Регіон', df_surgeon2)

print(f'Замінити пусті значення на середнє значення: \n {df_surgeon1}')

#9 операції з 2019 роком
df_9task = df_3task.iloc[:, -1]

regions_above_average = df_9task[df_3task.iloc[:, -1] > df_3task.iloc[:, -1].iloc[-1]]

print(f'Регіони де рівень народжуваності за 2019 рік був більше середнього по країні \n {regions_above_average}')