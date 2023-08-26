from json import load
from os import system
from pathlib import Path
from subprocess import getoutput
from time import sleep
from typing import Iterable

from textual import on, work
from textual.app import App, ComposeResult
from textual.containers import Grid, Horizontal, Vertical, VerticalScroll
from textual.screen import Screen
from textual.widgets import (Button, Label, LoadingIndicator, ProgressBar,
                             SelectionList, Static, TabbedContent, TabPane)

from src.comandos import (Repositórios, ler_configurações, sistema_operacional,
                          sistema_operacional_usuário)
from src.utils import recortar, root

local_programa = Path(__file__).parent.parent
local_texto_bem_vindo = local_programa / 'textos' / 'texto_bem_vindo.txt'
with local_texto_bem_vindo.open('r') as arquivo:
    texto = arquivo.read()
local_json_programas = local_programa / 'programas' / 'programas.json'
with local_json_programas.open('r') as arquivo:
    programas = load(arquivo)


class TelaErroRoot(Screen):
    CSS_PATH = str(local_programa / 'css/interface.css')

    def compose(self) -> ComposeResult:
        with Vertical(id = 'container_erro') as container:
            container.border_title = 'Error!'
            texto = '[red]You need to run this program with root privileges.[/]'
            yield Label(texto, id = 'label_erro')


