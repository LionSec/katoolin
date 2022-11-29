import os
from time import sleep
import curses
from typing import List, NoReturn, Callable
from apt.cache import Cache

from .arquivo_temporario import arquivo


def pegar_programas_instalaveis(funcao: Callable) -> Callable:
    """Retorna os programas que serão instalados."""
    def pegar_args(nomes):
        cache = Cache()
        cache.open()
        pacotes_brutos = map(cache.get, nomes)
        pacotes_filtrados = filter(lambda x: x, pacotes_brutos)
        nomes_dos_pacotes = map(lambda x: x.name, pacotes_filtrados)
        cache.close()
        funcao(nomes_dos_pacotes)
    return pegar_args


def limpar_tela_decorator(funcao: Callable) -> Callable:
    """Limipa a tela."""
    def pegar_args(*args):
        funcao(*args)
        tela = curses.getwin(arquivo)
        arquivo.seek(0)
        tela.clear()
        tela.refresh()
    return pegar_args


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


def mostrar_texto_tempo(tempo: int = 2) -> Callable:
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


@mostrar_texto_tempo()
def mostrar_banner() -> str:
    """Mostra um banner com o logo do katoolin."""
    with open('banner.txt') as file:
        return file.read()


def formatar_texto(itens, numero_de_linhas_faltosas = 4) -> str:
    """Formata um texto para exibir os programas instaláveis na tela."""
    linhas = os.get_terminal_size()[1] - numero_de_linhas_faltosas
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
    """Recorta uma lista."""
    return [lista[x: x + numero] for x in range(0, len(lista), numero)]


def limpar() -> NoReturn:
    """Limpa a tela."""
    tela = curses.getwin(arquivo)
    arquivo.seek(0)
    tela.clear()
    tela.refresh()


