"""Resultado de planificar: qué recursos hacen cada actividad y cuándo."""

from __future__ import annotations

from dataclasses import dataclass

from motorx7.dominio.tiempo import Intervalo


@dataclass(frozen=True)
class Asignacion:
    """Una actividad asignada a uno o varios recursos en un intervalo."""

    actividad_id: str
    recurso_ids: tuple[str, ...]
    intervalo: Intervalo
    costo: float


@dataclass(frozen=True)
class Planificacion:
    """Conjunto inmutable de asignaciones sobre un escenario."""

    id: str
    escenario_id: str
    asignaciones: tuple[Asignacion, ...]

    def asignacion_de(self, actividad_id: str) -> Asignacion | None:
        """Asignación de una actividad, o None si no fue asignada."""
        raise NotImplementedError
