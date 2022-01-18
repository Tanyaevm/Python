

print('Введите валюту, из которой будет перевод: usd, eur, rub, byn')
valuta_is = input()
print('Ваша валюта - ', valuta_is)

print('Введите сумму')
sum_val = input()
print('Сумма = ', sum_val)

print('Введите в какую валюту будет перевод: usd, eur, rub, byn')
valuta_v = input()
print('Итоговая валюта - ', valuta_v)

usd_item = 'usd'
eur_item = 'eur'
rub_item = 'rub'
byn_item = 'byn'


#из бел.р. в другие валюты
if valuta_is == byn_item:
    if valuta_v == rub_item:
        a = int(sum_val) * 29.47
        print('rub = ', a)
    elif valuta_v == eur_item:
        b = int(sum_val) * 0.34
        print('eur = ', b)
    elif valuta_v == usd_item:
        c = int(sum_val) * 0.39
        print('usd = ', c)
    elif valuta_v == byn_item:
        d = int(sum_val) * 1
        print('byn = ', d)

#из баксов в другие валюты
elif valuta_is == usd_item:
    if valuta_v == rub_item:
        a_1 = int(sum_val) * 76.19
        print('rub = ', a_1)
    elif valuta_v == byn_item:
        b_1 = int(sum_val) * 2.59
        print('byn = ', b_1)
    elif valuta_v == eur_item:
        c_1 = int(sum_val) * 0.88
        print('eur = ', c_1)
    elif valuta_v == usd_item:
        d_1 = int(sum_val) * 1
        print('usd = ', d_1)

#из евро в другие валюты
elif valuta_is == eur_item:
    if valuta_v == byn_item:
        a_2 = int(sum_val) * 2.95
        print('byn = ', a_2)
    elif valuta_v == rub_item:
        b_2 = int(sum_val) * 86.83
        print('rub = ', b_2)
    elif valuta_v == usd_item:
        c_2 = int(sum_val) * 1.14
        print('usd = ', c_2)
    elif valuta_v == eur_item:
        d_2 = int(sum_val) * 1
        print('eur = ', d_2)

#из рос р в другие валюты
elif valuta_is == rub_item:
    if valuta_v == byn_item:
        a_3 = int(sum_val) * 0.034
        print('byn = ', a_3)
    elif valuta_v == usd_item:
        b_3 = int(sum_val) * 0.013
        print('usd = ', b_3)
    elif valuta_v == eur_item:
        c_3 = int(sum_val) * 0.012
        print('eur = ', c_3)
    elif valuta_v == rub_item:
        d_3 = int(sum_val) * 1
        print('rub = ', d_3)

else:
    print('Произошла ошибка')


