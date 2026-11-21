"""Restricciones duras. Cada regla es una clase con el mismo método `evaluar`,
así el motor las recorre sin saber cuál es cada una (polimorfismo) y una regla
nueva se agrega sin modificar las existentes."""

from __future__ import annotations

from abc import ABC, abstractmethod

from motorx7.dominio.escenario import Escenario
from motorx7.dominio.planificacion import Planificacion
from motorx7.reglas.incidencia import Incidencia


class Regla(ABC):
    codigo: str = ""
    descripcion: str = ""

    @abstractmethod
    def evaluar(self, planificacion: Planificacion, escenario: Escenario) -> list[Incidencia]:
        """Devuelve las incidencias encontradas; lista vacía si la regla se cumple.
        No modifica la planificación."""


class IntegridadReferencias(Regla):
    codigo = "R01"
    descripcion = "La actividad y los recursos de cada asignación existen"

    def evaluar(self, planificacion: Planificacion, escenario: Escenario) -> list[Incidencia]:
        raise NotImplementedError


class RecursoActivo(Regla):
    codigo = "R02"
    descripcion = "Los recursos asignados están activos"

    def evaluar(self, planificacion: Planificacion, escenario: Escenario) -> list[Incidencia]:
        raise NotImplementedError


class HabilidadesCompatibles(Regla):
    codigo = "R03"
    descripcion = "Los recursos tienen las habilidades que exige la actividad"

    def evaluar(self, planificacion: Planificacion, escenario: Escenario) -> list[Incidencia]:
        raise NotImplementedError


class DisponibilidadCompleta(Regla):
    codigo = "R04"
    descripcion = "La disponibilidad del recurso cubre todo el intervalo asignado"

    def evaluar(self, planificacion: Planificacion, escenario: Escenario) -> list[Incidencia]:
        raise NotImplementedError


class CapacidadSimultanea(Regla):
    codigo = "R05"
    descripcion = "Ningún recurso supera su capacidad en intervalos superpuestos"

    def evaluar(self, planificacion: Planificacion, escenario: Escenario) -> list[Incidencia]:
        raise NotImplementedError


class CantidadRecursos(Regla):
    codigo = "R06"
    descripcion = "Cada actividad recibe la cantidad de recursos requerida"

    def evaluar(self, planificacion: Planificacion, escenario: Escenario) -> list[Incidencia]:
        raise NotImplementedError


class DependenciasCumplidas(Regla):
    codigo = "R07"
    descripcion = "Una actividad inicia después de que terminan sus dependencias"

    def evaluar(self, planificacion: Planificacion, escenario: Escenario) -> list[Incidencia]:
        raise NotImplementedError


class InicioPermitido(Regla):
    codigo = "R08"
    descripcion = "Ninguna actividad inicia antes de su inicio permitido"

    def evaluar(self, planificacion: Planificacion, escenario: Escenario) -> list[Incidencia]:
        raise NotImplementedError


class SinConflictos(Regla):
    codigo = "R09"
    descripcion = "No hay asignaciones en conflicto (actividad asignada dos veces o recurso repetido)"

    def evaluar(self, planificacion: Planificacion, escenario: Escenario) -> list[Incidencia]:
        raise NotImplementedError


def reglas_por_defecto() -> list[Regla]:
    """Las nueve restricciones duras que exige el enunciado."""
    return [
        IntegridadReferencias(),
        RecursoActivo(),
        HabilidadesCompatibles(),
        DisponibilidadCompleta(),
        CapacidadSimultanea(),
        CantidadRecursos(),
        DependenciasCumplidas(),
        InicioPermitido(),
        SinConflictos(),
    ]
