"""Carga de escenarios desde archivos JSON, con validación de esquema y referencias."""

from __future__ import annotations

from pathlib import Path

from motorx7.dominio.escenario import Escenario


def cargar_escenario_json(ruta: Path) -> Escenario:
    """Lanza EscenarioInvalidoError con todos los errores encontrados;
    nunca devuelve un escenario incompleto."""
    raise NotImplementedError


def exportar_escenario_json(escenario: Escenario, ruta: Path) -> None:
    raise NotImplementedError
