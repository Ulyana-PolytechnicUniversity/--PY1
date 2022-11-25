list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
max_index = 0 # начнем в первого элемента
current_num = 0  # пусть изначально тикущее и максимальное равно 0
max_number = 0

for i in range(len(list_numbers)): # перебераем индексы
    max_number = list_numbers[max_index]
    current_num = list_numbers[i]
    if current_num >= max_number:  # если текущее число больше или равно тому, которое встречали ранее
        max_index = i  # то перезаписываем индекс максимального числа


list_numbers[max_index] = current_num  # заменяем в списке максимальное последенее число последним числом в списке
list_numbers[len(list_numbers)-1] = max_number # заменяем последнее число максимальным последним



print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
