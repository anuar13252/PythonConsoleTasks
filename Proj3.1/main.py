# Имеется двумерный массив 4x5 в виде списка. Сделать консольную программу,
# которая вводит данные массива с  клавиатуры, осуществляет заданный вариантом
# алгоритм и выводит полученный список - результат на экран.
# Если минимальный элемент стоит во втором столбце, то заменить элементы этого
# столбца нулями.

# Функция ввода массива
def input_array(row, column):
    array = []
    for i in range(0, row):
        sub_array = []
        for j in range(column):
            number = int(input('Введите число:\t'))
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

# Нахождение минимального элемента
def search_minEl(min_eL, array):
    for i in array:
        for j in i:
            if min_eL > j:
                min_eL = j
    return min_eL 

# Выполнение условия задачи
def solve_task(array, min_elem):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][1] == min_elem:
                for i in range(len(array)):
                    for j in range(len(array[i])):
                        array[i][1] = 0
    return array


def main():
    array = input_array(4, 5)
    output_array(array)
    # Задаем мин элемент
    min_elem = array[0][0]
    # Находим мин элемент в массиве
    min_elem = search_minEl(min_elem, array)
    array = solve_task(array, min_elem)
    output_array(array)

if __name__ == '__main__':
    main()