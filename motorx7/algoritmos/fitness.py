"""Función de aptitud del algoritmo genético. La fórmula y los pesos se documentan aquí."""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

from motorx7.algoritmos.resultado import ActividadPendiente
from motorx7.dominio.escenario import Escenario
from motorx7.dominio.planificacion import Planificacion
from motorx7.reglas.incidencia import Retraso


@dataclass(frozen=True)
class PesosAptitud:
    asignadas: float
    costo: float
    retraso: float
    prioridad: float
    pendientes: float  # penaliza dejar actividades sin asignar


def calcular_aptitud(
    planificacion: Planificacion,
    pendientes: Sequence[ActividadPendiente],
    retrasos: Sequence[Retraso],
    escenario: Escenario,
    pesos: PesosAptitud,
) -> float:
    """Aptitud normalizada (mayor es mejor). Una solución con conflictos duros no se
    considera factible aunque tenga buena aptitud."""
    raise NotImplementedError
