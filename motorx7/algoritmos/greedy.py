"""Algoritmo inicial: heurística greedy determinista."""

from __future__ import annotations

from collections.abc import Iterable

from motorx7.algoritmos.resultado import ResultadoEjecucion
from motorx7.dominio.actividades import Actividad
from motorx7.dominio.escenario import Escenario


def ordenar_actividades(actividades: Iterable[Actividad]) -> list[Actividad]:
    """Orden determinista: prioridad (mayor primero), luego fecha límite y luego ID."""
    raise NotImplementedError


def ejecutar_greedy(escenario: Escenario) -> ResultadoEjecucion:
    """Procesa las actividades pendientes en orden y asigna cada una con
    `programar_actividad`. Rechaza la ejecución si no hay recursos o actividades válidos."""
    raise NotImplementedError
