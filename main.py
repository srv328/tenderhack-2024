import pandas as pd

df = pd.read_excel("data.xlsx")

record_count = len(df)
print(f"Количество записей: {record_count}")

unique_customers = df['Название заказчика'].nunique()
unique_suppliers = df['Поставщик'].nunique()

print(f"Уникальные заказчики: {unique_customers}")
print(f"Уникальные поставщики: {unique_suppliers}")

average_start_amount = df['Нач сумма закупки'].mean()
min_start_amount = df['Нач сумма закупки'].min()
max_start_amount = df['Нач сумма закупки'].max()

print(f"Средняя начальная сумма закупки: {round(average_start_amount, 2):,}")
print(f"Минимальная начальная сумма закупки: {min_start_amount:,}")
print(f"Максимальная начальная сумма закупки: {max_start_amount:,}")

print(f"Средний процент снижения цены: {round(df['% снижения'].mean(), 3)}")

print("Количество закупок по каждому типу закупки:")
print(df['Тип закупки'].value_counts())

print("Количество закупок в каждом регионе заказчика:")
print(df['Регион заказчика'].value_counts())
print("Количество закупок в каждом регионе поставщика:")
print(df['Регион поставщика'].value_counts())

print(f"Самый повторяющийся статус закупки: {df['Статус закупки'].mode()[0]}")
print(f"Самый повторяющийся статус контракта по закупке: {df['Статус контракта по закупке'].mode()[0]}")

print(f"Топ-10 наименований по закупке: \n{df['Наименование закупки'].value_counts().head(10)}")

df['Дата начала закупки'] = pd.to_datetime(df['Дата начала закупки'], format='%d.%m.%Y')
df['Дата окончания'] = pd.to_datetime(df['Дата окончания'], format='%d.%m.%Y')
df['Длительность'] = (df['Дата окончания'] - df['Дата начала закупки']).dt.days
average_duration = df['Длительность'].mean()

print(f"Средняя длительность закупок (время между началом и окончанием): {round(average_duration, 2)} дней")
