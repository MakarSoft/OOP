from typing import TypeVar, Sequence

T = TypeVar("T")


def repeat(val: T, times: int) -> list[T]:
    return [val] * times


def get_first_element(items: Sequence[T]) -> T:
    if items:
        return items[0]
    raise ValueError("items is empty")


def save(item: T) -> T:
    print("saved items", item)
    return item


def main() -> None:
    values = repeat(7, 3)
    lines = repeat("spam and eggs", 2)
    print("values:", values)
    print("lines:", lines)

    # for line in lines:
    #     print(line.title())
    #
    # for value in values:
    #     print(value.bit_count())

    value = get_first_element(values)
    print("value:", value)
    line = get_first_element(lines)
    print("line:", line.title())

    saved_line = save(line)
    print("saved line:", saved_line)


if __name__ == "__main__":
    main()
