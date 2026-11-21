"""Motor que aplica todas las reglas a una planificación."""

from __future__ import annotations

from collections.abc import Sequence

from motorx7.dominio.escenario import Escenario
from motorx7.dominio.planificacion import Planificacion
from motorx7.reglas.incidencia import InformeValidacion
from motorx7.reglas.restricciones import Regla, reglas_por_defecto


class MotorReglas:
    def __init__(self, reglas: Sequence[Regla] | None = None) -> None:
        self._reglas: list[Regla] = list(reglas) if reglas is not None else reglas_por_defecto()

    @property
    def reglas(self) -> tuple[Regla, ...]:
        return tuple(self._reglas)

    def agregar_regla(self, regla: Regla) -> None:
        self._reglas.append(regla)

    def validar(self, planificacion: Planificacion, escenario: Escenario) -> InformeValidacion:
        """Inspecciona la planificación sin modificarla: ejecuta todas las reglas
        y calcula los retrasos por separado."""
        raise NotImplementedError
