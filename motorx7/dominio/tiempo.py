"""Manejo de intervalos de tiempo."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Intervalo:
    """Intervalo de tiempo [inicio, fin). El inicio debe ser anterior al fin."""

    inicio: datetime
    fin: datetime

    def duracion_horas(self) -> float:
        """Duración del intervalo en horas."""
        raise NotImplementedError

    def contiene(self, otro: Intervalo) -> bool:
        """True si este intervalo cubre por completo a `otro`."""
        raise NotImplementedError

    def se_superpone(self, otro: Intervalo) -> bool:
        """True si los dos intervalos comparten algún tramo de tiempo."""
        raise NotImplementedError

    def interseccion(self, otro: Intervalo) -> Intervalo | None:
        """Tramo compartido entre ambos intervalos, o None si no se superponen."""
        raise NotImplementedError
