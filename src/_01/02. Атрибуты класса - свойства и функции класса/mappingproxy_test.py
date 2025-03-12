# Создаем словарь
from types import MappingProxyType

my_dict = {"a": 1, "b": 2}

# Создаем mappingproxy из словаря
proxy = MappingProxyType(my_dict)
print(type(proxy))

# Доступ к элементам через mappingproxy
print(proxy["a"])  # Вывод: 1

# Попытка изменить mappingproxy вызовет ошибку
try:
    proxy["a"] = 10
except TypeError as e:
    print(e)  # Вывод: 'mappingproxy' object does not support item assignment

# Изменяем исходный словарь
my_dict["a"] = 10

# Изменения в исходном словаре отражаются в mappingproxy
print(proxy["a"])  # Вывод: 10
