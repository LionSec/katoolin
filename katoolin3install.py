#!usr/bin/python3

from contextlib import suppress
from curses import wrapper
from typing import NoReturn

from src.main import katoolin_main
from src.ferramentas import verificar_root


def main() -> NoReturn:
    """Main function."""
    with suppress((KeyboardInterrupt, EOFError)):
        wrapper(katoolin_main)


if __name__ == '__main__':
    main()
