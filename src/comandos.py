from configparser import ConfigParser
from os import system
from pathlib import Path

import requests

from src.excessoes import SystemNotSupported

# from src.utils import baixar_arquivo


def ler_configurações() -> ConfigParser:
    """Carrega e retorna as configurações de comandos."""
    config = ConfigParser()
    config.read('configuração.ini')
    return config


local_arquivo_arch = Path('/etc/arch-release')
local_arquivo_debian = Path('/etc/debian_version')


def sistema_operacional() -> str:
    if local_arquivo_debian.exists():
        return 'kalilinux'
    elif local_arquivo_arch.exists():
        return 'archstrike'
    else:
        raise SystemNotSupported(
            'Your sistem is not supported. Check the updates in '
            'https://github.com/b166erbot/katoolin.'
        )


def sistema_operacional_usuário() -> str:
    if local_arquivo_debian.exists():
        return 'debian'
    else:
        return 'arch linux'


configurações = ler_configurações()
sistema = sistema_operacional()


class Repositórios:
    def _adicionar_repositório_derivado_arch(
        self, nome: str, conteúdo: str
    ) -> None:
        """Adiciona um arquivo com um novo repositório no arch."""
        local_arquivo = Path(f"/etc/pacman.d/{nome}-mirrorlist")
        if not local_arquivo.exists():
            with local_arquivo.open('a') as arquivo:
                arquivo.write(conteúdo)
        local_conf = Path('/etc/pacman.conf')
        with local_conf.open() as arquivo:
            conteúdo_conf = arquivo.read()
        if not '[archstrike]' in conteúdo_conf:
            with local_conf.open('a') as arquivo:
                conteúdo_para_conf = (
                    f'[archstrike]\nInclude = {local_arquivo}'
                )
                arquivo.write(conteúdo_para_conf)

    def _adicionar_repositório_derivado_debian(
        self, nome: str, repositório: str
    ) -> None:
        """Adiciona um arquivo com um novo repositório no debian."""
        local_arquivo = Path(f"/etc/apt/sources.list.d/{nome}.list")
        if not local_arquivo.exists():
            with local_arquivo.open('w') as arquivo:
                linhas = f"# {nome} repository\n{repositório}\n"
                arquivo.write(linhas)

    def _remover_repositório_derivado_arch(self, nome: str) -> None:
        """Remove um arquivo com um repositório no arch."""
        local_conf = Path(f"/etc/pacman.conf")
        with local_conf.open() as arquivo:
            conteúdo_conf = arquivo.read()
        if '[archstrike]' in conteúdo_conf:
            with local_conf.open('w') as arquivo:
                conteúdo_conf = conteúdo_conf.split('\n')
                remover_conteúdo = [
                    '[archstrike]',
                    f'Include = /etc/pacman.d/{nome}-mirrorlist'
                ]
                conteúdo_conf = '\n'.join(filter(
                    lambda linha: linha not in remover_conteúdo, conteúdo_conf
                ))
                arquivo.write(conteúdo_conf)

    def _remover_repositório_derivado_debian(self, nome: str) -> None:
        """Remove um arquivo com um repositório no debian."""
        repositório = Path(f"/etc/apt/sources.list.d/{nome}.list")
        if repositório.exists():
            repositório.unlink()

    def _adicionar_archstrike_repositório(self) -> None:
        """Adiciona o repositório do archstrike."""
        nome = 'archstrike'
        conteúdo = 'Server = https://mirror.archstrike.org/$arch/$repo'
        self._adicionar_repositório_derivado_arch('archstrike', conteúdo)

    def _adicionar_kali_repositório(self) -> None:
        """Adiciona o repositório do kali-linux."""
        nome = 'kali-linux'
        repositório = (
            'deb http://http.kali.org/kali kali-rolling '
            'main non-free contrib'
        )
        self._adicionar_repositório_derivado_debian(nome, repositório)
    
    def adicionar_repositório(self):
        """Adiciona um repositório de hacking para a distro do usuário."""
        if sistema == 'kalilinux':
            self._adicionar_kali_repositório()
        else:
            self._adicionar_archstrike_repositório()

    def adicionar_gpg_key(self) -> None:
        """Adiciona uma chave gpg para a distro do usuário."""
        url = configurações[sistema]['site chave gpg']
        nome_arquivo = Path(Path(url).name)
        local_arquivo = 'asc' / nome_arquivo
        # baixar_arquivo(url)
        if sistema == 'archstrike':
            comandos = configurações['archstrike']['comandos gpg'].split('\n')
            for comando in comandos:
                system(f"{comando} 1>/dev/null 2>/dev/null")
        else:
            with local_arquivo.open() as arquivo:
                conteúdo = arquivo.read()
            local_arquivo_trusted = '/etc/apt/trusted.gpg.d' / nome_arquivo
            if not local_arquivo_trusted.exists():
                with local_arquivo_trusted.open('w') as arquivo:
                    arquivo.write(conteúdo)

    def instalar_requisitos_arch(self) -> None:
        """Instala programas necessários para o funcionamento do mirrorlist."""
        pacotes_requeridos = configurações[sistema]['pacotes requeridos']
        comando_instalar = configurações[sistema]['instalar']
        system(
            f"{comando_instalar} {pacotes_requeridos} "
            '1>/dev/null 2>/dev/null'
        )
        local_mirror_list = Path('/etc/pacman.d/archstrike-mirrorlist')
        local_novo_mirror_list = Path(
            '/etc/pacman.d/archstrike-mirrorlist.pacnew'
        )
        if local_mirror_list.exists():
            local_mirror_list.unlink()
        local_novo_mirror_list.rename('/etc/pacman.d/archstrike-mirrorlist')

    def remover_repositório(self) -> None:
        """Remove repositórios hackers da distro do usuário."""
        if sistema == 'kalilinux':
            self._remover_repositório_derivado_debian('kali-linux')
        else:
            self._remover_repositório_derivado_arch('archstrike')
