import math

# Создать переменную item_1 типа integer.
item_1 = 4

# Создать переменную item_2 типа integer.
item_2 = 24

# Создать переменную result_sum в которой вы суммируете item_1 и item_2.
result_sum = item_1 + item_2

# Вывести result_sum в консоль.
print('result_sum = ', result_sum)

# Создать переменную result_subtr в которой вы вычитаете большую по значению переменную из меньшей по значению
result_subtr = item_2 - item_1

# Вывести result_subtr в консоль.
print('result_subtr = ', result_subtr)

# Создать переменную result_multi в которой вы умножаете item_1 на item_2.
result_multi = item_1 * item_2

# Вывести result_multi в консоль.
print('result_multi = ', result_multi)

# Создать переменную result_exp в которой вы item_1 возводите в степень item_2.
result_exp = item_1 ** item_2

# Вывести result_exp в консоль.
print('result_exp = ', result_exp)

# Создать переменную result_m_exp в которой вы item_1 возводите в степень item_2 используя библиотеку math.
result_m_exp = math.pow(item_1, item_2)

# Вывести result_m_exp в консоль.
print('result_m_exp = ', result_m_exp)

# Создать переменную result_s_root в которой вы найдёте квадратный корень любой из переменной item
result_s_root = item_1 ** 0.5

# Вывести result_s_root в консоль.
print('result_s_root = ', result_s_root)

# Создать переменную result_m_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math.
result_m_s_root = math.sqrt(item_1)

# Вывести result_m_s_root в консоль.
print('result_m_s_root = ', result_m_s_root)

# Создать переменную result_mp_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math используя метод pow.
result_mp_s_root = math.pow(item_1, 0.5)

# Вывести result_mp_s_root в консоль.
print('result_mp_s_root', result_mp_s_root)

#  19. Присвоить переменной item_1 odd /нечетный/ значение
item_1 = 7

#  20. Присвоить переменной item_2 even /четный/ значение
item_2 = 2

# Создать переменную result_division в которой вы разделите item_1 на item_2.
result_division = item_1 / item_2

# Вывести result_division в консоль.
print('result_division = ', result_division)

# Создать переменную result_m_floor и result_division округлить до ближайшего целого меньшего чем result_division.
result_m_floor = math.floor(result_division)

# Вывести result_m_floor в консоль.
print('result_m_floor = ', result_m_floor)

# Создать переменную result_m_ceil и result_division округлить до ближайшего целого большего чем result_division.
result_m_ceil = math.ceil(result_division)

# Вывести result_m_ceil в консоль.
print('result_m_ceil = ', result_m_ceil)

# Создать переменную result_int и result_division округлить до ближайшего целого через явное приведение.
result_int = round(result_division, 0)

# Вывести result_int в консоль.
print('result_int = ', result_int)

# Создать переменную result_no_division_loss в которой вы разделите item_1 на item_2 без остатка.
result_no_division = item_1 // item_2

# Вывести result_no_division_loss в консоль.
print('result_no_division = ', result_no_division)

# Создать переменную result_division_loss в которой вы найдёте остаток от деления item_1 на item_2.
result_division_loss = item_1 % item_2

# Вывести result_division_loss в консоль.
print('result_division_loss = ', result_division_loss)

# Дальше будет реализация через арифметические действия с присваиванием.


# Создать переменную item_3 и присвоить ей целое число
item_3 = 5

# Прибавить 10 к item_3 с присвоением.
item_3 += 10

# Вывести item_3 в консоль.
print('item_3 + 10 = ', item_3)

# Отнять 5 от item_3 с присвоением.
item_3 -= 5

# Вывести item_3 в консоль.
print('item_3 - 5 =', item_3)

# Умножить item_3 на 3 с присвоением.
item_3 *= 3

# Вывести item_3 в консоль.
print('item_3 * 3 = ', item_3)

# Разделить item_3 на 2 с присвоением.
item_3 /= 2

# Вывести item_3 в консоль.
print('item_3 / 2 = ', item_3)

# Возвести в степень 2 item_3 с присвоением.
item_3 **= 2

# Вывести item_3 в консоль.
print('item_3 ** 2 = ', item_3)

# Найти квадратный корень item_3 с присвоением.
item_3 **= 0.5

# Вывести item_3 в консоль.
print('item_3 ** 0.5 = ', item_3)

# Присвоить остаток от деления item_3
item_3 %= 3

# Вывести item_3 в консоль.
print('item_3 % 3 = ', item_3)

# Boolean

# Создать переменную b_item_t и присвоить True
b_item_t = True

# Создать переменную b_item_f и присвоить False
b_item_f = False

# Создать переменную b_item_relult_sum и присвоить сумму b_item_t и b_item_f
b_item_result_sum = b_item_t + b_item_f

# Вывести b_item_relult_sum в консоль.
print('b_item_result_sum = ', b_item_result_sum)

# Создать переменную b_item_relult_subtr и присвоить разницу b_item_t и b_item_f
b_item_result_subtr = b_item_t - b_item_f

# Вывести b_item_relult_subtr в консоль.
print('b_item_result_subtr = ', b_item_result_subtr)

# Создать переменную b_item_relult_multi и присвоить умножение b_item_t и b_item_f
b_item_result_multi = b_item_t * b_item_f

# Вывести b_item_relult_multi в консоль.
print('b_item_result_multi = ', b_item_result_multi)

# # Создать переменную b_item_relult_division и присвоить деление b_item_t и b_item_f
# b_item_relult_division = b_item_t / b_item_f
#
# # Вывести b_item_relult_division в консоль. (Получить ошибку)
# print('b_item_relult_division = ', b_item_relult_division)

# Создать переменную b_item_1_int и присвоить явное приведение b_item_t к int
b_item_1_int = int(b_item_t)

# Вывести b_item_1_int в консоль.
print('b_item_1_int = ', b_item_1_int)

# Создать переменную b_item_2_int и присвоить явное приведение b_item_f к int
b_item_2_int = int(b_item_f)

# Вывести b_item_2_int в консоль.
print('b_item_2_int = ', b_item_2_int)