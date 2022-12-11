from random import randint
def get_unique_list_numbers(a, b, n) -> list[int]:
#a-нижний предел дапазона b-верхний предел диапазона n-количество чисел
    numbers = []

    while len(numbers) < n:
        num = randint(a, b)
        if num not in numbers:
            numbers.append(num)
    return numbers

list_unique_numbers = get_unique_list_numbers(-10, 10, 15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
