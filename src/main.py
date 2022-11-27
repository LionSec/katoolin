import curses, os
from shutil import move
from apt import cache
from typing import NoReturn

from .menus import main_menu, menu_1, menu_2, menu_5
from .ferramentas import (
    mostrar_menus, verificar_root, mostrar_banner, mostrar_texto, terminado,
    limpar
)
from .comandos import (
    adicionar_kali_repositorio, remover_kali_repositorio,
    adicionar_diesch_repositorio, executar
)
from .apt_install import instalar, gerenciar_pacotes, atualizar
from .dicionarios import argumentos_pacotes
from .programas import tudo
from .arquivo_temporario import arquivo


def opcoes_menu_1(tela) -> NoReturn:
    """Mostra o submenu 1 do menu principal."""
    while True:
        opcoes = ['1','2','3','4', 'back']
        tecla = mostrar_menus(menu_1, opcoes)
        if tecla == '1':
            tela.clear()
            tela.refresh()
            adicionar_kali_repositorio()
            executar(
                "apt-key adv --keyserver "
                "keyserver.ubuntu.com --recv-keys ED444FF07D8D0BF6"
            )
            os.rename('/etc/apt/trusted.gpg', '/etc/apt/kali-linux.gpg')
            move('/etc/apt/kali-linux.gpg', '/etc/apt/trusted.gpg.d')
            tela.clear()
            tela.refresh()
        elif tecla == '2':
            mostrar_texto('wait for the command to finish running.')
            cache_ = cache.Cache()
            cache_.update()
        elif tecla == '3':
            remover_kali_repositorio()
        elif tecla == 'back':
            break
        terminado()


def opcoes_menu_2() -> NoReturn:
    """Mostra o submenu 2 do menu principal."""
    opcoes = list(map(str, range(15)))
    opcoes.append('back')
    while True:
        tecla = mostrar_menus(menu_2, opcoes)
        if tecla == '0':  # install all packages
            instalar(tudo)
            limpar()
            terminado()
        elif tecla != 'back':
            gerenciar_pacotes(*argumentos_pacotes[tecla])
        elif tecla == 'back':
            break


def opcoes_menu_principal(tela):
    while True:
        tecla = mostrar_menus(main_menu, ['1','2','3','4','5', 'exit'])
        if tecla == '1':
            opcoes_menu_1(tela)
        elif tecla == '2':
            opcoes_menu_2()
        elif tecla == '3':
            # adicionar_diesch_repositorio()
            # atualizar()
            instalar(['classicmenu-indicator'])
            limpar()
            terminado()
        elif tecla == '4':
            instalar(['kali-menu'])
            limpar()
            terminado()
        elif tecla == '5':
            menu_5()
        elif tecla == 'exit':
            exit()


def katoolin_main(tela) -> NoReturn:
    """Função principal."""
    try:
        colunas, linhas = os.get_terminal_size()
        curses.initscr()
        curses.echo()
        verificar_root(tela)
        with arquivo as arquivo_:
            tela.putwin(arquivo_)
            arquivo_.seek(0)
            mostrar_banner()
            opcoes_menu_principal(tela)
    finally:
        curses.endwin()
