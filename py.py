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
df_3task = df.replace("—", float('nan'))
print(f'Третє завдання: \n{df_3task}')

#4 dtypes
print(f'Четверте завдання: \n{df.dtypes}')

#5 ппц
non_numeric_cols = df.columns[~df.applymap(lambda x: isinstance(x, (int, float))).all()]
df_5task = df.copy()
df_5task[non_numeric_cols] = df_5task[non_numeric_cols].apply(pd.to_numeric, errors='coerce')
print(f"П'яте завдання: \n{df_5task}")