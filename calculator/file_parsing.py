import pathlib
import typing
from pathlib import Path


def read_path() -> Path:
    """ reads a path from the input"""
    return Path(input("Enter the name of the file: "))


def _generate_lines(path: Path) -> typing.Iterable[str]:
    """ opens the file and yields the lines"""
    with open(path) as file:
        yield from file

def parse_for_locations(path: Path):
    """ parses the lines and yields the addresses of each line"""
    for address in _generate_lines(path):
        address = address.strip()
        if address.lower().startswith('center') or address.lower().startswith('location') or address == "":
            pass
        else:
            yield address