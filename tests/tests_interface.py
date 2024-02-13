from unittest import TestCase
from unittest.mock import MagicMock, patch
from itertools import chain
from functools import wraps


def mock_decorador(*args, **kwargs):
    def decorador(função):
        @wraps(função)
        def função_decorada(*args, **kwargs):
            return função(*args, **kwargs)
        return função_decorada
    return decorador


# é necessário mockar antes de importar, caso contrário, não irá funcionar.
patch('textual.work', mock_decorador).start()
from src.interface import KatoolinApp
from src.programas import programas


class TestsKatoolinApp(TestCase):
    def setUp(self, *_) -> None:
        self._argumentos = MagicMock(teste = False)
        self.app = KatoolinApp(self._argumentos)
        self.programas = list(chain(*programas['kali linux'].values()))
        self.programas.extend(chain(*programas['parrot'].values()))
        self.programas.extend(chain(*programas['backbox'].values()))

    @patch('src.interface.KatoolinApp.query_one')
    @patch('src.interface.KatoolinApp.query')
    @patch('src.interface.root', return_value = True)
    @patch('src.interface.sistema_operacional', return_value = 'debian')
    @patch('src.interface.system')
    def test_instalar_programas_passando_comando_correto_para_systema(
        self, system, *_
    ):
        self.app._instalar_programas(self.programas)
        for argumento in system.call_args_list[:4]:
            self.assertRegex(
                str(argumento),
                (
                    'apt --fix-broken -t=kali-rolling install -y .* '
                    '1>/dev/null 2>/dev/null'
                )
            )