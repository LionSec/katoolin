from os import remove, system, rename
from typing import NoReturn
from pathlib import Path
import curses
from shutil import move


def adicionar_repositorio(nome: str, repositorio: str) -> NoReturn:
    """Adiciona um arquivo com um novo repositório."""
    local_arquivo = f"/etc/apt/sources.list.d/{nome}.list"
    if not Path(local_arquivo).exists():
        with open(local_arquivo, 'a') as arquivo:
            linhas = f"# {nome} repository\n"
            linhas += repositorio + '\n'
            arquivo.write(linhas)


def remover_repositorio(nome: str) -> NoReturn:
    """Remove um arquivo com um repositório."""
    repositorio = f"/etc/apt/sources.list.d/{nome}.list"
    if Path(repositorio).exists():
        remove(repositorio)


def adicionar_kali_repositorio() -> NoReturn:
    """Adiciona o repositório do kali-linux."""
    nome = 'kali-linux'
    repositorio = (
        'deb http://http.kali.org/kali kali-rolling '
        'main non-free contrib'
    )
    adicionar_repositorio(nome, repositorio)


def remover_kali_repositorio() -> NoReturn:
    """Remove o repositório do kali-linux."""
    remover_repositorio('kali-linux')


def adicionar_diesch_repositorio() -> NoReturn:
    """Adiciona o repositório do diesch."""
    nome = 'diesch'
    repositorio = (
        'deb http://ppa.launchpad.net/diesch/testing/ubuntu '
        'main non-free contrib'
    )
    adicionar_repositorio(nome, repositorio)


def executar(comando: str) -> NoReturn:
    """Executa um comando shell na máquina sem exibir qualquer mensagem."""
    system(comando)


def adicionar_kali_gpg_key() -> NoReturn:
    """Adiciona uma gpg key do kali linux."""
    if not Path('/etc/apt/trusted.gpg.d/kali-linux.gpg').exists():
        curses.endwin()
        executar(
            "apt-key adv --keyserver "
            "keyserver.ubuntu.com --recv-keys ED444FF07D8D0BF6"
        )
        rename('/etc/apt/trusted.gpg', '/etc/apt/kali-linux.gpg')
        move('/etc/apt/kali-linux.gpg', '/etc/apt/trusted.gpg.d')


def remover_kali_gpg_key() -> NoReturn:
    """Remove uma gpg key do kali linux."""
    kali_gpg_key = Path('/etc/apt/trusted.gpg.d/kali-linux.gpg')
    if kali_gpg_key.exists():
        kali_gpg_key.unlink()
