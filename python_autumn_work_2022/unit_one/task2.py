#Преобразуйте переменную age и foo в число 
age = "23"
foo = "23abc"
print(int(age))
print(foo)

#Преобразуйте переменную age в Boolean
del age
#age = 123abc
age = 123
print(bool(age))

#Преобразуйте переменную flag в Boolean
flag = 1
print(bool(flag))

#Преобразуйте значение  в Boolean
str_one = "Privet"
str_two = ""

print(bool(str_one + str_two))

#Преобразуйте значение 0 и 1  в Boolean
bool(1)
True
bool(0)
False
print(bool(1))
print(bool(0))
