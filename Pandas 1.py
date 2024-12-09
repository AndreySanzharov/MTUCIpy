import pandas as pd
import matplotlib.pyplot as plt

# Загрузка и предварительная обработка данных
data = pd.read_csv('Titanic.csv')  # Загрузка данных
data_with_index = pd.read_csv('Titanic.csv', index_col='PassengerId')  # Установка идентификатора
data = data.dropna()  # Удаление строк с пропущенными значениями

# Описание базы данных
print("Информация о данных:")
print(data.info())  # Информация о переменных и их типах

print("\nОписательные статистики по количественным показателям:")
print(data.describe())  # Описательные статистики

# Построение гистограммы возраста
plt.hist(data['Age'], bins=20, color='red')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()

print("\nОписательные статистики по стоимости билетов:")
print(data['Fare'].describe())  # Статистика для Fare

# Работа со строками и столбцами
print("\nНазвания столбцов:")
print(list(data.columns))  # Вывод списка названий столбцов

data.rename(columns={'Pclass': 'Class'}, inplace=True)  # Переименование столбца

female_data = data[data['Sex'] == 'female']  # Женщины
ymale_data = data[(data['Sex'] == 'male') & (data['Survived'] == 1) & (data['Age'] < 32)]  # Молодые выжившие мужчины
class_1_2 = data[data['Class'].isin([1, 2])]  # Пассажиры 1 или 2 класса
survived_class_1_2 = data[(data['Survived'] == 1) & (data['Class'].isin([1, 2]))]  # Выжившие пассажиры 1 или 2 класса

data['Female'] = data['Sex'].apply(lambda x: 1 if x == 'female' else 0)  # Новый столбец Female

# Группировка
print("\nУникальные значения Embarked:")
print(data['Embarked'].unique())  # Уникальные значения Embarked

print("\nСредние значения по группам Survived:")
print(data.groupby('Survived').mean())  # Средние значения по группам

age_stats = data.groupby('Sex')['Age'].agg(['mean', 'median'])  # Средние и медианные значения возраста по полу
print("\nСредние и медианные значения возраста по полу:")
print(age_stats)

# Выгрузка базы в файл
data.columns = map(str.lower, data.columns)  # Преобразование названий столбцов в нижний регистр
data.to_csv('Titanic-new.csv', index=False)  # Сохранение в новый CSV файл
print("\nДанные сохранены в файл 'Titanic-new.csv'")
