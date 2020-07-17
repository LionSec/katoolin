import apt
from typing import NoReturn, Callable, List

from .ferramentas import mostrar_menus, mostrar_texto, limpar


def atualizar_commitar_cache(funcao: Callable) -> Callable:
    """Gerencia o cache do apt."""
    def pegar_args(nomes):
        if any(nomes):
            cache = apt.cache.Cache()
            cache.open()
            funcao(nomes, cache)
            cache.commit()
            cache.close()
    return pegar_args


@atualizar_commitar_cache
def instalar(nomes: List[str], cache) -> NoReturn:
    """Instala um pacote no linux."""
    pacotes_brutos = map(cache.get, nomes)
    pacotes_filtrados = filter(lambda x: x, pacotes_brutos)
    for pacote in pacotes_filtrados:
        pacote.mark_install()


def gerenciar_pacotes(tela, menu: Callable, programas: List[str]) -> NoReturn:
    """Gerencia/instala os pacotes do linux."""
    opcoes = list(map(str, range(len(programas))))
    opcoes += ['back', 'install']
    programas = dict(zip(opcoes, programas))
    programas_para_instalar = []
    while True:
        tecla = mostrar_menus(tela, menu, opcoes)
        if tecla == '0':  # mark to install all programs
            programas_para_instalar = list(programas.values())[1:]
            break
        elif tecla == 'install':
            mostrar_texto(tela, 'wait for the command to finish running')
            mostrar_texto(tela, '\ninstalling programs...')
            instalar(programas_para_instalar)  # install programs
            limpar(tela)
        elif tecla == 'back':  # get out
            break
        else:  # mark to install a program
            programa = programas[tecla]
            programas_para_instalar.append(programa)



# don't need?
# @atualizar_commitar_cache
# def remover(nomes, cache):
#     pacotes_brutos = map(cache.get, nomes)
#     pacotes_filtrados = filter(lambda x: x, pacotes_brutos)
#     for pacote in pacotes_filtrados:
#         if pacote.is_installed:
#             pacote.mark_delete()
