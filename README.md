# Plan MotoRX-7

Sistema de planificación y optimización de recursos para el Taller Mecánico Seis Pistones
(caso ficticio). Proyecto final del curso SC-250 Paradigmas de Programación, Universidad Fidélitas.

El sistema administra recursos (mecánicos, equipos y bahías) y actividades (servicios del taller),
valida restricciones con un motor de reglas, genera una planificación inicial con una heurística
greedy, la optimiza con un algoritmo genético propio, analiza los resultados con programación
funcional y compara la ejecución secuencial con la paralela.

## Requisitos

- Python 3.12 o superior
- Git

## Instalación

```bash
git clone https://github.com/DiegoSalazarArtavia/MotoRX-7.git
cd MotoRX-7
python -m venv .venv
```

Activar el entorno virtual:

- Windows: `.venv\Scripts\activate`
- macOS / Linux: `source .venv/bin/activate`

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
streamlit run app.py
```

## Pruebas

```bash
pytest
```

## Estructura

```
MotoRX-7/
├── app.py                      Punto de entrada (Streamlit)
├── motorx7/
│   ├── dominio/                Recursos, actividades, planificación, escenario, dependencias y excepciones
│   ├── reglas/                 Restricciones duras, retrasos y motor de validación
│   ├── algoritmos/             Programador de actividades, greedy, genético, aptitud y decodificador
│   ├── funcional/              Transformaciones y métricas con funciones puras
│   ├── paralelo/               Comparación secuencial / paralela
│   ├── comparacion/            Métricas y comparación entre ejecuciones
│   ├── escenarios/             Generación reproducible e importación de escenarios
│   ├── persistencia/           Serialización y repositorio SQLite
│   └── interfaz/               Secciones de la interfaz (sin lógica de negocio)
├── tests/                      Pruebas automatizadas (pytest)
├── datos/                      Escenarios y resultados guardados
└── docs/                       Documentación técnica y artículo
```

Las dependencias entre módulos van en una sola dirección: `interfaz` usa a todos los demás,
`algoritmos` usa `reglas` y `dominio`, y `dominio` no depende de ningún otro módulo.
Así el motor de reglas y los algoritmos se pueden ejecutar y probar sin la interfaz.

## Organización del equipo

| Integrante | Módulos |
|---|---|
| David Steven López Castillo | `algoritmos/programador.py`, `algoritmos/greedy.py`, `algoritmos/resultado.py`, `interfaz/`, `app.py`, integración |
| Gabriel Alberto Sanabria Naranjo | `dominio/`, `persistencia/` |
| Austin Gabriel Badilla Valerio | `reglas/`, `escenarios/` |
| Jefry Ricardo Granados Baltodano | `algoritmos/genetico.py`, `algoritmos/decodificador.py`, `algoritmos/fitness.py` |
| Diego Alonso Salazar Artavia | `funcional/`, `paralelo/`, `comparacion/` |

Cada integrante escribe las pruebas de sus módulos en `tests/` (`test_<modulo>.py`).

## Forma de trabajo con Git

1. Nadie trabaja directamente sobre `main`.
2. Cada integrante crea una rama para su trabajo: `git checkout -b nombre/tema`
   (por ejemplo `diego/funcional`).
3. Antes de subir cambios, correr `pytest` y verificar que todo pase.
4. Subir la rama (`git push -u origin nombre/tema`) y abrir un Pull Request hacia `main`.
5. Otro integrante revisa el Pull Request antes de integrarlo.
6. Las firmas de las funciones y clases compartidas (lo que recibe y lo que devuelve cada una)
   no se cambian sin avisar al grupo, porque otros módulos dependen de ellas.
