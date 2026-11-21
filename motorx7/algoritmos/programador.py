"""Búsqueda del primer horario factible para una actividad.
Lo usan el algoritmo greedy y el decodificador del genético, así ambos
colocan las actividades con exactamente la misma lógica."""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

from motorx7.dominio.actividades import Actividad
from motorx7.dominio.escenario import Escenario
from motorx7.dominio.planificacion import Asignacion


@dataclass(frozen=True)
class ResultadoProgramacion:
    asignacion: Asignacion | None
    motivo: str | None  # causa cuando no se pudo asignar


def programar_actividad(
    actividad: Actividad,
    escenario: Escenario,
    asignaciones_actuales: Sequence[Asignacion],
    preferencia_recursos: Sequence[str] | None = None,
    paso_minutos: int = 30,
) -> ResultadoProgramacion:
    """Busca el primer instante, desde el inicio permitido y después de las dependencias,
    en el que haya suficientes recursos activos, compatibles y libres.
    `preferencia_recursos` define el orden en que se prueban los recursos (lo usa el genético).
    No inventa disponibilidad: si no hay opción dentro del horizonte, devuelve el motivo."""
    raise NotImplementedError
