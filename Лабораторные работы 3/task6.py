list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
max_index = 0 # начнем в первого элемента

for i in range(len(list_numbers)): # находим максимально последнее число
    max_number = list_numbers[max_index]
    current_num = list_numbers[i]
    if current_num >= max_number:
        max_index = i


list_numbers[max_index] = current_num  # заменяем в списке максимальное посдленее число последним числом в списке
list_numbers[len(list_numbers)-1] = max_number # заменяем последнее число максимальным последним



print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
