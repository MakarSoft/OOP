from typing import TypeVar, reveal_type

T = TypeVar("T", int, float)


def square(x: T) -> T:
    return x * x


def wrong_square(x: int | float) -> int | float:
    return x * x


def main() -> None:
    a = square(3)
    print(a)
    b = square(2.5)
    print(b)
    # c = square("foo")
    # print(c)
    c = wrong_square(3)
    # reveal_type(c)
    print(c, type(c))
    # d = square(MyInt(1))


if __name__ == "__main__":
    main()
