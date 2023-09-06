from pathlib import Path
from json import load

from src.utils import (
    transformar_classes_programas, acrescentar_programas_extras
)
from src.ler_arquivos import sub_sistema
from src.modelos import Programas


local_programa = Path(__file__).parent.parent
local_json_programas = local_programa / 'programas' / 'programas.json'
with local_json_programas.open('r') as arquivo:
    programas = transformar_classes_programas(load(arquivo))
    programas = acrescentar_programas_extras(programas)
sistemas = [
    'ubuntu', 'pop!_os', 'linux', 'elementary', 'zorin', 'kubuntu', 'xubuntu',
    'lubuntu', 'kde'
]
if sub_sistema() not in sistemas:
    xprobe = Programas('xprobe', 'backbox')
    tinyhoneypot = Programas('tinyhoneypot', 'backbox')
    backbox = programas['backbox']
    index_programa = (
        backbox['information-gathering'].index(xprobe)
    )
    backbox['information-gathering'].pop(index_programa)
    index_programa = (
        backbox['social-engineering'].index(tinyhoneypot)
    )
    backbox['social-engineering'].pop(index_programa)


__all__ = ['programas']