class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str): #В базовом классе надо сделать проверки для name и author
        if not isinstance(name, str):
            raise TypeError("name должно быть типа str")
        self.name = name

        if not isinstance(author, str):
            raise TypeError("author должно быть типа str")
        self.author = author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.valid_pages(pages)

    def __str__(self) -> str: #перегружаем str, так как добавляется аргумент pages
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"

    def __repr__(self) -> str: #перегружаем repr, так как добавляется аргумент pages
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages = {self.pages!r})"

    def valid_pages(self, pages) -> None: #проверки для pages
        if not isinstance(pages, int):
            raise TypeError("pages должно быть типа int")

        if pages <= 0:
            raise ValueError("pages должно быть положительным числом")
        self.pages = pages

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.valid_duration(duration)

    def __str__(self) -> str: #перегружаем str, так как добавляется аргумент duration
        return f"Книга {self.name}. Автор {self.author}. Длительность {self.duration}"

    def __repr__(self) -> str: #перегружаем repr, так как добавляется аргумент duration
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration ={self.duration!r})"

    def valid_duration(self, duration) -> None: #проверки для duration
        if not isinstance(duration, float):
            raise TypeError("duration должно быть типа float")

        if duration <= 0:
            raise ValueError("duration должно быть положительным числом")

        self.duration = duration

book1 = Book("Евгений онегин1", "Пушкин1")
book2 = PaperBook("Евгений онегин2", "Пушкин2", 122)
book3 = AudioBook("Евгений онегин3", "Пушкин3", 12.2)

print(book1.__repr__())
print(book2.__repr__())
print(book3.__repr__())

print(book1.__str__())
print(book2.__str__())
print(book3.__str__())
