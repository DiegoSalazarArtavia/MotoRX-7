"""Funciones puras: no modifican sus entradas ni dependen de variables globales.
Las tres operaciones de comparación tienen versión imperativa y funcional,
y ambas deben devolver resultados equivalentes."""

from __future__ import annotations

from collections.abc import Iterable

from motorx7.dominio.actividades import Actividad, Prioridad
from motorx7.dominio.escenario import Escenario
from motorx7.dominio.planificacion import Asignacion, Planificacion
from motorx7.dominio.recursos import Recurso
from motorx7.reglas.incidencia import Retraso

# --- 1. Filtrar recursos activos ---

def filtrar_recursos_activos_imperativo(recursos: Iterable[Recurso]) -> tuple[Recurso, ...]:
    raise NotImplementedError


def filtrar_recursos_activos_funcional(recursos: Iterable[Recurso]) -> tuple[Recurso, ...]:
    raise NotImplementedError


# --- 2. Costo total de las asignaciones ---

def costo_total_imperativo(asignaciones: Iterable[Asignacion]) -> float:
    raise NotImplementedError


def costo_total_funcional(asignaciones: Iterable[Asignacion]) -> float:
    raise NotImplementedError


# --- 3. Agrupar actividades por prioridad ---

def agrupar_por_prioridad_imperativo(
    actividades: Iterable[Actividad],
) -> dict[Prioridad, tuple[Actividad, ...]]:
    raise NotImplementedError


def agrupar_por_prioridad_funcional(
    actividades: Iterable[Actividad],
) -> dict[Prioridad, tuple[Actividad, ...]]:
    raise NotImplementedError


# --- Métricas de análisis ---

def actividades_por_prioridad(actividades: Iterable[Actividad]) -> dict[Prioridad, int]:
    raise NotImplementedError


def costo_por_recurso(asignaciones: Iterable[Asignacion], escenario: Escenario) -> dict[str, float]:
    raise NotImplementedError


def actividades_retrasadas(retrasos: Iterable[Retraso]) -> tuple[str, ...]:
    raise NotImplementedError


def utilizacion_por_recurso(planificacion: Planificacion, escenario: Escenario) -> dict[str, float]:
    """Proporción (0 a 1) de las horas disponibles de cada recurso que quedaron ocupadas."""
    raise NotImplementedError
