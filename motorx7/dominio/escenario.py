"""Escenario: el conjunto de recursos y actividades sobre el que se planifica."""

from __future__ import annotations

from dataclasses import dataclass, field

from motorx7.dominio.actividades import Actividad
from motorx7.dominio.recursos import Recurso
from motorx7.dominio.tiempo import Intervalo


@dataclass
class Escenario:
    """Agrupa recursos y actividades. Todas las altas y cambios pasan por aquí
    para que las validaciones se apliquen siempre."""

    id: str
    nombre: str
    horizonte: Intervalo
    semilla: int | None = None
    recursos: dict[str, Recurso] = field(default_factory=dict)
    actividades: dict[str, Actividad] = field(default_factory=dict)

    # --- Recursos ---
    def agregar_recurso(self, recurso: Recurso) -> None:
        """Valida y agrega. Lanza IdDuplicadoError o ValidacionError sin guardar nada parcial."""
        raise NotImplementedError

    def editar_recurso(self, recurso: Recurso) -> None:
        """Reemplaza un recurso existente después de validarlo de nuevo."""
        raise NotImplementedError

    def desactivar_recurso(self, recurso_id: str) -> None:
        """Marca el recurso como inactivo sin borrarlo."""
        raise NotImplementedError

    def recursos_activos(self) -> list[Recurso]:
        raise NotImplementedError

    # --- Actividades ---
    def agregar_actividad(self, actividad: Actividad) -> None:
        """Valida (incluye dependencias existentes y ausencia de ciclos) y agrega."""
        raise NotImplementedError

    def editar_actividad(self, actividad: Actividad) -> None:
        raise NotImplementedError

    def eliminar_actividad(self, actividad_id: str) -> None:
        """Solo elimina actividades pendientes de las que ninguna otra dependa.
        Lanza OperacionNoPermitidaError en caso contrario."""
        raise NotImplementedError
