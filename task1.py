# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union

# Найти объем куба и площадь нижней грани
class Cube:
    def __init__(self, length: Union[int, float], width: Union[int, float], height: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Куб"
        :param length: длина
        :param width: ширина
        :param height: высота
        Примеры:
        >>> cube = Cube(5, 5, 8)  # инициализация экземпляра класса
        """

        if not isinstance(length, (int, float)):
            raise TypeError("Длина должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина должна быть положительным числом")
        self.length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина должна быть типа int или float")
        if width <= 0:
            raise ValueError("Ширина должна быть положительным числом")
        self.width = width

        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        self.height = height

    def square_(self):
        """
        Метод вычисляет площадь нижней грани.
        >>> cube = Cube(5, 5, 8)
        >>> cube.square_()
        25

        """
        return self.length * self.width

    def cube_volume(self):
        """
        Метод вычисляет объем куба.
        >>> cube = Cube(5, 5, 8)
        >>> cube.cube_volume()
        200
        """
        return self.length * self.width * self.height


class Bottle:
    def __init__(self, volume: int, water_volume: int):
        """
        Создание и подготовка к работе объекта "Бутылка"
        :param volume: объем бутылки
        :param water_volume: объем воды в бутылке
        Примеры:
        >>> bottle = Bottle(5, 2)  # инициализация экземпляра класса
        """

        if not isinstance(volume, int):
            raise TypeError("Объем бутылки должен быть типа int")
        if volume <= 0:
            raise ValueError("Объем должен быть положительным числом")
        self.volume = volume

        if not isinstance(water_volume, int):
            raise TypeError("Объем воды должен быть типа int")
        if water_volume <= 0:
            raise ValueError("Объем воды должен положительным числом")
        self.water_volume = water_volume

    def add_water(self, water: int):
        """
        Метод вычисляет объем воды после добавления.
        >>> bottle = Bottle(5, 2)
        >>> bottle.add_water(5)
        """
        if not isinstance(water, int):
            raise TypeError("Объем бутылки должен быть типа int")
        if water <= 0:
            raise ValueError("Объем должен быть положительным числом")
        self.water_volume += water

    def difference_between_volumes(self):
        """
        Метод вычисляет пустой объем бутылки.
        >>> bottle = Bottle(5, 2)
        >>> bottle.difference_between_volumes()
        3
        """
        return self.volume - self.water_volume

class Cylinder:
    def __init__(self, diameter: int, height: int):
        """
        Создание и подготовка к работе объекта "Цилиндр"
        :param diametеr: диаметр
        :param height: высота цилиндра
        Примеры:
        >>> cylinder = Cylinder(5, 2)  # инициализация экземпляра класса
        """
        if not isinstance(diameter, int):
            raise TypeError("Диаметр цилиндра должен быть типа int")
        if diameter <= 0:
            raise ValueError("Диаметр цилиндра должен быть положительным числом")
        self.diameter = diameter

        if not isinstance(height, int):
            raise TypeError("Высота цилиндра должен быть типа int")
        if height <= 0:
            raise ValueError("ВЫсота цилиндра должен быть положительным числом")
        self.height = height

    def cylinder_volume(self):
        """
        Метод вычисляет объем цилиндра.
        >>> cylinder = Cylinder(5, 2)
        >>> cylinder.cylinder_volume()
        39.25
        """
        return 3.14 * (self.diameter/2) ** 2 * self.height

    def square_cylinder(self):
        """
        Метод вычисляет площадь нижней грани.
        >>> cylinder = Cylinder(5, 2)
        >>> cylinder.square_cylinder()
        19.625
        """
        return 3.14 * (self.diameter / 2) ** 2

if __name__ == "__main__":
    #TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()