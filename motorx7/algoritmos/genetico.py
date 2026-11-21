"""Algoritmo genético implementado desde cero."""

from __future__ import annotations

import random
from dataclasses import dataclass

from motorx7.algoritmos.decodificador import Cromosoma
from motorx7.algoritmos.fitness import PesosAptitud
from motorx7.algoritmos.resultado import ResultadoEjecucion
from motorx7.dominio.escenario import Escenario


@dataclass(frozen=True)
class ParametrosGeneticos:
    poblacion: int
    generaciones: int
    prob_cruce: float
    prob_mutacion: float
    elitismo: int
    semilla: int

    def validar(self) -> None:
        """Comprueba rangos (probabilidades entre 0 y 1, elitismo menor que la población, etc.)."""
        raise NotImplementedError


def crear_poblacion_inicial(
    escenario: Escenario, parametros: ParametrosGeneticos, rng: random.Random
) -> list[Cromosoma]:
    raise NotImplementedError


def evaluar_individuo(cromosoma: Cromosoma, escenario: Escenario, pesos: PesosAptitud) -> float:
    """Decodifica, valida y calcula la aptitud de un individuo.
    Es una función de nivel de módulo y sin estado compartido para poder
    ejecutarla en otros procesos desde el módulo de paralelismo."""
    raise NotImplementedError


def seleccionar(
    poblacion: list[Cromosoma], aptitudes: list[float], rng: random.Random
) -> Cromosoma:
    raise NotImplementedError


def cruzar(padre: Cromosoma, madre: Cromosoma, rng: random.Random) -> Cromosoma:
    raise NotImplementedError


def mutar(cromosoma: Cromosoma, prob_mutacion: float, rng: random.Random) -> Cromosoma:
    raise NotImplementedError


def ejecutar_genetico(
    escenario: Escenario, parametros: ParametrosGeneticos, pesos: PesosAptitud
) -> ResultadoEjecucion:
    """Ciclo evolutivo completo. Registra la mejor aptitud de cada generación y
    devuelve la mejor planificación factible encontrada."""
    raise NotImplementedError
