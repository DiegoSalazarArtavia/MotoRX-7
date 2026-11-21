"""Resultado común de cualquier ejecución (greedy o genético)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from motorx7.dominio.planificacion import Planificacion
from motorx7.reglas.incidencia import InformeValidacion


@dataclass(frozen=True)
class ActividadPendiente:
    """Actividad que no se pudo asignar y la causa."""

    actividad_id: str
    motivo: str


@dataclass(frozen=True)
class ResultadoEjecucion:
    id: str
    algoritmo: str  # "greedy" o "genetico"
    escenario_id: str
    fecha: datetime
    semilla: int | None
    parametros: dict[str, float | int | str]
    planificacion: Planificacion
    pendientes: tuple[ActividadPendiente, ...]
    informe: InformeValidacion
    tiempo_segundos: float
    aptitud: float | None = None
    evolucion_aptitud: tuple[float, ...] = field(default_factory=tuple)  # mejor aptitud por generación
