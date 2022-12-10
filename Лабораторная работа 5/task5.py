from random import sample
from string import ascii_lowercase
from string import ascii_uppercase
from string import digits

def get_random_password(a) -> str:

    lower_words = ascii_lowercase
    upper_words = ascii_uppercase
    numbers = digits

    password = "".join(sample(lower_words + upper_words + numbers, a))

    return password


print(get_random_password(8))
