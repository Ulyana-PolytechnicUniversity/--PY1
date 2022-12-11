from random import sample
from string import ascii_lowercase, ascii_uppercase, digits

def get_random_password(n) -> str:  #n-количество символов в пароле

    password = "".join(sample(ascii_lowercase + ascii_uppercase + digits, n))

    return password


print(get_random_password(8))
