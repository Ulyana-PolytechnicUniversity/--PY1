def delete(list_, index=None):
     if index is None:
          list_1 = list_[:-1]

     else:
          list_1 = list_[:index]
          list_2 = list_[index + 1:]
          list_1.extend(list_2)

     return list_1


print(delete([0, 1, 2], index=0))  # [1, 2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
#пустая строка