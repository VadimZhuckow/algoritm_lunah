with open('Luhn.txt', 'r') as f:
    data = f.readlines()
    data2 = []
    for i in data:
        i.rstrip('\n')
        data2.append(i.rstrip('\n'))


def Luhn(card):
    # Здесь храним контрольную сумму
    checksum = 0
    # Переводим номер карточки из строки в массив чисел
    cardnumbers = list(map(int, card))
    # Проходимся по каждому числу
    for count, num in enumerate(cardnumbers):
        # Если index чётный, значит число стоит на нечётной позиции
        # Так получается потому что считаем с нуля
        if count % 2 == 0:
            buffer = num * 2
            # Если удвоенное число больше 9, то вычитаем из него 9 и прибавляем к контрольной сумме
            if buffer > 9:
                buffer -= 9
            # Если нет, то сразу прибавляем к контрольной сумме
            checksum += buffer
        # Если число стоит на чётной позиции, то прибавляем его к контрольной сумме
        else:
            checksum += num
    # Если контрольная сумма делится без остатка на 10, то номер карты правильный
    return checksum % 10 == 0


# test = ['4111111111111111',
#         '4111111111111112',
#         '4111111111111113']
#
test2 = []
for i in data2:

    if Luhn(i) == False:
        print(i)
        test2.append(i)


with open('nowalid.txt', 'w') as f:
    f.writelines(f"{item}\n" for item in test2)


