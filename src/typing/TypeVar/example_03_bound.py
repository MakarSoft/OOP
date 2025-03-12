import random
from typing import TypeVar, Sequence

S = TypeVar("S", bound=str)


class MovieTitle(str):
    @property
    def featuring(self) -> str:
        return f"Now playing {self!r}"


def get_and_show_random_line(lines: Sequence[S]) -> S:
    random_line: S = random.choice(lines)
    print("chosen line:", random_line.title())
    return random_line


def main() -> None:
    elements = ["foo", "bar", "spam and eggs"]
    line = get_and_show_random_line(elements)
    print("got line:", line)

    movies = [
        MovieTitle("foo"),
        MovieTitle("fizz buzz"),
        MovieTitle("spam and eggs"),
    ]
    movie = get_and_show_random_line(movies)
    # print(reveal_type(movie))
    print("got movie:", movie.featuring)


if __name__ == "__main__":
    main()
