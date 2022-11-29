#!usr/bin/python3


from contextlib import suppress
from curses import wrapper
from typing import NoReturn
from pathlib import Path
from os import chdir


try:
    from .src.main import katoolin_main
    from .src.ferramentas import verificar_root
except ImportError:
    from src.main import katoolin_main
    from src.ferramentas import verificar_root


def main() -> NoReturn:
    """Função principal."""
    aqui = Path(__file__).parent
    chdir(aqui)
    with suppress((KeyboardInterrupt, EOFError)):
        wrapper(katoolin_main)


if __name__ == '__main__':
    main()
