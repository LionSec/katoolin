from argparse import Namespace
from os import system
from pathlib import Path
from time import sleep
from typing import Iterable

from textual import on, work
from textual.app import App, ComposeResult
from textual.containers import Grid, Horizontal, Vertical, VerticalScroll
from textual.screen import Screen
from textual.widgets import (
    Button, Label, LoadingIndicator, ProgressBar, TabbedContent,
    TabPane)
from textual.widgets.selection_list import Selection

from src.comandos import (
    GerenciarRepositórios, ler_configurações, sistema_operacional)
from src.modelos import MinhaListaSeleção, Programas
from src.utils import (
    recortar, root)
from src.programas import programas

local_programa = Path(__file__).parent.parent
local_texto_bem_vindo = local_programa / 'textos' / 'texto_bem_vindo.txt'
with local_texto_bem_vindo.open('r') as arquivo:
    texto = arquivo.read()
sistema = sistema_operacional()
configurações = ler_configurações()
nomes_repositórios = {
    'debian': ['kali linux', 'parrot', 'backbox'],
    'arch linux': ['blackarch', 'archstrike']
}
nomes_origem = {
    'kali linux': 'kali-rolling'
}

class TelaEscolherRepositórios(Screen):
    CSS_PATH = str(local_programa / 'css/interface.css')

    def __init__(
        self, distros: list[str], *args, **kwargs
    ) -> None:
        self._seleções_distros = [
            (distro, numero_distro)
            for numero_distro, distro
            in enumerate(distros)
        ]
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        container = Vertical(
            id = 'vertical_escolher_repositorios',
            classes = 'container_generico'
        )
        container.border_title = 'Choice'
        with container:
            yield Label(
                'Choose the distributions you want to install the programs.'
            )
            yield MinhaListaSeleção(
                *self._seleções_distros,
                id = 'lista_selecao_escolher_repositorio',
            )
            yield Button(
                'Continue', id = 'botao_continuar2',
                classes = 'botao_em_baixo', disabled = True
            )


class TelaErroRoot(Screen):
    CSS_PATH = str(local_programa / 'css/interface.css')

    def compose(self) -> ComposeResult:
        with Vertical(id = 'container_erro') as container:
            container.border_title = 'Error!'
            texto = '[red]You need to run this program with root privileges.[/]'
            yield Label(texto, id = 'label_erro')


class TelaCarregamento2(Screen):
    CSS_PATH = str(local_programa / 'css/interface.css')

    def compose(self) -> ComposeResult:
        container = Vertical(
            id = 'vertical_carregamento2', classes = 'container_generico'
        )
        container.border_title = 'Loading'
        with container:
            yield Label(id = 'label_carregamento2')
            yield ProgressBar(
                id = 'progressbar_carregamento2', classes = 'botoes_em_baixo',
                total = 100, show_eta = False
            )


