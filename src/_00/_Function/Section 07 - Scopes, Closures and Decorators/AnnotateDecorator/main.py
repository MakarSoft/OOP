# https://gist.github.com/mahenzon/c5372caa6b817871185eeb9a6e80f42c

import logging
from functools import wraps
from typing import Callable, Sized, ParamSpec, TypeVar

from common import configure_logging


log = logging.getLogger(__name__)


T = TypeVar("T")
P = ParamSpec("P")


def trace(func: Callable[P, T]) -> Callable[P, T]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        log.info(
            "call %r with args %s and kwargs %s",
            func.__name__,
            args,
            kwargs,
        )
        result = func(*args, **kwargs)
        log.info("result %r", result)
        return result

    return wrapper


@trace
def square(num: int) -> int:
    return num * num


@trace
def square_root(num: float) -> float:
    res: float = num**0.5
    return res


@trace
def get_size(value: Sized) -> int:
    return len(value)


@trace
def power(num: float, exponent: float) -> float:
    res: float = num**exponent
    return res


def main() -> None:
    configure_logging()
    log.info("sq 10 = %s", square(10))
    log.info("root 100 = %s", square_root(100))
    values = {"foo", "bar", "baz"}
    log.info("size of %s = %s", values, get_size(values))


if __name__ == "__main__":
    main()
