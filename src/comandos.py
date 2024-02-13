from configparser import ConfigParser
from itertools import chain
from os import system
from pathlib import Path
from typing import Iterable

from src.excessoes import SystemNotSupported
from src.programas import programas
from src.ler_arquivos import ler_configurações, sistema_operacional

# from src.utils import baixar_arquivo


configurações = ler_configurações()
sistema = sistema_operacional()


class GerenciarRepositórios:
    def _incluir_arquivo_no_pacman_conf(
        self, nome: str
    ) -> None:
        """Inclui linhas no arquivo pacman.conf."""
        local_sources = Path(configurações[sistema]['local sources'])
        local_arquivo = local_sources / f"{nome}-mirrorlist"
        local_conf = Path(configurações[sistema]['arquivo sources'])
        with local_conf.open() as arquivo:
            conteúdo_conf = arquivo.read()
        if not f'[{nome}]' in conteúdo_conf:
            with local_conf.open('a') as arquivo:
                conteúdo_para_conf = (
                    f'\n\n[{nome}]\n'
                    # f'SigLevel = Never\n'
                    # ver isso no container archlinux
                    f'Include = {local_arquivo}'
                )
                arquivo.write(conteúdo_para_conf)

    def _adicionar_repositório_derivado_arch(
        self, nome: str, conteúdo: str
    ) -> None:
        """Adiciona um arquivo com um novo repositório no arch."""
        local_sources = Path(configurações[sistema]['local sources'])
        local_arquivo = local_sources / f"{nome}-mirrorlist"
        if not local_arquivo.exists():
            with local_arquivo.open('w') as arquivo:
                arquivo.write(conteúdo)

    def _adicionar_repositório_derivado_debian(
        self, nome: str, repositório: str
    ) -> None:
        """Adiciona um arquivo com um novo repositório no debian."""
        local_sources = Path(configurações[sistema]['local sources'])
        local_repositório = local_sources / f"{nome}.list"
        if not local_repositório.exists():
            with local_repositório.open('w') as arquivo:
                linhas = f"# {nome} repository\n{repositório}\n"
                arquivo.write(linhas)

    def _adicionar_archstrike_repositório(self) -> None:
        """Adiciona o repositório do archstrike."""
        nome = 'archstrike'
        conteúdo = (
            'Server = https://mirror.archstrike.org/$arch/$repo'
        )
        self._incluir_arquivo_no_pacman_conf(nome)
        self._adicionar_repositório_derivado_arch(nome, conteúdo)
    
    def _adicionar_blackarch_repositório(self) -> None:
        """Adiciona o repositório do blackarch."""
        self._incluir_arquivo_no_pacman_conf('blackarch')

    def _adicionar_kali_repositório(self) -> None:
        """Adiciona o repositório do kali-linux."""
        nome = 'kali-linux'
        repositório = (
            'deb http://http.kali.org/kali kali-rolling '
            'main non-free contrib'
        )
        self._adicionar_repositório_derivado_debian(nome, repositório)
    
    def _adicionar_backbox_repositório(self) -> None:
        """Adiciona um repositório do backbox."""
        nome = 'backbox'
        repositório = (
            'deb https://ppa.launchpadcontent.net/backbox/eight/ubuntu '
            'jammy main\n'
            'deb-src https://ppa.launchpadcontent.net/backbox/eight/ubuntu '
            'jammy main'
        )
        self._adicionar_repositório_derivado_debian(nome, repositório)
    
    def _adicionar_parrot_repositório(self) -> None:
        """Adiciona um repositório do parrot."""
        nome = 'parrot'
        repositório = (
            'deb https://deb.parrot.sh/parrot/ parrot main contrib non-free\n'
            '#deb-src https://deb.parrot.sh/parrot/ parrot main contrib '
            'non-free\n'
            'deb https://deb.parrot.sh/parrot/ parrot-security main contrib '
            'non-free\n'
            '#deb-src https://deb.parrot.sh/parrot/ parrot-security main '
            'contrib non-free\n'
            'deb https://deb.parrot.sh/parrot parrot-backports main '
            'contrib non-free\n'
            '#deb-src https://deb.parrot.sh/parrot parrot-backports main '
            'contrib non-free'
        )
        self._adicionar_repositório_derivado_debian(nome, repositório)

    def adicionar_repositórios(self):
        """Adiciona um repositório de hacking para a distro do usuário."""
        if sistema == 'debian':
            self._adicionar_kali_repositório()
            self._adicionar_backbox_repositório()
            self._adicionar_parrot_repositório()
        else:
            self._adicionar_archstrike_repositório()
            self._adicionar_blackarch_repositório()

    def _adicionar_chaves_gpg_debian(self) -> None:
        """Adiciona chaves gpg para debian."""
        distros = ['kali linux', 'backbox', 'parrot']
        for distro in distros:
            local_arquivo = Path(configurações[distro]['local arquivo asc'])
            nome_arquivo = Path(local_arquivo.name)
            local_arquivo_trusted = (
                configurações[sistema]['local gpg'] / nome_arquivo
            )
            with local_arquivo.open() as arquivo:
                conteúdo = arquivo.read()
            if not local_arquivo_trusted.exists():
                with local_arquivo_trusted.open('w') as arquivo:
                    arquivo.write(conteúdo)

    def _adicionar_chaves_gpg_arch(self) -> None:
        """Adiciona chaves gpg no arch linux."""
        comandos = configurações['archstrike']['comandos gpg'].split('\n')
        comandos.extend(configurações['blackarch']['comandos gpg'].split('\n'))
        for comando in comandos:
            system(f"{comando} 1>/dev/null 2>/dev/null")

    def adicionar_chaves_gpg(self) -> None:
        """Adiciona uma chave gpg para a distro do usuário."""
        # url = configurações[sistema]['site chave gpg']
        # baixar_arquivo(url)
        if sistema == 'arch linux':
            self._adicionar_chaves_gpg_arch()
        else:
            self._adicionar_chaves_gpg_debian()

    def instalar_requisitos_blackarch(self) -> None:
        """Copia o mirrorlist para o local de destino."""
        local_sources = Path(configurações[sistema]['local sources'])
        local_arquivo = Path(
            configurações['blackarch']['local mirrorlist']
        )
        novo_local_arquivo = local_sources / local_arquivo.name
        if not novo_local_arquivo.exists():
            with local_arquivo.open() as arquivo:
                conteúdo = arquivo.read()
            with novo_local_arquivo.open('w') as arquivo:
                arquivo.write(conteúdo)

    def adicionar_preferências_debian(self) -> None:
        """Configurar o sistema para não instalar a se não estiver instalado."""
        pacotes_kali = map(str, chain(*list(programas['kali linux'].values())))
        pacotes_backbox = map(str, chain(*list(programas['backbox'].values())))
        pacotes_parrot = map(str, chain(*list(programas['parrot'].values())))
        self._adicionar_preferências_debian(
            'kali-linux', pacotes_kali, 'kali', '602'
        )
        self._adicionar_preferências_debian(
            'parrot', pacotes_parrot, 'parrot', '601'
        )
        self._adicionar_preferências_debian(
            'backbox', pacotes_backbox, 'backbox', '600'
        )

    def _adicionar_preferências_debian(
        self, nome: str, packages: Iterable[str], release: str, priority: str
    ) -> None:
        """Adiciona arquivo e define a prioridade do repositório."""
        conteúdo = (
            "Package: *\n"
            f"Pin: release o={release}\n"
            "Pin-Priority: 100\n\n"
            f"Package: {' '.join(packages)}\n"
            f"Pin: release o={release}\n"
            f"Pin-Priority: {priority}"
        )
        local_preferências = Path(configurações[sistema]['local preferências'])
        local_arquivo = local_preferências / f'{nome}.pref'
        if not local_arquivo.exists():
            with local_arquivo.open('w') as arquivo:
                arquivo.write(conteúdo)