class TelaProgramas(Screen):
    CSS_PATH = str(local_programa / 'css/interface.css')

    def __init__(
        self, distro: str, install: bool, app: App, *args, **kwargs
    ) -> None:
        self._install = install
        self._distro = distro
        self._app = app
        self._id_botao_categoria_selecionados = {
            f"botao_{categoria}_selecionar_todos": categoria
            for categoria in programas[distro]
        }
        self._id_botao_categoria_deselecionados = {
            f"botao_{categoria}_deselecionar_todos": categoria
            for categoria in programas[distro]
        }
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        primeira_aba = list(programas[self._distro])[0]
        tab_programas = TabbedContent(
            initial = primeira_aba, id = 'tab_programas'
        )
        tab_programas.border_title = 'Programs'
        texto_ação = 'install' if self._install else 'next'
        texto_aviso = (
            f'current repository: [green italic]<{self._distro}>[/]\n'
            'first, mark all the programs in all the tabs that you prefer,\n'
            f'then click {texto_ação} below.'
        )
        with VerticalScroll(id = 'vertical_programas'):
            with tab_programas:
                for aba in programas[self._distro]:
                    # map de tuplas com os programas e se ele está
                    # desabilitado
                    programas_ = list(map(
                        lambda programa: (
                            (programa, programa in self._app.programas_instalar)
                        ),
                        programas[self._distro][aba]
                    ))
                    if any(map(lambda programa: programa[1], programas_)):
                        texto_extra = (
                            ' [red]some programs have been disabled.[/]'
                        )
                    else:
                        texto_extra = ''
                    # lista com seleções dos programas
                    itens = [
                        Selection(
                            str(item), numero_programa, disabled = desabilitado
                        )
                        for numero_programa, (item, desabilitado)
                        in enumerate(programas_)
                    ]
                    with TabPane(aba, id = aba):
                        with VerticalScroll():
                            yield Label(
                                texto_aviso + texto_extra,
                                id = 'label_aviso_programas'
                            )
                            horizontal = Horizontal(
                                classes = 'horizontal_botoes_programas'
                            )
                            horizontal_1 = Horizontal(
                                classes = 'horizontal_botoes_programas_'
                            )
                            horizontal_2 = Horizontal(
                                classes = 'horizontal_botoes_programas_'
                            )
                            horizontal_1.border_title = 'from this tab'
                            horizontal_2.border_title = 'from all tabs'
                            with horizontal:
                                with horizontal_1:
                                    yield Button(
                                        'select all',
                                        id = f"botao_{aba}_selecionar_todos",
                                        classes = 'selecionar_todos'
                                    )
                                    yield Button(
                                        'deselect all',
                                        id = f"botao_{aba}_deselecionar_todos",
                                        classes = 'deselecionar_todos'
                                    )
                                with horizontal_2:
                                    yield Button(
                                        'select all',
                                        classes = 'selecionar_todos_abas'
                                    )
                                    yield Button(
                                        'deselect all',
                                        classes = 'deselecionar_todos_abas'
                                    )
                            distro = self._distro.replace(' ', '_')
                            yield MinhaListaSeleção(
                                *itens,
                                id = f"lista_selecao_{aba}",
                                classes = f'lista_selecao_{distro}'
                            )
            yield Button(
                texto_ação,
                id = 'botao_instalar_programas', classes = 'botoes_em_baixo'
            )


class TelaCarregamento1(Screen):
    CSS_PATH = str(local_programa / 'css/interface.css')

    def compose(self) -> ComposeResult:
        container = Vertical(
            id = 'vertical_carregamento1', classes = 'container_generico'
        )
        container.border_title = 'Loading'
        with container:
            yield Label(id = 'label_carregamento1')
            yield LoadingIndicator(
                id = 'loading_carregamento1', classes = 'botoes_em_baixo'
            )


class TelaInstalarRepositórios(Screen):
    CSS_PATH = str(local_programa / 'css/interface.css')

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        texto = (
            'First, we need to install the repositories and update the '
            f"program database for your {sistema} or {sistema}"
            ' based system. Click start to install and update.'
        )
        container = Vertical(
            id = 'vertical_repositorios', classes = 'container_generico'
        )
        container.border_title = 'Install Repositories'
        with container:
            yield Label(
                texto, id = 'label_repositorios', classes = 'label_repositorios'
            )
            yield Button(
                'start',
                id = 'botao_iniciar1',
                classes = 'botoes_em_baixo'
            )


class TelaBoasVindas(Screen):
    CSS_PATH = str(local_programa / 'css/interface.css')

    def compose(self) -> ComposeResult:
        with VerticalScroll(id = 'vertical_bem_vindo') as container:
            container.border_title = 'Welcome'
            yield Label(texto, id = 'label_bem_vindo')
            yield Button(
                'continue',
                id = 'botao_continuar1',
                classes = 'botoes_em_baixo'
            )


