# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

dict_ = [{"bin": bin(item),"dec": item,"hex": hex(item), "oct": oct(item)} for item in range(16)]

pprint(dict_)
