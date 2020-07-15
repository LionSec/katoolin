from os import devnull, remove
from os.path import exists
from subprocess import Popen


def adicionar_repositorio(nome, repositorio):
    local_arquivo = f"/etc/apt/sources.list.d/{nome}.list"
    if not exists(local_arquivo):
        with open(local_arquivo, 'a') as arquivo:
            linhas = f"# Repositório {nome}\n"
            linhas += repositorio + '\n'
            arquivo.write(linhas)


def remover_repositorio(nome):
    repositorio = f"/etc/apt/sources.list.d/{nome}.list"
    if exists(repositorio):
        remove(repositorio)


def adicionar_kali_repositorio():
    nome = 'kali linux'
    repositorio = (
        'deb http://http.kali.org/kali kali-rolling '
        'main non-free contrib'
    )
    adicionar_repositorio(nome, repositorio)


def remover_kali_repositorio():
    remover_repositorio('kali linux')


def adicionar_diesch_repositorio():
    nome = 'diesch'
    repositorio = (
        'deb http://ppa.launchpad.net/diesch/testing/ubuntu '
        'main non-free contrib'
    )
    adicionar_repositorio(nome, repositorio)


add_apt_key = (
    "apt-key adv --keyserver hkp://keys.gnupg.net --recv-keys 7D8D0BF6"
)


def executar(string):
    # print('press enter after the command runs\n')
    Popen(
        string.split(), stdout=open(devnull, 'w'),
        stderr=open(devnull, 'w')
    )
