"""Generación reproducible de escenarios: misma semilla, mismos datos."""

from __future__ import annotations

from motorx7.dominio.escenario import Escenario

# (actividades, recursos) según el enunciado
TAMANOS: dict[str, tuple[int, int]] = {
    "pequeno": (20, 5),
    "mediano": (100, 20),
    "grande": (500, 50),
}


def generar_escenario(tamano: str, semilla: int) -> Escenario:
    """Crea exactamente la cantidad indicada de actividades y recursos, con IDs únicos,
    habilidades, disponibilidades, costos, prioridades y dependencias sin ciclos.
    Usa random.Random(semilla), nunca el generador global."""
    raise NotImplementedError
