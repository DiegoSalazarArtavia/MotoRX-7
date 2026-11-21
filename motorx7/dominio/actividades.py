"""Actividades (servicios del taller) que deben planificarse."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum, IntEnum


class Prioridad(IntEnum):
    """Se usa IntEnum para poder ordenar: CRITICA > ALTA > MEDIA > BAJA."""

    BAJA = 1
    MEDIA = 2
    ALTA = 3
    CRITICA = 4


class EstadoActividad(Enum):
    PENDIENTE = "pendiente"
    ASIGNADA = "asignada"
    COMPLETADA = "completada"
    CANCELADA = "cancelada"


@dataclass
class Actividad:
    """Servicio a planificar.

    duracion_horas: tiempo positivo de ejecución.
    inicio_permitido / fecha_limite: ventana de planificación.
    habilidades_requeridas y cantidad_recursos: lo que exige la actividad.
    dependencias: IDs de actividades que deben terminar antes.
    """

    id: str
    descripcion: str
    duracion_horas: float
    prioridad: Prioridad
    inicio_permitido: datetime
    fecha_limite: datetime
    habilidades_requeridas: frozenset[str]
    cantidad_recursos: int
    dependencias: tuple[str, ...] = ()
    estado: EstadoActividad = field(default=EstadoActividad.PENDIENTE)

    def validar(self) -> None:
        """Valida duración, fechas, cantidad de recursos y autorreferencias. Lanza ValidacionError."""
        raise NotImplementedError
