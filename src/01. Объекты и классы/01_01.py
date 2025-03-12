import requests
from typing import Final, Generator


GOOGLE_URL: Final[str] = "https://www.google.com"
SPEC_CHARS: Final[str] = "__"


def is_dunder(attr_name: str) -> bool:
    """ """
    return attr_name.startswith(SPEC_CHARS) and attr_name.endswith(SPEC_CHARS)


def get_help(obj: object) -> Generator[tuple[str, str], None, None]:
    """ """
    for attr_name in dir(obj):
        if callable(attr := getattr(obj, attr_name)) and not is_dunder(
            attr_name
        ):
            yield attr_name, attr.__doc__.split("\n")[0]


# ==========================================================
if __name__ == "__main__":

    response: requests.models.Response = requests.get(GOOGLE_URL)

    print("=" * 60)
    for name, help in get_help(response):
        print(f"{name:<15}{help}")
