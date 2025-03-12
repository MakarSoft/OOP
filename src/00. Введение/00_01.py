import requests
from typing import Final


GOOGLE_URL: Final[str] = 'https://www.google.com'
SPEC_CHARS: Final[str] = '__'
SKIP: Final[bool] = True

response: requests.models.Response = requests.get(GOOGLE_URL)
print(type(response))
print(response)
print('-'*50)

attrs = dir(response)
print(attrs)
print('-'*50)

for attr in attrs:
    if SKIP and attr.startswith(SPEC_CHARS) and attr.endswith(SPEC_CHARS):
        continue
    print(f'{attr:<25} : {type(getattr(response, attr))}')


# Лирическое отступление насчет type hinting
# --------------------------------------------------------------
# Начиная с Python 3.8 функция подсказки типов (type hinting)
# (воплощенная модулем typing) будет поддерживать пометку имен как
# final qualifier to typing (Final).
# PEP 591 – Adding a final qualifier to typing.
#
# Это означает, что модуль typing получает два новых объекта:
# Конструкция typing.Final
#   https://docs.python.org/3.8/library/typing.html#typing.Final
# Декоратор @typing.final()​
#   https://docs.python.org/3.8/library/typing.html#typing.final

# Вышеупомянутые объекты не меняют работу Python, эти конструкции,
# которые просто документируют, что объект или ссылку следует считать
# окончательными.
# Их использование заключается в использовании средства проверки подсказок
# типа, такого как mypy, для проверки того, что ваш проект правильно
# обрабатывает объекты, задокументированные таким образом, как окончательные.
# Используем объект typing.Final, чтобы пометить глобальный атрибут или
# атрибут как окончательный, документируя таким образом, что значение никогда
# не изменится после присвоения:
#
# GLOBAL_CONSTANT: Final[str] = "This is a constant value because it is final"

# Пример...
# ------------------------------------------
#
# from typing import final, Final
#
# # FOO is marked final, can't assign another value to it
# FOO: Final[int] = 42
#
# class Foo:
#     @final
#     def spam(self) -> int:
#         """A final method can't be overridden in a subclass"""
#         return 42
#
# @final
# class Bar:
#     """A final class can't be subclassed"""
#
# # Rule breaking section
# FOO = 81
#
# class Spam(Foo, Bar):
#     def spam(self) -> int:
#         return 17
#
# if __name__ == '__main__':
#     print("FOO:", FOO)
#     print("Spam().spam():", Spam().spam())
#
# ============================================================
# $ python demo.py   # Python will not throw errors here
# FOO: 81
# Spam().spam(): 17
#
# $ mypy demo.py        # only a type checker will
# demo.py:17: error: Cannot assign to final name "FOO"
# demo.py:19: error: Cannot inherit from final class "Bar"
# demo.py:20: error: Cannot override final attribute "spam" (previously
#   declared in base class "Foo")
