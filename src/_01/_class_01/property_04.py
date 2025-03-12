from typing import Callable, Optional, TypeVar

T = TypeVar('T')


class MyProperty:
    def __init__(
        self,
        fget: Optional[Callable[['MyProperty'], T]] = None,
        fset: Optional[Callable[['MyProperty', T], None]] = None
    ) -> None:
        self.fget = fget
        self.fset = fset

    def __get__(self, instance: Optional['MyProperty'], owner: Optional[type] = None) -> Optional[T]:
        if self.fget is not None:
            return self.fget(instance)
        return None

    def __set__(self, instance: 'MyProperty', value: T) -> None:
        if self.fset is not None:
            return self.fset(instance, value)
        raise AttributeError("can't set attribute")

    def setter(self, fset: Callable[['MyProperty', T], None]) -> 'MyProperty':
        self.fset = fset
        return self

# Пример использования
class Person:
    def __init__(self, name: str) -> None:
        self._name: str = name

    @MyProperty
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("Имя должно быть строкой")
        self._name = value

# Использование
p = Person("Alice")
print(p.name)  # Вывод: Alice
p.name = "Bob"
print(p.name)  # Вывод: Bob

try:
    p.name = 123  # Это вызовет ValueError
except ValueError as e:
    print(e)  # Вывод: Имя должно быть строкой