class TelaDesinstalarRepositórios(Screen):
    CSS_PATH = str(local_programa / 'css/interface.css')

    def compose(self) -> ComposeResult:
        texto = (
            'To finish, now we have to remove the repositories so as not to '
            'break your system. Click start to remove and update.'
        )
        container = Vertical(
            id = 'vertical_desinstalar_repositorios',
            classes = 'container_generico'
        )
        container.border_title = 'Uninstall Repositories'
        with container:
            yield Label(
                texto, id = 'label_desinstalar_repositorios',
                classes = 'label_repositorios'
            )
            yield Button(
                'start',
                id = 'botao_iniciar2',
                classes = 'botoes_em_baixo'
            )


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

    def __init__(self, *args, **kwargs) -> None:
        self._sistema = sistema_operacional()
        self._id_botao_categoria_selecionados = {
            f"botao_{categoria}_selecionar_todos": categoria
            for categoria in programas[self._sistema]
        }
        self._id_botao_categoria_deselecionados = {
            f"botao_{categoria}_deselecionar_todos": categoria
            for categoria in programas[self._sistema]
        }
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        primeira_aba = list(programas[self._sistema])[0]
        tab_programas = TabbedContent(
            initial = primeira_aba, id = 'tab_programas'
        )
        tab_programas.border_title = 'Programs'
        texto_aviso = (
            'first, mark all the programs in all the tabs that you prefer,\n'
            'then click install below.'
        )
        with VerticalScroll(id = 'vertical_programas'):
            with tab_programas:
                for aba in programas[self._sistema]:
                    itens = [
                        (item, numero_programa)
                        for numero_programa, item
                        in enumerate(programas[self._sistema][aba])
                    ]
                    with TabPane(aba, id = aba):
                        with VerticalScroll():
                            yield Label(
                                texto_aviso, id = 'label_aviso_programas'
                            )
                            horizontal = Horizontal(
                                classes = 'horizontal_botoes_programas'
                            )
                            with horizontal:
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
                            yield SelectionList(
                                *itens, id = f"lista_selecao_{aba}",
                                classes = 'lista_selecao'
                            )
            yield Button(
                'install',
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


class TelaRepositórios(Screen):
    CSS_PATH = str(local_programa / 'css/interface.css')

    def __init__(self, *args, **kwargs) -> None:
        self._sistema = sistema_operacional_usuário()
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        texto = (
            'First, we need to install the repositories and update the '
            f"program database for your {self._sistema} or {self._sistema}"
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


class TelaBemVindo(Screen):
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

    _sistema = sistema_operacional()
    _sistema_usuário = sistema_operacional_usuário()
    SCREENS = {
        'tela boas vindas': TelaBemVindo(),
        'tela programas': TelaProgramas(),
        'tela repositórios': TelaRepositórios(),
        'tela carregamento1': TelaCarregamento1(),
        'tela carregamento2': TelaCarregamento2(),
        'tela desinstalar repositórios': TelaDesinstalarRepositórios(),
        'tela erro': TelaErroRoot()
    }
    global programas
    for lista_programas in programas['kalilinux'].values():
        for programa in lista_programas:
            if programa in programas['ferramentas_extras_kalilinux']:
                index_programa = lista_programas.index(programa)
                lista_programas.pop(index_programa)
                lista_programas.extend(
                    programas['ferramentas_extras_kalilinux'][programa]
                )
    repositórios = Repositórios()

    def on_mount(self) -> None:
        if not root():
            self.push_screen('tela erro')
            self.call_later(self.esperar_e_sair)
        else:
            self.push_screen('tela boas vindas')
    
    def esperar_e_sair(self) -> None:
        """Espera alguns segundos e sai do programa."""
        sleep(3)
        super().exit()
    
    @on(Button.Pressed, '#botao_continuar1')
    def trocar_tela_repositórios(self, evento: Button.Pressed) -> None:
        self.switch_screen('tela repositórios')
    
    @on(Button.Pressed, '.selecionar_todos')
    def selecionar_todos_itens(self, evento: Button.Pressed) -> None:
        categoria = (
            self.SCREENS['tela programas']
            ._id_botao_categoria_selecionados[evento.button.id]
        )
        lista_seleção = self.query_one(
            f"#lista_selecao_{categoria}", SelectionList
        )
        lista_seleção.select_all()

    @on(Button.Pressed, '.deselecionar_todos')
    def deselecionar_todos_itens(self, evento: Button.Pressed) -> None:
        categoria = (
            self.SCREENS['tela programas']
            ._id_botao_categoria_deselecionados[evento.button.id]
        )
        lista_seleção = self.query_one(
            f"#lista_selecao_{categoria}", SelectionList
        )
        lista_seleção.deselect_all()
    
    @on(Button.Pressed, '#botao_iniciar1')
    def instalar_repositórios_atualizar(self, evento: Button.Pressed) -> None:
        """Carrega a tela de loading e inicia a instalação do repositório."""
        self.switch_screen('tela carregamento1')
        self.call_later(self._instalar_repositórios_atualizar)
    
    @work(exclusive = True, thread = True)
    def _instalar_repositórios_atualizar(self) -> None:
        """Instala os repositórios e atualiza a base de dados dos programas."""
        configurações = ler_configurações()
        label_carregamento1 = self.query_one('#label_carregamento1', Label)
        label_carregamento1.update(
            f'installing {self._sistema} repository.'
        )
        self.repositórios.adicionar_repositório()
        label_carregamento1.update(
            f'[green]installing {self._sistema} repository.[/]'
        )
        sleep(0.3)

        label_carregamento1.update(f'adding {self._sistema} gpg key.')
        self.repositórios.adicionar_gpg_key()
        label_carregamento1.update(
            f'[green]adding {self._sistema} gpg key.[/]'
        )
        sleep(0.3)

        label_carregamento1.update('updating. maybe this will take a while.')
        comando = configurações[self._sistema]['atualizar']
        system(f"{comando} 1>/dev/null 2>/dev/null")
        label_carregamento1.update(
            '[green]updating. maybe this will take a while.[/]'
        )
        sleep(0.3)
        if self._sistema == 'archstrike':
            label_carregamento1.update(
                f'installing necessary programs in {self._sistema_usuário}'
            )
            self.repositórios.instalar_requisitos_arch()
            label_carregamento1.update(
                "[green]installing necessary programs "
                f"in {self._sistema_usuário}[/]"
            )
            sleep(0.3)

            label_carregamento1.update('updating. maybe this will take a while.')
            comando = configurações[self._sistema]['atualizar']
            system(f"{comando} 1>/dev/null 2>/dev/null")
            label_carregamento1.update(
                '[green]updating. maybe this will take a while.[/]'
            )
            sleep(0.3)
        label_carregamento1.update('[green]Done![/]')
        sleep(1)
        label_carregamento1.update('')
        self.call_later(lambda: self.switch_screen('tela programas'))
    
    @on(Button.Pressed, '#botao_instalar_programas')
    def instalar_programas(self, evento: Button.Pressed) -> None:
        """Carrega a tela de loading e instala os programas."""
        todos_os_programas = list(programas[self._sistema].values())
        programas_selecionados = [
            todos_os_programas[index_lista][index_programa]
            for index_lista, lista_seleção
            in enumerate(self.query('.lista_selecao'))
            for index_programa in lista_seleção.selected
        ]
        self.switch_screen('tela carregamento2')
        self.call_later(
            lambda: self._instalar_programas(programas_selecionados)
        )

    @work(exclusive = True, thread = True)
    def _instalar_programas(self, programas_selecionados: list[str]) -> None:
        """Instala os programas selecionados pelo usuário."""
        configurações = ler_configurações()
        label_carregamento2 = self.query_one('#label_carregamento2', Label)
        progressbar_carregamento2 = self.query_one(
            '#progressbar_carregamento2', ProgressBar
        )
        label_carregamento2.update(
            'installing programs. maybe this will take a while.'
        )
        quinze_porcento = (15 * len(programas_selecionados)) // 100 or 1
        comando_instalar = configurações[self._sistema]['instalar']
        programas_unicos = list(filter(
            lambda programa: '|' not in programa, programas_selecionados
        ))
        programas_unicos = recortar(programas_unicos, quinze_porcento)
        programas_multiplos = filter(
            lambda programa: '|' in programa, programas_selecionados
        )
        programas_multiplos = list(map(
            lambda programas: programas.split(' | '), programas_multiplos
        ))
        for recorte in programas_unicos:
            comando = (
                f"{comando_instalar} {' '.join(recorte)} "
                "1>/dev/null 2>/dev/null"
            )
            system(comando)
            if progressbar_carregamento2.percentage * 100 <= 90:
                progressbar_carregamento2.advance(15)
            label_carregamento2.update(
                'installing programs. maybe this will take a while. '
                f"{progressbar_carregamento2.percentage * 100}%"
            )
        self._instalar_programas_multiplos(
            programas_multiplos, comando_instalar
        )
        progressbar_carregamento2.advance(100) # garante que irá avançar em 100%
        label_carregamento2.update(
            '[green]installing programs. maybe this will take a while.[/]'
        )
        sleep(0.3)
        label_carregamento2.update('[green]Done![/]')
        sleep(1)
        self.call_later(
            lambda: self.switch_screen('tela desinstalar repositórios')
        )

    def _instalar_programas_multiplos(
        self, programas_multiplos: Iterable[str], comando_instalar: str
    ) -> None:
        """Instala os programas que tem mais de uma possibilidade."""
        for programas in programas_multiplos:
            for programa in programas:
                try:
                    call(
                        f"{comando_instalar} {programa}".split(),
                        stdout = DEVNULL, stderr = DEVNULL
                    )
                    break
                except:
                    pass
    
    @on(Button.Pressed, '#botao_iniciar2')
    def desinstalar_repositórios(self, evento: Button.Pressed) -> None:
        """Desisntala todos os repositórios e finaliza."""
        self.switch_screen('tela carregamento1')
        self.query_one('#label_carregamento1', Label).update('')
        self.call_later(self._desinstalar_repositórios)
    
    @work(exclusive = True, thread = True)
    def _desinstalar_repositórios(self) -> None:
        configurações = ler_configurações()
        label_carregamento1 = self.query_one('#label_carregamento1', Label)
        label_carregamento1.update(
            f'uninstalling {self._sistema_usuário} repository.'
        )
        self.repositórios.remover_repositório()
        label_carregamento1.update(
            f'[green]uninstalling {self._sistema_usuário} repository.[/]'
        )
        sleep(0.3)

        label_carregamento1.update('updating. maybe this will take a while.')
        comando = configurações[self._sistema]['atualizar']
        system(f"{comando} 1>/dev/null 2>/dev/null")
        label_carregamento1.update(
            '[green]updating. maybe this will take a while.[/]'
        )
        sleep(0.3)
        label_carregamento1.update('[green]Done![/]')
        sleep(1)
        self.call_later(self.exit)