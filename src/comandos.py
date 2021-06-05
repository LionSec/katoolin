from subprocess import Popen
from os import devnull, remove
from typing import NoReturn

from os.path import exists


def adicionar_repositorio(nome: str, repositorio: str) -> NoReturn:
    """Adiciona um arquivo com um novo repositório."""
    nome = nome.replace(' ', '_')
    local_arquivo = f"/etc/apt/sources.list.d/{nome}.list"
    if not exists(local_arquivo):
        with open(local_arquivo, 'a') as arquivo:
            linhas = f"# Repositório {nome}\n"
            linhas += repositorio + '\n'
            arquivo.write(linhas)


def remover_repositorio(nome: str) -> NoReturn:
    """Remove um arquivo com um repositório."""
    nome = nome.replace(' ', '_')
    repositorio = f"/etc/apt/sources.list.d/{nome}.list"
    if exists(repositorio):
        remove(repositorio)


def adicionar_kali_repositorio() -> NoReturn:
    """Adiciona o repositório do kali-linux."""
    nome = 'kali linux'
    repositorio = (
        'deb http://http.kali.org/kali kali-rolling '
        'main non-free contrib'
    )
    adicionar_repositorio(nome, repositorio)


def remover_kali_repositorio() -> NoReturn:
    """Remove o repositório do kali-linux."""
    remover_repositorio('kali linux')


def adicionar_diesch_repositorio() -> NoReturn:
    """Adiciona o repositório do diesch."""
    nome = 'diesch'
    repositorio = (
        'deb http://ppa.launchpad.net/diesch/testing/ubuntu '
        'main non-free contrib'
    )
    adicionar_repositorio(nome, repositorio)


add_apt_key = (
    "apt-key adv --keyserver hkp://keys.gnupg.net --recv-keys 7D8D0BF6"
)


def executar(string: str) -> NoReturn:
    """Executa um comando shell na máquina sem exibir qualquer mensagem."""
    Popen(
        string.split(), stdout=open(devnull, 'w'),
        stderr=open(devnull, 'w')
    )
