import os
from time import sleep
import sys
import curses
from typing import List, NoReturn, Callable

from .arquivo_temporario import arquivo


def mostrar_menus(menu: Callable, teclas: List[str]) -> str:
    """Mostra os menus e retorna uma tecla precionada."""
    tela = curses.getwin(arquivo)
    arquivo.seek(0)
    tecla = ''
    while tecla not in teclas:
        tela.erase()
        tela.addstr(menu())
        tela.refresh()
        tecla = tela.getstr().decode()
    return tecla


def _root() -> bool:
    """Verifica se o programa foi iniciado como root e o retorna um boolean."""
    return os.getuid() == 0


def mostrar(tempo: int = 2) -> Callable:
    """Mostra uma mensagem durante algum tempo."""
    def pegar_funcao(funcao):
        def pegar_tela(*args, **kwargs):
            tela = curses.getwin(arquivo)
            arquivo.seek(0)
            texto = funcao(*args, **kwargs)
            tela.erase()
            tela.addstr(texto[-79*13:])  # antigo bug. remover slice?
            tela.refresh()
            sleep(tempo)
        return pegar_tela
    return pegar_funcao


def verificar_root(tela) -> NoReturn:
    """Verifica se o programa foi iniciado como root e caso contrário, sai."""
    if not _root():
        tela.addstr('this program needs to be run with root privileges.')
        tela.refresh()
        sleep(2)
        exit(1)


@mostrar()
def mostrar_banner() -> str:
    """Mostra um banner com o logo do katoolin."""
    with open('banner.txt') as file:
        return file.read()


def formatar_texto(itens) -> str:
    """Formata um texto para exibir os programas instaláveis na tela."""
    linhas = os.get_terminal_size()[1] - 4  # - 4 linhas
    itens2 = [
        f"{numero}) {item}" for numero, item in enumerate(itens, 1)
    ]
    itens_em_partes = cortar(itens2, linhas)
    itens_formatados = []
    for lista in itens_em_partes:
        tamanho = max(map(len, lista))
        formato = f'<{tamanho}'
        itens_formatados.append(
            list(map(lambda x: format(x, formato), lista))
        )
    itens_formatados = list(map(' '.join, zip(*itens_formatados)))
    return '\n'.join(itens_formatados)


def mostrar_texto(texto: str) -> NoReturn:
    """Escreve algo na tela."""
    tela = curses.getwin(arquivo)
    arquivo.seek(0)
    tela.addstr(texto)
    tela.refresh()


def terminado() -> NoReturn:
    """Mostra uma mensagem na tela que terminou algo."""
    mostrar_texto('\nDone.')
    sleep(1)


def cortar(lista: list, numero: int) -> list[list]:
    return [lista[x: x + numero] for x in range(0, len(lista), numero)]


def limpar() -> NoReturn:
    tela = curses.getwin(arquivo)
    arquivo.seek(0)
    tela.erase()
    tela.refresh()

