"""Análisis del grafo de dependencias entre actividades."""

from __future__ import annotations

from collections.abc import Mapping

from motorx7.dominio.actividades import Actividad


def buscar_ciclo(actividades: Mapping[str, Actividad]) -> list[str] | None:
    """Devuelve la cadena de IDs que forma un ciclo (por ejemplo ["A002", "A005", "A002"])
    o None si el grafo no tiene ciclos."""
    raise NotImplementedError


def orden_topologico(actividades: Mapping[str, Actividad]) -> list[str]:
    """IDs ordenados de forma que cada actividad aparece después de sus dependencias.
    Lanza CicloDependenciaError si existe un ciclo."""
    raise NotImplementedError
