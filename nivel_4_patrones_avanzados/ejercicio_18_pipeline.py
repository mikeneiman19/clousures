"""
Ejercicio 18 - Motor de Pipeline Secuencial (Middleware)
crear_pipeline(*funciones_transformacion) permite pasar un dato inicial y
hacerlo fluir en orden por todas las funciones del pipeline.
"""

from functools import reduce


def crear_pipeline(*funciones_transformacion):
    def ejecutar_pipeline(dato_inicial):
        return reduce(lambda dato, funcion: funcion(dato), funciones_transformacion, dato_inicial)
    return ejecutar_pipeline


if __name__ == "__main__":
    pipeline = crear_pipeline(
        lambda t: t.strip(),
        lambda t: t.lower(),
        lambda t: t.replace(" ", "_"),
    )

    print("Ejercicio 18:", pipeline("   Hola Mundo Funcional   "))
