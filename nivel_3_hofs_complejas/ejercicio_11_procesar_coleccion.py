"""
Ejercicio 11 - Pipeline de Mapeo y Filtrado Combinado
procesar_coleccion(lista, fn_predicado, fn_transformacion) combina filter y map.
"""


def procesar_coleccion(lista, fn_predicado, fn_transformacion):
    return list(map(fn_transformacion, filter(fn_predicado, lista)))


if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("Ejercicio 11:", procesar_coleccion(numeros, lambda x: x % 2 == 0, lambda x: x ** 2))
    print("Ejercicio 11:", procesar_coleccion(["ana", "luis", "sofia"], lambda s: len(s) > 3, lambda s: s.upper()))
