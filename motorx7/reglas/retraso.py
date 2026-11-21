"""Cálculo de retrasos respecto a la fecha límite (penalización, no violación)."""

from __future__ import annotations

from motorx7.dominio.escenario import Escenario
from motorx7.dominio.planificacion import Planificacion
from motorx7.reglas.incidencia import Retraso


def calcular_retrasos(planificacion: Planificacion, escenario: Escenario) -> tuple[Retraso, ...]:
    """Un Retraso por cada actividad asignada que termina después de su fecha límite."""
    raise NotImplementedError
