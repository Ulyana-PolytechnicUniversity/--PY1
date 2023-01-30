BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    """ Класс, описывающий объект Книга """

    def __init__(self, id_: int, name: str, pages: int):

        if not isinstance(id_, int):
            raise TypeError("id_ должно быть типа int")

        if id_ <= 0:
            raise ValueError("id должен быть положительным числом")

        self.id = id_

        if not isinstance(name, str):
            raise TypeError("name должно быть типа int")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("pages должен быть положительным числом")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})'


# TODO написать класс Library

class Library:
    """ Класс, описывающий объект Библиотека """
    
    def __init__(self, books=[]):

        self.books = books

    def get_next_book_id(self) -> int:
        if self.books == []:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, id_new: int) -> int:
        if not isinstance(id_new, int):
            raise TypeError("id_new должен быть типа int")
        if id_new <= 0:
            raise ValueError("id_new должен быть положительным числом")
        self.id_new = id_new

        for ind, el in enumerate(self.books):
            index = None
            if el.id == id_new:
                return ind

        if index == None:
             raise ValueError("Книги с запрашиваемым id не существует")





if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
