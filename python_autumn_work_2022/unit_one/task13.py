#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.

mass=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
massnew = mass
for i in range(len(massnew)):
    massnew[i] +=1
print(massnew)