list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_index = 0   # начнем в первого элемента
current_num = 0
max_number = 0

for i, current_num in enumerate(list_numbers):  # перебераем все пары индексы-значение
    max_number = list_numbers[max_index]

    if current_num >= max_number: # если текущее число больше того, которое встречали ранее
        max_index = i # то перезаписываем индекс максимального числа


list_numbers[max_index], list_numbers[len(list_numbers)-1] = current_num, max_number   # зпменяем значения


print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
