"""Métricas por ejecución y tabla comparativa."""

from __future__ import annotations

from dataclasses import dataclass

from motorx7.algoritmos.resultado import ResultadoEjecucion
from motorx7.dominio.escenario import Escenario


@dataclass(frozen=True)
class MetricasEjecucion:
    asignadas: int
    pendientes: int
    costo_total: float
    retraso_total_horas: float
    recursos_usados: int
    utilizacion_promedio: float
    violaciones_por_regla: dict[str, int]
    tiempo_segundos: float
    aptitud: float | None
    factible: bool


@dataclass(frozen=True)
class FilaComparacion:
    metrica: str
    valor_inicial: float
    valor_genetico: float
    diferencia: float
    diferencia_porcentual: float | None  # None cuando el denominador es cero
    interpretacion: str  # "mejoró", "empeoró" o "no cambió"


@dataclass(frozen=True)
class ComparacionEjecuciones:
    valida: bool
    advertencias: tuple[str, ...]
    filas: tuple[FilaComparacion, ...]


def calcular_metricas(resultado: ResultadoEjecucion, escenario: Escenario) -> MetricasEjecucion:
    raise NotImplementedError


def comparar_ejecuciones(
    inicial: ResultadoEjecucion, genetico: ResultadoEjecucion, escenario: Escenario
) -> ComparacionEjecuciones:
    """Compara dos ejecuciones del mismo escenario. Si no son comparables, lo advierte.
    Señala cuando un menor costo viene acompañado de más pendientes o más retraso."""
    raise NotImplementedError
