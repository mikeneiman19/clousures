"""
Ejecuta todos los ejercicios del taller, nivel por nivel.

Uso:
    python main.py
"""

import runpy
from pathlib import Path

RAIZ = Path(__file__).parent

for carpeta in sorted(RAIZ.glob("nivel_*")):
    print("=" * 60)
    print(carpeta.name.upper())
    print("=" * 60)
    for archivo in sorted(carpeta.glob("ejercicio_*.py")):
        # run_name="__main__" hace que se ejecute el bloque de pruebas de cada archivo
        runpy.run_path(str(archivo), run_name="__main__")
    print()
