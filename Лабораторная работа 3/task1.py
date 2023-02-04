class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str): #В базовом классе надо сделать проверки для name и author
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author


    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> str:
        return self._pages

    @pages.setter
    def pages(self, new_pages) -> None:

        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages

    def __str__(self) -> str: #хочу видеть всю информацию о книге, поэтому перегружаем str, так как добавляется аргумент pages
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"

    def __repr__(self) -> str: #хочу видеть всю информацию о книге, поэтому перегружаем repr, так как добавляется аргумент pages
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages = {self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self) -> str: #хочу видеть всю информацию о книге, поэтому перегружаем str, так как добавляется аргумент duration
        return f"Книга {self.name}. Автор {self.author}. Длительность {self.duration}"

    def __repr__(self) -> str: #хочу видеть всю информацию о книге, поэтому перегружаем repr, так как добавляется аргумент duration
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration ={self.duration!r})"

    @property
    def duration(self) -> str:
        return self._duration

    @duration.setter
    def duration(self, new_duration) -> None:

        if not isinstance(new_duration, float):
            raise TypeError("Длительность должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Длительность должна быть положительным числом")
        self._duration = new_duration
        
