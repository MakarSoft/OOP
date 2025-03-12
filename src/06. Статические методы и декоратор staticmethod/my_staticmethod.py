class MyStaticMethod:
    # Дескриптор, который принимает функцию в своем конструкторе (__init__).
    # Метод __get__ возвращает саму функцию, не привязывая ее к
    # экземпляру класса (instance).

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        # Возвращаем функцию, не привязывая ее к экземпляру
        return self.func


# Используем наш декоратор
def staticmethod(func):
    return MyStaticMethod(func)


# Пример использования
class MyClass:
    @staticmethod
    def my_static_method(x, y):
        return x + y


# # Или используем наш дескриптор как декоратор
# class MyClass:
#     @MyStaticMethod
#     def my_static_method(x, y):
#         return x + y


# Вызов статического метода
result = MyClass.my_static_method(5, 10)
print(result)  # Output: 15

# Также можно вызвать статический метод на экземпляре класса
obj = MyClass()
result_instance = obj.my_static_method(3, 7)
print(result_instance)  # Output: 10


# ---------------------------------------------
# Метод __get__ в Python является частью механизма дескрипторов.
# Дескрипторы — это объекты, которые управляют доступом к атрибутам
# других объектов. Метод __get__ вызывается, когда атрибут,
# связанный с дескриптором, запрашивается у объекта.
#
# ### Основные моменты о методе __get__:
#
# 1. Синтаксис:
#    Метод __get__ имеет следующий синтаксис:
#    def __get__(self, instance, owner):
#        # Логика получения значения
#
#    - self: ссылка на сам дескриптор.
#    - instance: экземпляр класса, из которого запрашивается атрибут.
#       Если атрибут запрашивается у класса, а не у экземпляра, то `instance`
#       будет равен `None`.
#    - owner: класс, которому принадлежит дескриптор.
#
# 2. Пример использования:
#    Давайте рассмотрим пример, чтобы лучше понять, как работает __get__:
#
#    class Descriptor:
#        def __get__(self, instance, owner):
#            return f"Called __get__ on {owner.__name__} with instance {instance}"
#
#    class MyClass:
#        attr = Descriptor()
#
#    obj = MyClass()
#
#    print(obj.attr)
#    # Вывод: Called __get__ on MyClass with instance <__main__.MyClass object at 0x...>
#
#    print(MyClass.attr)
#    # Вывод: Called __get__ on MyClass with instance None

# 3. Использование дескрипторов:
#    Дескрипторы могут использоваться для различных целей, таких как:
#    - Управление доступом к атрибутам (например, для реализации свойств).
#    - Валидация данных при установке значений.
#    - Логирование доступа к атрибутам.
#
# 4. Другие методы дескрипторов:
#    Кроме __get__, дескрипторы могут также реализовывать методы
#    __set__ и __delete__, которые управляют установкой и удалением
#    значений соответственно.
#
# ### Пример с __set__ и __delete__:
#
# class Descriptor:
#     def __get__(self, instance, owner):
#         return f"Getting value from {owner.__name__}"
#
#     def __set__(self, instance, value):
#         print(f"Setting value to {value} in {instance}")
#
#     def __delete__(self, instance):
#         print(f"Deleting value from {instance}")
#
# class MyClass:
#     attr = Descriptor()
#
# obj = MyClass()
# print(obj.attr)  # Вывод: Getting value from MyClass
# obj.attr = 42    # Вывод: Setting value to 42 in <__main__.MyClass object at 0x...>
# del obj.attr     # Вывод: Deleting value from <__main__.MyClass object at 0x...>
#
# Таким образом, метод `__get__` является важной частью механизма дескрипторов в Python и позволяет управлять доступом к атрибутам объектов.
