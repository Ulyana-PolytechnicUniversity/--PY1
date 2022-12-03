def delete(list_, index=None):

     if index is None or index == -1:
          list_ = list_[:-1]

     else:
          list_ = list_[:index] + list_[index + 1:] 
          
     
     return list_


print(delete([0, 1, 2], index=0))  # [1, 2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
#пустая строка
