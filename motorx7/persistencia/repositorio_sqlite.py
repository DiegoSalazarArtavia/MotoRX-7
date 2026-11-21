"""Repositorio SQLite. Cada guardado se hace dentro de una transacción para
no dejar resultados parciales."""

from __future__ import annotations

from pathlib import Path

from motorx7.algoritmos.resultado import ResultadoEjecucion
from motorx7.dominio.escenario import Escenario


class RepositorioSQLite:
    def __init__(self, ruta_db: Path) -> None:
        self.ruta_db = ruta_db

    def inicializar(self) -> None:
        """Crea las tablas si no existen."""
        raise NotImplementedError

    # --- Escenarios ---
    def guardar_escenario(self, escenario: Escenario) -> None:
        raise NotImplementedError

    def obtener_escenario(self, escenario_id: str) -> Escenario:
        raise NotImplementedError

    def listar_escenarios(self) -> list[tuple[str, str]]:
        """Pares (id, nombre)."""
        raise NotImplementedError

    # --- Ejecuciones ---
    def guardar_ejecucion(self, resultado: ResultadoEjecucion) -> None:
        raise NotImplementedError

    def obtener_ejecucion(self, ejecucion_id: str) -> ResultadoEjecucion:
        """Recupera la ejecución tal como se guardó, sin recalcularla.
        Lanza PersistenciaError si los datos están corruptos."""
        raise NotImplementedError

    def listar_ejecuciones(self) -> list[ResultadoEjecucion]:
        raise NotImplementedError

    def eliminar_ejecucion(self, ejecucion_id: str) -> None:
        raise NotImplementedError
