from os import getuid
from pathlib import Path
from typing import Any, Iterable

import requests


def recortar(lista: list[Any], numero: int) -> list[list[Any]]:
    return [lista[x: numero + x] for x in range(0, len(lista), numero)]


def root() -> bool:
    """Verifica se o programa foi iniciado como root."""
    return getuid() == 0


def baixar_arquivo(url: str) -> None:
    local_arquivo = Path(Path(url).name)
    if not local_arquivo.exists():
        with requests.get(url, stream=True) as requisição:
            requisição.raise_for_status()
            with local_arquivo.open('ab') as arquivo:
                for chunk in requisição.iter_content(chunk_size=8192): 
                    arquivo.write(chunk)