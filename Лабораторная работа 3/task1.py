class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str): #В базовом классе надо сделать проверки для name и author
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author


    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages(pages)

    @property
    def pages(self):
        return self.pages

    @pages.setter
    def name(self, pages):

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

    def __str__(self) -> str: #перегружаем str, так как добавляется аргумент pages
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"

    def __repr__(self) -> str: #перегружаем repr, так как добавляется аргумент pages
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages = {self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration(duration)

    def __str__(self) -> str: #перегружаем str, так как добавляется аргумент duration
        return f"Книга {self.name}. Автор {self.author}. Длительность {self.duration}"

    def __repr__(self) -> str: #перегружаем repr, так как добавляется аргумент duration
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration ={self.duration!r})"

    @property
    def duration(self):
        return self.duration

    @duration.setter
    def duration(self, duration):

        if not isinstance(duration, int):
            raise TypeError("Длительность должна быть типа int")
        if duration <= 0:
            raise ValueError("Длительность должна быть положительным числом")
        self.pages = duration



