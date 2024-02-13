from typing import TypeVar, cast
from json import load
from pathlib import Path

from textual.widgets import SelectionList
from textual.widgets.selection_list import Selection
from typing_extensions import Self

SelectionType = TypeVar('SelectionType')


class Programas:
    def __init__(self, programa: str, distro: str) -> None:
        self._programa = programa
        self.distro = distro

    def __eq__(self, other: Self | str) -> bool:
        """Retorna se um programa é igual ao outro."""
        if isinstance(other, str):
            return other == self._programa
        elif isinstance(other, Programas):
            return self._programa == other._programa
        else:
            raise TypeError(
                f"Precisa ser instância de str ou Programa"
            )

    def __hash__(self) -> hash:
        """Retorna o hash do programa."""
        return hash(self._programa)
    
    def __str__(self) -> str:
        """Retorna uma string do programa."""
        return self._programa
    
    def __repr__(self) -> str:
        """Retorna uma string do programa."""
        return self._programa


class MinhaListaSeleção(SelectionList):
    def _select_enabled(self, value: SelectionType) -> bool:
        """Seleciona se estiver ativo."""
        if not self._options[value].disabled:
            self._selected[value] = None
            self._message_changed()
            return True
        return False

    def select_all_enabled(self) -> Self:
        """Seleciona todos que estão ativos."""
        return self._apply_to_all(self._select_enabled)
