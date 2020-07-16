import curses, os
from apt import cache
from typing import NoReturn

from .menus import main_menu, menu_1, menu_2
from .ferramentas import (
    mostrar_menus, verificar_root, mostrar_banner, mostrar_texto, terminado
)
from .comandos import (
    adicionar_kali_repositorio, remover_kali_repositorio,
    adicionar_diesch_repositorio, executar, add_apt_key
)
from .apt_install import instalar, gerenciar_pacotes
from .dicionarios import argumentos_pacotes
from .programas import tudo


def opcoes_menu_1(tela) -> NoReturn:
    """Mostra o submenu 1 do menu principal."""
    while True:
        opcoes = ['1','2','3','4', 'back']
        tecla = mostrar_menus(tela, menu_1, opcoes)
        if tecla == '1':
            adicionar_kali_repositorio()
            executar(add_apt_key)
            terminado(tela)
        elif tecla == '2':
            mostrar_texto(tela, 'wait for the command to finish running.')
            cache_ = cache.Cache()
            cache_.update()
            terminado(tela)
        elif tecla == '3':
            remover_kali_repositorio()
            terminado(tela)
        elif tecla == 'back':
            break


def opcoes_menu_2(tela) -> NoReturn:
    """Mostra o submenu 2 do menu principal."""
    opcoes = list(map(str, range(15)))
    opcoes.append('back')
    while True:
        tecla = mostrar_menus(tela, menu_2, opcoes)
        if tecla == '0':  # install all packages
            instalar(tudo)
        elif tecla != 'back':
            gerenciar_pacotes(tela, *argumentos_pacotes[tecla])
        elif tecla == 'back':
            break
        tela.erase()
        tela.refresh()
        terminado(tela)


def katoolin_main(tela) -> NoReturn:
    """Função principal."""
    try:
        colunas, linhas = os.get_terminal_size()
        curses.initscr()
        curses.echo()
        verificar_root(tela)
        mostrar_banner(tela)
        while True:
            tecla = mostrar_menus(tela, main_menu, ['1','2','3','4','5'])
            if tecla == '1':
                opcoes_menu_1(tela)
            elif tecla == '2':
                opcoes_menu_2(tela)
            elif tecla == '3':
                adicionar_diesch_repositorio()
                cache_ = cache.Cache()
                cache_.update()
                instalar('classicmenu-indicator')
                terminado(tela)
            elif tecla == '4':
                instalar('kali-menu')
                terminado(tela)
            elif tecla == '5':
                pass
            elif tecla == 'back':
                pass
    finally:
        curses.endwin()
