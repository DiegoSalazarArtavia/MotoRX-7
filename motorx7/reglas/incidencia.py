"""Estructuras del informe de validación."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class Incidencia:
    """Violación de una restricción dura."""

    codigo_regla: str
    actividad_id: str
    recurso_id: str | None
    descripcion: str
    contexto: dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class Retraso:
    """Penalización por terminar después de la fecha límite (no es violación dura)."""

    actividad_id: str
    fin: datetime
    fecha_limite: datetime
    horas_retraso: float


@dataclass(frozen=True)
class InformeValidacion:
    incidencias: tuple[Incidencia, ...]
    retrasos: tuple[Retraso, ...]

    @property
    def factible(self) -> bool:
        return len(self.incidencias) == 0

    @property
    def estado(self) -> str:
        return "FACTIBLE" if self.factible else "NO FACTIBLE"
