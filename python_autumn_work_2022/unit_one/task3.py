# todo: Данные две переменные:
# Нужно обменять значения переменных местами. В итого age должен равнятся 25 а  temperature – 36.6:
age = 36.6
temperature = 25

age, temperature = temperature, age
print(age)
print(temperature)

age = 36.6
temperature = 25

temp = age
age = temperature
temperature = temp
print(int(age))
print(float(temperature))
