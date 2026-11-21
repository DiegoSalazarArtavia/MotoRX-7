"""Punto de entrada. Ejecutar con: streamlit run app.py"""

import streamlit as st

from motorx7.interfaz import secciones

SECCIONES = {
    "Escenarios": secciones.escenarios,
    "Recursos": secciones.recursos,
    "Actividades": secciones.actividades,
    "Validar": secciones.validar,
    "Algoritmo inicial": secciones.algoritmo_inicial,
    "Algoritmo genético": secciones.algoritmo_genetico,
    "Análisis funcional": secciones.analisis_funcional,
    "Secuencial vs. paralelo": secciones.paralelo,
    "Comparación": secciones.comparacion,
    "Historial": secciones.historial,
}


def main() -> None:
    st.set_page_config(page_title="Plan MotoRX-7", layout="wide")
    st.sidebar.title("Plan MotoRX-7")
    opcion = st.sidebar.radio("Menú principal", list(SECCIONES))
    SECCIONES[opcion]()


if __name__ == "__main__":
    main()
