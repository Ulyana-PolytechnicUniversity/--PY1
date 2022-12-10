def get_random_password() -> str:
    import random
    import string

    length_password = 8
    lower_words = string.ascii_lowercase
    upper_words = string.ascii_uppercase
    numbers = string.digits

    all_simbols = lower_words + upper_words + numbers

    password = "".join(random.sample(all_simbols, length_password))

    return password

print(get_random_password())
