"""Traducción de un cromosoma a una planificación."""

from __future__ import annotations

from dataclasses import dataclass

from motorx7.algoritmos.resultado import ActividadPendiente
from motorx7.dominio.escenario import Escenario
from motorx7.dominio.planificacion import Planificacion


@dataclass(frozen=True)
class Cromosoma:
    """orden_actividades: permutación de IDs de actividades.
    preferencias_recursos: para cada actividad (mismo orden), IDs de recursos en orden de preferencia."""

    orden_actividades: tuple[str, ...]
    preferencias_recursos: tuple[tuple[str, ...], ...]


def decodificar(
    cromosoma: Cromosoma, escenario: Escenario
) -> tuple[Planificacion, tuple[ActividadPendiente, ...]]:
    """Recorre el orden del cromosoma respetando dependencias y coloca cada actividad
    con `programar_actividad`."""
    raise NotImplementedError
