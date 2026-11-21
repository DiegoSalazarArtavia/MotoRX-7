"""Ejecución secuencial y paralela (procesos) de evaluaciones independientes.
Los tiempos se miden con un reloj monotónico (time.perf_counter).
En Windows, `funcion` debe estar definida a nivel de módulo para poder
enviarse a otros procesos, y el punto de entrada debe protegerse con
if __name__ == "__main__"."""

from __future__ import annotations

from collections.abc import Callable, Sequence
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ResultadoBenchmark:
    modo: str  # "secuencial" o "paralelo"
    evaluaciones: int
    procesos: int
    tiempo_segundos: float
    resultados: tuple[Any, ...]
    errores: tuple[str, ...]


@dataclass(frozen=True)
class ComparacionRendimiento:
    secuencial: ResultadoBenchmark
    paralelo: ResultadoBenchmark
    aceleracion: float  # tiempo_secuencial / tiempo_paralelo
    resultados_equivalentes: bool
    observacion: str


def ejecutar_secuencial(funcion: Callable[..., Any], entradas: Sequence[Any]) -> ResultadoBenchmark:
    raise NotImplementedError


def ejecutar_paralelo(
    funcion: Callable[..., Any], entradas: Sequence[Any], procesos: int
) -> ResultadoBenchmark:
    raise NotImplementedError


def calcular_aceleracion(tiempo_secuencial: float, tiempo_paralelo: float) -> float:
    raise NotImplementedError


def comparar(funcion: Callable[..., Any], entradas: Sequence[Any], procesos: int) -> ComparacionRendimiento:
    """Ejecuta ambas modalidades con las mismas entradas, verifica que los resultados
    coincidan e interpreta la aceleración (incluida la desaceleración por sobrecarga)."""
    raise NotImplementedError
