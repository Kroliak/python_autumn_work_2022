#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().
# При решении задачи обратите внимание какой тип вы получаете через функцию input().

A = float(input("Введите точку A на числовой оси "))
B = float(input("Введите точку B на числовой оси "))
C = float(input("Введите точку C на числовой оси "))

AC = A+C
BC = B+C
print(abs(AC))
print(abs(BC))