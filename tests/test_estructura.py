"""Pruebas de humo: la estructura del proyecto se importa y los contratos básicos existen."""

import importlib

import pytest

MODULOS = [
    "motorx7.dominio.excepciones",
    "motorx7.dominio.tiempo",
    "motorx7.dominio.recursos",
    "motorx7.dominio.actividades",
    "motorx7.dominio.planificacion",
    "motorx7.dominio.dependencias",
    "motorx7.dominio.escenario",
    "motorx7.reglas.incidencia",
    "motorx7.reglas.restricciones",
    "motorx7.reglas.retraso",
    "motorx7.reglas.motor",
    "motorx7.algoritmos.resultado",
    "motorx7.algoritmos.programador",
    "motorx7.algoritmos.greedy",
    "motorx7.algoritmos.fitness",
    "motorx7.algoritmos.decodificador",
    "motorx7.algoritmos.genetico",
    "motorx7.funcional.transformaciones",
    "motorx7.paralelo.benchmark",
    "motorx7.comparacion.comparador",
    "motorx7.escenarios.generador",
    "motorx7.escenarios.importador",
    "motorx7.persistencia.serializacion",
    "motorx7.persistencia.repositorio_sqlite",
]


@pytest.mark.parametrize("nombre", MODULOS)
def test_modulo_se_importa(nombre):
    importlib.import_module(nombre)


def test_motor_tiene_nueve_reglas_con_codigo_unico():
    from motorx7.reglas.motor import MotorReglas

    codigos = [regla.codigo for regla in MotorReglas().reglas]
    assert len(codigos) == 9
    assert len(set(codigos)) == 9


def test_tamanos_de_escenario_del_enunciado():
    from motorx7.escenarios.generador import TAMANOS

    assert TAMANOS == {"pequeno": (20, 5), "mediano": (100, 20), "grande": (500, 50)}


def test_prioridades_se_pueden_ordenar():
    from motorx7.dominio.actividades import Prioridad

    assert Prioridad.CRITICA > Prioridad.ALTA > Prioridad.MEDIA > Prioridad.BAJA


def test_recurso_abstracto_no_se_instancia():
    from motorx7.dominio.recursos import Recurso

    with pytest.raises(TypeError):
        Recurso("R001", "x", 1, 0.0, frozenset({"a"}), ())
