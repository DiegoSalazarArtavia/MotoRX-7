"""Recursos del taller: personas, equipos y unidades operativas."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum

from motorx7.dominio.tiempo import Intervalo


class TipoRecurso(Enum):
    HUMANO = "humano"
    EQUIPO = "equipo"
    UNIDAD_OPERATIVA = "unidad_operativa"


@dataclass
class Recurso(ABC):
    """Recurso que puede asignarse a actividades.

    capacidad: máximo de actividades simultáneas (entero >= 1).
    costo_por_hora: costo no negativo en colones.
    disponibilidad: intervalos en los que el recurso se puede usar.
    habilidades: capacidades que ofrece (no puede estar vacío).
    """

    id: str
    nombre: str
    capacidad: int
    costo_por_hora: float
    habilidades: frozenset[str]
    disponibilidad: tuple[Intervalo, ...]
    activo: bool = field(default=True)

    @property
    @abstractmethod
    def tipo(self) -> TipoRecurso:
        """Tipo de recurso; cada subclase define el suyo."""

    def validar(self) -> None:
        """Valida capacidad, costo, intervalos y habilidades. Lanza ValidacionError."""
        raise NotImplementedError

    def esta_disponible(self, intervalo: Intervalo) -> bool:
        """True si algún intervalo de disponibilidad cubre `intervalo` completo."""
        raise NotImplementedError

    def tiene_habilidades(self, requeridas: frozenset[str]) -> bool:
        """True si el recurso ofrece todas las habilidades requeridas."""
        raise NotImplementedError

    def calcular_costo(self, horas: float) -> float:
        """Costo de usar el recurso `horas` horas. Las subclases pueden redefinirlo."""
        raise NotImplementedError


@dataclass
class RecursoHumano(Recurso):
    """Mecánico o inspector."""

    @property
    def tipo(self) -> TipoRecurso:
        return TipoRecurso.HUMANO


@dataclass
class Equipo(Recurso):
    """Elevador, escáner de diagnóstico, alineadora, etc."""

    @property
    def tipo(self) -> TipoRecurso:
        return TipoRecurso.EQUIPO


@dataclass
class UnidadOperativa(Recurso):
    """Bahía de servicio general o de inspección."""

    @property
    def tipo(self) -> TipoRecurso:
        return TipoRecurso.UNIDAD_OPERATIVA
