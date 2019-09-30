# Имеется двумерный массив 10х2 в виде списка. Сделать консольную программу,
# которая вводит данные массива с клавиатуры, осуществляет заданый вариантом
# алгоритм и выводит получиенный список-результат на экран

import math

# Функция массива
def input_array(row, column):
    array = []
    for i in range(0, row):
        sub_array = []
        for j in range(column):
            print('Введите число [ ', i, ' ]', '[ ', j, ' ]:')
            number = int(input())
            sub_array.append(number)
        array.append(sub_array)
    return array

# Функция вывода массива
def output_array(array):
    print()
    for i in array:
        for j in i:
            print("%d\t" % j, end='')
        print('')

def main():
    array = input_array(10, 2)
    output_array(array)


if __name__ == '__main__':
    main()