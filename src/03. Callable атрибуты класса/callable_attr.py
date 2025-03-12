import inspect

from typing import Any, Callable, Optional, ParamSpec, TypeVar
from functools import wraps

T = TypeVar('T')
P = ParamSpec('P')


class Foo:
    ''' Супер класс '''

    def bar(*args):
        ''' bar '''
        pass

    def fiz(*args):
        ''' fiz '''
        pass


def view(func: Callable[P, T]) -> Callable[P, T]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        print()
        res = func(*args, **kwargs)
        print(res)
    return wrapper


@view
def get_members(
    obj: object,
    predicate: Optional[Callable[[Any], bool]]
) -> list[tuple[str, Any]]:

    inspected_list = inspect.getmembers(obj, predicate)

    return inspected_list


if __name__ == "__main__":
    class_members = get_members(Foo, inspect.isfunction)

    f = Foo()
    instance_members = get_members(f, inspect.ismethod)
