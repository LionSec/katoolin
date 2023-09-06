#!usr/bin/python3


from argparse import ArgumentParser
from os import chdir
from pathlib import Path

aqui = Path(__file__).parent
chdir(aqui)

from src.comandos import sistema
from src.interface import KatoolinApp


def main() -> None:
    """Função principal."""
    descricao = 'Installs various hacking tools from various repositories.'
    usagem = (
        'sudo ./katoolin3 or [poetry shell] sudo `which python3` katoolin3.py'
    )
    parser = ArgumentParser(
        usage = usagem, description = descricao
    )
    parser.add_argument(
        '-t', '--teste', action = 'store_true',
        help = (
            'This option is just for development. don\'t use it.'
        )
    )
    argumentos = parser.parse_args()
    app = KatoolinApp(argumentos)
    app.run()


main()


# TODO: usar o rich aqui.
