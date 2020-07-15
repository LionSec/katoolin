import os
from time import sleep
import sys


def mostrar_menus(tela, menu, teclas):
    tecla = ''
    while tecla not in teclas:
        tela.erase()
        tela.addstr(menu())
        tela.refresh()
        tecla = tela.getstr().decode()
    return tecla


def _root():
    return os.getuid() == 0


def mostrar(tempo=2):
    def pegar_funcao(funcao):
        def pegar_tela(tela):
            texto = funcao(tela)
            tela.erase()
            tela.addstr(texto[-79*13:])
            tela.refresh()
            sleep(tempo)
        return pegar_tela
    return pegar_funcao


def verificar_root(tela):
    if not _root():
        tela.addstr('this program needs to be run with root privileges.')
        tela.refresh()
        sleep(2)
        exit(1)


@mostrar()
def mostrar_banner(tela):
    with open('banner.txt') as file:
        return file.read()


def formatar_texto(itens):
    linhas = os.get_terminal_size()[1]
    itens2 = [
        f"{numero}) {item}" for numero, item in enumerate(itens)
    ]
    return ' - '.join(itens2)


def mostrar_texto(tela, texto):
    tela.addstr(texto)
    tela.refresh()


def terminado(tela):
    mostrar_texto(tela, '\nDone.')
    sleep(1)


# def bloquear_print():
#     sys.stderr = open(os.devnull, 'w')
#     sys.stdout = open(os.devnull, 'w')
#
#
# def desbloquear_print():
#     sys.stderr.close()
#     sys.stdout.close()
#     sys.stderr = sys.__stderr__
#     sys.stdout = sys.__stdout__
