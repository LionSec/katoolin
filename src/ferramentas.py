import os
from time import sleep

from .apt_install import instalar


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


def gerenciar_pacotes(tela, menu, programas):
    opcoes = list(map(str, range(len(programas))))
    opcoes.append('back')
    programas = dict(zip(opcoes, programas))
    programas_para_instalar = []
    while True:
        tecla = mostrar_menus(tela, menu, opcoes)
        if tecla == '0':  # mark to install all programs
            programas_para_instalar = list(programas.values()[1:])
            break
        if tecla == 'back':  # get out
            break
        else:  # mark to install a program
            programa = programas[tecla]
            programas_para_instalar.append(programa)
    mostrar_texto(tela, 'wait for the command to finish running')
    instalar(programas_para_instalar)  # install programs