class KatoolinApp(App):
    CSS_PATH = str(local_programa / 'css/interface.css')

    SCREENS = {
        'tela boas vindas': TelaBoasVindas(),
        'tela repositórios': TelaInstalarRepositórios(),
        'tela carregamento1': TelaCarregamento1(),
        'tela carregamento2': TelaCarregamento2(),
        'tela erro': TelaErroRoot(),
        'tela escolher repositórios': TelaEscolherRepositórios(
            nomes_repositórios[sistema]
        )
    }
    gerenciar_repositórios = GerenciarRepositórios()
    programas_instalar = set()

    def __init__(self, argumentos: Namespace, *args, **kwargs) -> None:
        self._argumentos = argumentos
        super().__init__(*args, **kwargs)

    def on_mount(self) -> None:
        if self._argumentos.teste or root():
            self.push_screen('tela boas vindas')
        else:
            self.push_screen('tela erro')
            self.call_later(self.esperar_e_sair)
    
    def esperar_e_sair(self) -> None:
        """Espera alguns segundos e sai do programa."""
        sleep(3)
        super().exit()
    
    @on(Button.Pressed, '#botao_continuar1')
    def trocar_tela_repositórios(self, evento: Button.Pressed) -> None:
        self.switch_screen('tela repositórios')
    
    @on(Button.Pressed, '.selecionar_todos')
    def selecionar_todos_itens(self, evento: Button.Pressed) -> None:
        aba_ativa = self.query_one('#tab_programas', TabbedContent).active
        lista_seleção = self.query_one(
            f"#lista_selecao_{aba_ativa}", MinhaListaSeleção
        )
        lista_seleção.select_all_enabled()

    @on(Button.Pressed, '.deselecionar_todos')
    def deselecionar_todos_itens(self, evento: Button.Pressed) -> None:
        aba_ativa = self.query_one('#tab_programas', TabbedContent).active
        lista_seleção = self.query_one(
            f"#lista_selecao_{aba_ativa}", MinhaListaSeleção
        )
        lista_seleção.deselect_all()

    @on(Button.Pressed, '.selecionar_todos_abas')
    def selecionar_todos_itens_das_abas(self, evento: Button.Pressed) -> None:
        distro = self.screen._distro.replace(' ', '_')
        for seleção in self.query(f".lista_selecao_{distro}"):
            seleção.select_all_enabled()

    @on(Button.Pressed, '.deselecionar_todos_abas')
    def deselecionar_todos_itens_das_abas(self, evento: Button.Pressed) -> None:
        distro = self.screen._distro.replace(' ', '_')
        for seleção in self.query(f".lista_selecao_{distro}"):
            seleção.deselect_all()

    @on(Button.Pressed, '#botao_iniciar1')
    def instalar_repositórios_atualizar(self, evento: Button.Pressed) -> None:
        """Carrega a tela de loading e inicia a instalação do repositório."""
        self.switch_screen('tela carregamento1')
        self.call_later(self._instalar_repositórios_atualizar)

    @work(exclusive = True, thread = True)
    def _instalar_repositórios_atualizar(self) -> None:
        """Instala os repositórios e atualiza a base de dados dos programas."""
        if not self._argumentos.teste:
            label_carregamento1 = self.query_one('#label_carregamento1', Label)
            label_carregamento1.update(
                f'installing repositories.'
            )
            self.gerenciar_repositórios.adicionar_repositórios()
            label_carregamento1.update(
                f'[green]installing repositories.[/]'
            )
            sleep(0.3)

            if sistema == 'arch linux':
                label_carregamento1.update(
                    'installing necessary programs in blackarch and archstrike'
                )
                self.gerenciar_repositórios.instalar_requisitos_blackarch()
                label_carregamento1.update(
                    "[green]installing necessary programs in "
                    "blackarch and archstrike[/]"
                )
                sleep(0.3)
            else:
                label_carregamento1.update(
                    'changing the priority of repositories'
                )
                self.gerenciar_repositórios.adicionar_preferências_debian()
                label_carregamento1.update(
                    '[green]changing the priority of repositories[/]'
                )
                sleep(0.3)

            label_carregamento1.update(f'adding gpg keys.')
            self.gerenciar_repositórios.adicionar_chaves_gpg()
            label_carregamento1.update(
                f'[green]adding gpg keys.[/]'
            )
            sleep(0.3)

            label_carregamento1.update(
                'updating. maybe this will take a while.'
            )

            label_carregamento1.update(
                'updating. maybe this will take a while.'
            )
            comando = configurações[sistema]['atualizar']
            system(f"{comando} 1>/dev/null 2>/dev/null")
            label_carregamento1.update(
                '[green]updating. maybe this will take a while.[/]'
            )
            sleep(0.3)
            label_carregamento1.update('[green]Done![/]')
            sleep(1)
            label_carregamento1.update('')
        self.call_later(lambda: self.switch_screen(
            'tela escolher repositórios'
        ))

    @on(Button.Pressed, '#botao_instalar_programas')
    def instalar_programas(self, evento: Button.Pressed) -> None:
        """Carrega a tela de loading e instala os programas."""
        todos_os_programas = list(programas[self.screen._distro].values())
        distro = self.screen._distro.replace(' ', '_')
        programas_selecionados = set(
            todos_os_programas[index_lista][index_programa]
            for index_lista, lista_seleção
            in enumerate(self.query(f'.lista_selecao_{distro}'))
            for index_programa in lista_seleção.selected
        )
        self.programas_instalar.update(programas_selecionados)
        if str(evento.button.label) == 'next':
            self.switch_screen(
                TelaProgramas(*next(self._distros_selecionadas), self)
            )
        else:
            self.switch_screen('tela carregamento2')
            self.call_later(
                lambda: self._instalar_programas(self.programas_instalar)
            )

    @work(exclusive = True, thread = True)
    def _instalar_programas(self, programas_selecionados: list[str]) -> None:
        """Instala os programas selecionados pelo usuário."""
        if not self._argumentos.teste:
            label_carregamento2 = self.query_one('#label_carregamento2', Label)
            progressbar_carregamento2 = self.query_one(
                '#progressbar_carregamento2', ProgressBar
            )
            label_carregamento2.update(
                'installing programs. maybe this will take a while.'
            )
            quinze_porcento = (15 * len(programas_selecionados)) // 100 or 1
            comando_instalar = configurações[sistema]['instalar']
            if sistema == 'debian':
                for nome_repositório in nomes_repositórios['debian']:
                    origem = nomes_origem.get(
                        nome_repositório, nome_repositório
                    )
                    comando_instalar_ = comando_instalar.format(origem)
                    programas = filter(
                        lambda programa: programa.distro == nome_repositório,
                        programas_selecionados
                    )
                    programas = list(map(
                        str, programas
                    ))
                    programas = recortar(programas, quinze_porcento)
                    for recorte in programas:
                        comando = (
                            f"{comando_instalar_} {' '.join(recorte)} "
                            "1>/dev/null 2>/dev/null"
                        )
                        system(comando)
                        porcentagem = (
                            (len(recorte) * 100) // len(programas_selecionados)
                        )
                        progressbar_carregamento2.advance(porcentagem)
            else:
                programas = list(map(str, programas_selecionados))
                programas = recortar(programas, quinze_porcento)
                for recorte in programas:
                    comando = (
                        f"{comando_instalar} {' '.join(recorte)} "
                        "1>/dev/null 2>/dev/null"
                    )
                    system(comando)
                    progressbar_carregamento2.advance(15)
            # garante que irá avançar em 100%
            progressbar_carregamento2.advance(100)
            label_carregamento2.update(
                '[green]installing programs. maybe this will take a while.[/]'
            )
            sleep(0.3)
            label_carregamento2.update('[green]Done![/]')
            sleep(1)
        self.call_later(self.exit)

    @on(Button.Pressed, '#botao_continuar2')
    def botao_continuar_excolher_repositorios(
        self, evento: Button.Pressed
    ) -> None:
        """Passa para a próxima tela: instalar programas."""
        seleção = self.query_one(
            '#lista_selecao_escolher_repositorio', MinhaListaSeleção
        )
        distros_selecionadas = map(
            lambda index_distro: nomes_repositórios[sistema][index_distro],
            seleção.selected
        )
        distros_selecionadas = sorted(
            distros_selecionadas,
            key = lambda distro: nomes_repositórios[sistema].index(distro)
        )
        # todas as telas menos a última irá criar um botão next e a última irá
        # criar um botão install.
        último_número = len(distros_selecionadas) - 1
        self._distros_selecionadas = (
            (distro, número == último_número)
            for número, distro
            in enumerate(distros_selecionadas)
        )
        distro, boleano_botão_instalar = next(self._distros_selecionadas)
        self.switch_screen(
            TelaProgramas(distro, boleano_botão_instalar, self)
        )
    
    @on(MinhaListaSeleção.SelectionToggled, '#lista_selecao_escolher_repositorio')
    def lista_seleção_alterada(
        self, evento: MinhaListaSeleção.SelectionToggled
    ) -> None:
        """Executa quando o uruário altera a lista."""
        botão = self.query_one('#botao_continuar2', Button)
        lista_seleção = self.query_one(
            '#lista_selecao_escolher_repositorio', MinhaListaSeleção
        )
        if len(lista_seleção.selected) == 0:
            botão.disabled = True
        else:
            botão.disabled = False
