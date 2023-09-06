from pathlib import Path
from configparser import ConfigParser


def ler_configurações() -> ConfigParser:
    """Carrega e retorna as configurações de comandos."""
    config = ConfigParser()
    config.read('configuração.ini')
    return config

configurações = ler_configurações()
local_arquivo_sistema = Path('/etc/os-release')


def sistema_operacional() -> str:
    with local_arquivo_sistema.open() as arquivo:
        conteúdo = arquivo.read()
    if 'debian' in conteúdo:
        return 'debian'
    elif 'arch' in conteúdo:
        return 'arch linux'
    else:
        raise SystemNotSupported(
            'Your sistem is not supported. Check the updates in '
            'https://github.com/b166erbot/katoolin.'
        )


def sub_sistema() -> str:
    local_arquivo = Path('/etc/issue')
    if local_arquivo.exists():
        with local_arquivo.open() as arquivo:
            sistema = arquivo.readlines()[0].strip().split()[0]
        return sistema.lower()
    else:
        return 'Erro'