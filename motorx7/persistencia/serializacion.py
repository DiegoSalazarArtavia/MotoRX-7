"""Conversión entre objetos del dominio y diccionarios (para SQLite y JSON)."""

from __future__ import annotations

from typing import Any

from motorx7.algoritmos.resultado import ResultadoEjecucion
from motorx7.dominio.escenario import Escenario


def escenario_a_dict(escenario: Escenario) -> dict[str, Any]:
    raise NotImplementedError


def dict_a_escenario(datos: dict[str, Any]) -> Escenario:
    raise NotImplementedError


def resultado_a_dict(resultado: ResultadoEjecucion) -> dict[str, Any]:
    raise NotImplementedError


def dict_a_resultado(datos: dict[str, Any]) -> ResultadoEjecucion:
    raise NotImplementedError
