def delete(list_, index=None):
     if index is None:
          list_ = list_[:-1]

     else:
          #list_ = list_[:index] + list_[index + 1:] # Способ 1. данный способ не работает с отрицательным индексом (не использую его)
          
          list_1 = list_.pop(index) # Способ 2. работает с отрицательным индексом. Использую его
          
          #del list_[index] # Способ 3. работает с отрицательным индексом (не использую его)
          
          # я выбрала способ 2 (перед ним нет знака "#")

     return list_


print(delete([0, 1, 2], index=0))  # [1, 2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
#пустая строка
