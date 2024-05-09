import numpy as np
import pandas as pd
data = pd.read_csv(r'C:\Users\User\Downloads\Telegram Desktop\test-2.csv')
survivals = data['Survived'].values
print("Общее количество выживших пассажиров:", survivals.sum())

age_fare = data[['Age', 'Fare']].values
age_fare_sorted = age_fare[np.argsort(age_fare[:, 0])]
youngest_passenger = age_fare_sorted[0]
oldest_passenger = age_fare_sorted[-1]
print("Информация о самом молодом пассажире:")
print("Возраст:", youngest_passenger[0], "Стоимость билета:", youngest_passenger[1])
print("Информация о самом старом пассажире:")
print("Возраст:", oldest_passenger[0], "Стоимость билета:", oldest_passenger[1])

relatives = data[['SibSp', 'Parch']].values
total_relatives = relatives.sum()
print("Общее количество родственников на борту:", total_relatives)
max_relatives = relatives.max(axis=1).max()
passanger_with_max_relatives = data[np.any(relatives == max_relatives, axis=1)]
print("Пассажир с наибольшим количеством родственников:")
print(passanger_with_max_relatives)