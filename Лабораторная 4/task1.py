if __name__ == "__main__":
    # Write your solution here
    class Automobile:
        """
        Базовый класс автомобили.
                :param car_brand: марка
                :param price: цена
        """

        def __init__(self, car_brand: str, price: int):
            self._car_brand = car_brand

            if not isinstance(price, int):
                raise TypeError("price должно быть типа int")

            if price <= 0:
                raise ValueError("price должен быть положительным числом")
            self.price = price

        @property # марка машины не может поменяться, поэтому делаем непубличным
        def car_brand(self):
            return self._car_brand

        def __str__(self) -> str:
            return f"Марка {self.car_brand}. Цена {self.price}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(car_brand={self.car_brand!r}, price={self.price!r})"

        def price_change (self, change: int) -> str:
            """
            Метод определяет новую цену машины в зависимсти от величины ее изменения
            Наследуемый метод.
            :param change: показывает на сколько тыс.р. изменилась цена
            """
            if not isinstance(change, int):
                raise TypeError("change должен быть типа int")
            self.change = change
            return f"Новая цена = {self.price + change} руб."

        def car_tax (self):
            """
            Метод определяет налог на автомобиль в зависимоти от стоимости.
            Метод придуман мной, ничего общего с реальными налогами не имеет.
            Наследуемый метод.
            """
            return f"Налог = {self.price * 0.025} руб."



    class Truck(Automobile):
    """
        Дочерний класс грузовые автомобили.
        :param load_capacity: грузоподъемность
    """
        def __init__(self, car_brand: str, price: int, load_capacity: int):
            super().__init__(car_brand, price)
            self.load_capacity = load_capacity


        def __str__(self) -> str:  # перегружаем str, так как хочу видеть всю информацию о машине
            return f"Марка {self.car_brand}. Цена {self.price} тыс. Грузоподъемность {self.load_capacity}т."

        def __repr__(self) -> str:  # хочу видеть все атрибуты, поэтому перегружаем repr, так как добавляется аргумент load_capacity
            return f"{self.__class__.__name__}(car_brand={self.car_brand!r}, price={self.price!r}, load_capacity = {self.load_capacity!r})"


        def car_tax (self):
            """
            Метод определяет налог на автомобиль в зависимоти от стоимости.
            Перегружаем метод, так как для грузового транспорта другая формула для вычисления
            """
            return  f"Налог = {self.price * 0.03} руб."


    class Car(Automobile):
    """
        Дочерний класс лекговые автомобили.
        :param color: цвет
    """
        def __init__(self, car_brand: str, price: int, color: str):
            super().__init__(car_brand, price)

            if not isinstance(color, str):
                raise TypeError("color должно быть типа str")
            self.color = color

        def __str__(self) -> str:  # перегружаем str, так как хочу видеть всю информацию о машине
            return f"Марка {self.car_brand}. Цена {self.price} тыс. Цвет {self.color}."

        def __repr__(self) -> str:  # хочу видеть все атрибуты, поэтому перегружаем repr, так как добавляется аргумент color
            return f"{self.__class__.__name__}(car_brand={self.car_brand!r}, price={self.price!r}, color ={self.color!r})"


    pass
