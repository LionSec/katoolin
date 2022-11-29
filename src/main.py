import curses, os
from shutil import move
from typing import NoReturn

from .menus import (
    main_menu, menu_1, menu_2, menu_5
)
from .ferramentas import (
    mostrar_menus, verificar_root, mostrar_banner, mostrar_texto, terminado,
    limpar
)
from .comandos import (
    adicionar_kali_repositorio, remover_kali_repositorio,
    adicionar_diesch_repositorio, adicionar_kali_gpg_key,
    remover_kali_gpg_key
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
            adicionar_kali_repositorio()
            adicionar_kali_gpg_key()
            limpar()
        elif tecla == '2':
            mostrar_texto('wait for the command to finish running.')
            atualizar()
            limpar()
        elif tecla == '3':
            remover_kali_repositorio()
            remover_kali_gpg_key()
        elif tecla == 'back':
            break
        terminado()


def opcoes_menu_2() -> NoReturn:
    """Mostra o submenu 2 do menu principal."""
    opcoes = list(map(
        str, range(len(argumentos_pacotes) + 1)
    ))
    opcoes.append('back')
    while True:
        tecla = mostrar_menus(menu_2, opcoes)
        if tecla == '0':  # install all packages
            curses.endwin()
            print(
                'wait for the command to finish running'
                '\ninstalling programs...'
            )
            instalar(tudo)
            limpar()
            terminado()
        elif tecla.isnumeric():
            gerenciar_pacotes(*argumentos_pacotes[tecla])
        elif tecla == 'back':
            break


def opcoes_menu_principal(tela) -> NoReturn:
    """Menu principal."""
    while True:
        tecla = mostrar_menus(main_menu, ['1','2','3','4','5', 'exit'])
        if tecla == '1':
            opcoes_menu_1(tela)
        elif tecla == '2':
            opcoes_menu_2()
        elif tecla == '3':
            # adicionar_diesch_repositorio()
            # atualizar()
            instalar({'classicmenu-indicator'})
            limpar()
            terminado()
        elif tecla == '4':
            instalar({'kali-menu'})
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
