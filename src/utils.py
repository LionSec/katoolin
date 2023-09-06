from copy import deepcopy
from os import getuid
# from pathlib import Path
from typing import Any

from src.modelos import Programas

# import requests
distros = {
    'ferramentas_extras_kalilinux': 'kali linux'
}


def recortar(lista: list[Any], numero: int) -> list[list[Any]]:
    return [lista[x: numero + x] for x in range(0, len(lista), numero)]


def root() -> bool:
    """Verifica se o programa foi iniciado como root."""
    return getuid() == 0


# colocar o nome do arquivo como parâmetro.
# def baixar_arquivo(url: str) -> None:
#     local_arquivo = Path(Path(url).name)
#     if not local_arquivo.exists():
#         with requests.get(url, stream=True) as requisição:
#             requisição.raise_for_status()
#             with local_arquivo.open('ab') as arquivo:
#                 for chunk in requisição.iter_content(chunk_size=8192): 
#                     arquivo.write(chunk)


def transformar_classes_programas(
    programas: dict[str, list[str]]
) -> dict[str, list[str]]:
    """Transforma as strings de programas em classes de programas."""
    novos_programas = deepcopy(programas)
    for distro in programas:
        for categoria in programas[distro]:
            novos_programas[distro][categoria] = list(map(
                lambda pacote: Programas(
                    pacote,
                    distros.get(distro, distro)
                ),
                programas[distro][categoria]
            ))
    return novos_programas


def acrescentar_programas_extras(
    programas: dict[str, list[str]]
) -> dict[str, list[str]]:
    """Acrecenta os programas do extra no kali."""
    novos_programas = deepcopy(programas)
    for categoria in programas['kali linux']:
        for programa in programas['kali linux'][categoria]:
            if programa in programas['ferramentas_extras_kalilinux']:
                index_programa = (
                    programas['kali linux'][categoria].index(programa)
                )
                novos_programas['kali linux'][categoria].pop(index_programa)
                novos_programas['kali linux'][categoria].extend(
                    programas['ferramentas_extras_kalilinux'][programa]
                )
    del novos_programas['ferramentas_extras_kalilinux']
    return novos_programas
