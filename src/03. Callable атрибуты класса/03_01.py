import inspect

from typing import Any
from types import FunctionType, MethodType
from pprint import pprint


class Foo:
    def bar(self):
        pass

    def baz(self):
        pass


# =====================


def methods_1(cls: type) -> list[str]:
    return [
        name
        for name, val in cls.__dict__.items()
        if isinstance(val, MethodType)  # or isinstance(val, FunctionType)
    ]


def methods_2(cls: type) -> list[str]:
    return [
        name
        for name, val in cls.__dict__.items()
        if isinstance(val, FunctionType)
    ]


def methods_3(cls: type) -> list[str]:
    return [
        name
        for name in dir(Foo)
        if callable(getattr(cls, name))
    ]


def methods_4(cls: type) -> list[str]:
    return [
        (name, getattr(cls, name))
        for name in dir(Foo)
    ]


pprint(methods_1(Foo))
print()
pprint(methods_2(Foo))
print()
pprint(methods_3(Foo))
print()

pprint(methods_4(Foo))
print()
# ---------------------
method_list: list[str] = []
for attribute in dir(Foo):
    # Get the attribute value
    attribute_value = getattr(Foo, attribute)
    # Check that it is callable
    if callable(attribute_value):
        # Filter all dunder (__ prefix) methods
        if not attribute.startswith("__"):
            method_list.append(attribute)
pprint(method_list)
print()

# -----------------------

inspected_list: list[tuple[str, Any]] = inspect.getmembers(
    Foo, predicate=inspect.ismethod
)
pprint(inspected_list)
print()

inspected_list = inspect.getmembers(Foo, predicate=inspect.isfunction)
pprint(inspected_list)
print()

methods_list = [func for func in dir(Foo) if callable(getattr(Foo, func))]
pprint(methods_list)

# ---------------------
