
# задача 3
# number = int(input('Введите трехзначное число: '))
# while number // 1000 > 0 :   
#     if number//1000 > 0:
#         print('Число не трехзначное')
#         number = int(input('Введите трехзначное число: '))
#
# sum = 0
# while number / 10 > 0:
#     sum = sum + number % 10
#     number //= 10
#
# print(f'Сумма цифр числа равна: {sum}')


# задача 4

# S = int(input("Введите общее количество журавликов: "))
# if not S % 6:
#      x = S // 6
#      print(f'Катя {x * 4} ')
#      print(f'Сережа {x} ')
#      print(f'Петя {x}')


# задача 6

# while True:
#     number = input('Введите шестизначный номер Вашего билета: ')
#     if number.isdigit() and len(number) == 6:
#         if sum(map(int, number[:3])) == sum(map(int, number[3:])):
#             print('Ваш билет счастливый!')
#         else:
#             print('Ваш билет не счастливый')
#         break
#     else:
#         print('Введен некорректный номер билета, попробуйте еще раз')


# задача 8


# n = int(input("Введите один размер шоколадки в дольках: "))
# m = int(input("Введите другой размер шоколадки в дольках: "))
#
# k = int(input("Введите количество долек, которое хотите отломить: "))
#
# if k < m * n and (k % m == 0 or k % n == 0):
#     print('Да')
# else:
#     print('Нет')