#!usr/bin/python3


from os import chdir
from pathlib import Path

aqui = Path(__file__).parent
chdir(aqui)

from src.comandos import sistema
from src.interface import KatoolinApp


def main() -> None:
    """Função principal."""
    app = KatoolinApp()
    app.run()


main()
