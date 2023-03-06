def sort(array):  # сортируем
    for i in range(len(array)):  # сортировка выбором
        idx_min = i  # сохраняем индекс предположительно минимального элемента

        for j in range(i, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j
        if i != idx_min:  # если индекс не совпадает с минимальным, меняем
            array[i], array[idx_min] = array[idx_min], array[i]
    return array


def binary_search(array, element, left, right):  # ищем индексы с использованием глобальных переменных
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    global less_index
    global more_index
    middle = (right + left) // 2  # находим середину
    if element <= array[middle]:  # если элемент меньше элемента в середине
        more_index = middle
        return binary_search(array, element, left, middle - 1)
    elif element > array[middle]:  # иначе в правой
        less_index = middle
        return binary_search(array, element, middle + 1, right)
    return less_index, more_index


input_array = []  # ввод последовательности и создание списка
while not input_array:
    try:
        input_array = list(map(int, input('Inter array number '
                                          'separated by "space": ').split()))
    except ValueError:
        print('Incorrect input, please input only number.')
        input_array = []
print(f'You are inputted {input_array}')


any_number = 0
while not any_number:  # получаем число для проверки
    try:
        any_number = int(input('Input number for check in array: '))
        if any_number > max(input_array) or any_number < min(input_array):
            raise ValueError('inputted number mast be in array range!')

    except ValueError as error:
        print(error)
        print('Incorrect input, please input only number.')
        any_number = 0
print(f'You are inputted {any_number}')


sort_array = sort(input_array)  # сортируем введённый список
print(f'sorted array is: {sort_array}')

less_index = 0
more_index = 0
len_sort_array = len(sort_array)
position = binary_search(sort_array, any_number, 0, len_sort_array - 1)
if less_index == more_index:
    print('Specified number is first with index 0')
else:
    print(f'index of position less number = {less_index},'
          f' index of position more or equal number = {more_index}')