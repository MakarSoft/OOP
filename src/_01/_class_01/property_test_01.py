from typing import Callable, Optional, TypeVar, Any, Type

# Определяем обобщенный тип для экземпляра класса
T = TypeVar('T')

class MyProperty:
    def __init__(self, fget: Optional[Callable[[T], Any]] = None,
                 fset: Optional[Callable[[T, Any], None]] = None,
                 fdel: Optional[Callable[[T], None]] = None) -> None:
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance: Optional[T], owner: Type) -> Any:
        if self.fget is None:
            raise AttributeError("Не определен метод получения значения.")
        return self.fget(instance)

    def __set__(self, instance: T, value: Any) -> None:
        if self.fset is None:
            raise AttributeError("Не определен метод установки значения.")
        return self.fset(instance, value)

    def __delete__(self, instance: T) -> None:
        if self.fdel is None:
            raise AttributeError("Не определен метод удаления значения.")
        return self.fdel(instance)

    @classmethod
    def setter(cls, fset: Callable[[T, Any], None]) -> 'MyProperty':
        """Метод для установки сеттера."""
        cls.fset = fset
        return cls

    @classmethod
    def deleter(cls, fdel: Callable[[T], None]) -> 'MyProperty':
        """Метод для установки делеттера."""
        cls.fdel = fdel
        return cls

class Circle:
    def __init__(self, radius: float) -> None:
        self._radius: float = radius

    @MyProperty
    def radius(self) -> float:
        """Геттер для радиуса."""
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        """Сеттер для радиуса с проверкой."""
        if value < 0:
            raise ValueError("Радиус не может быть отрицательным.")
        self._radius = value

    @MyProperty
    def area(self) -> float:
        """Вычисление площади круга."""
        import math
        return math.pi * (self._radius ** 2)

# Пример использования
circle = Circle(5.0)
print(circle.radius)  # Получение радиуса
print(circle.area)    # Получение площади

circle.radius = 10.0  # Установка нового радиуса
print(circle.area)    # Площадь с новым радиусом

# circle.radius = -5  # Это вызовет ValueError
