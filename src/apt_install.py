import apt


def atualizar_commitar_cache(funcao):
    def pegar_args(*argumentos, **kwargumentos):
        cache = apt.cache.Cache()
        cache.open()
        funcao(*argumentos, cache, **kwargumentos)
        cache.commit()
        cache.close()
    return pegar_args


@atualizar_commitar_cache
def instalar(nomes, cache):
    pacotes_brutos = map(cache.get, nomes)
    pacotes_filtrados = filter(lambda x: x, pacotes_brutos)
    for pacote in pacotes_filtrados:
        if not pacote.is_installed:
            pacote.mark_install()


# don't need?
# @atualizar_commitar_cache
# def remover(nomes, cache):
#     pacotes_brutos = map(cache.get, nomes)
#     pacotes_filtrados = filter(lambda x: x, pacotes_brutos)
#     for pacote in pacotes_filtrados:
#         if pacote.is_installed:
#             pacote.mark_delete()
