#Создать переменную типа String
name_str = 'text'
print('name_str =', name_str, type(name_str))

#Создать переменную типа Integer
name_int = 5
print('name_int =', name_int, type(name_int))

#Создать переменную типа Float
name_float = 23.2
print('name_float =', name_float, type(name_float))

#Создать переменную типа Bytes
name = 'Kate'
name_bytes = bytes(name, 'utf-8')
print('name_bytes = ', name_bytes, type(name_bytes))

#Создать переменную типа List
name_list = [2,4,6,7, 'dd', 7,4]
print('name_list = ', name_list, type(name_list))

#Создать переменную типа Tuple
name_tuple = tuple('Hello world')
print('name_tuple = ', name_tuple, type(name_tuple))

#Создать переменную типа Set
name_set = {3, 2, 'tt'}
print('name_set = ', name_set, type(name_set))

#Создать переменную типа Frozen set
name_frozen_set = frozenset({3,2,1})
print('name_set_frozen', name_frozen_set, type(name_frozen_set))

#Создать переменную типа Dict
name_dict = {1:4, 4:4, 7:3}
print('name_dict = ', name_dict, type(name_dict))

#Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
a = 'Kate '
b = 'Jons'
c = a + b
print(c)

#Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
v = 'Number'
n = 5
print(v, n)

#Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
r = 'Number '
k = 6
print(r + str(k))
