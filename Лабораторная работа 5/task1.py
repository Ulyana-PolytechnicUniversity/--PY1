# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
grades_list = range(16)

graders_dict = []

#for val in grades_list:
    #key = ["bin", "dec", "hex", "oct"]
    #values = [bin(val), val, hex(val), oct(val)]
    #graders_dict.append(dict(zip(key, values)))


graders_dict = [dict(zip(["bin", "dec", "hex", "oct"], [bin(val), val, hex(val), oct(val)])) for val in grades_list]

pprint(graders_dict)

