"""
Ejercicio 12 - Reductor / Agrupador Personalizado
agrupar_por(lista, fn_clave) agrupa una coleccion de diccionarios en un
diccionario clave-valor segun el resultado de fn_clave.
"""


def agrupar_por(lista, fn_clave):
    grupos = {}
    for item in lista:
        clave = fn_clave(item)
        grupos.setdefault(clave, []).append(item)
    return grupos


if __name__ == "__main__":
    personas = [
        {"nombre": "Ana", "ciudad": "Quito"},
        {"nombre": "Luis", "ciudad": "Guayaquil"},
        {"nombre": "Sofia", "ciudad": "Quito"},
    ]

    print("Ejercicio 12:", agrupar_por(personas, lambda p: p["ciudad"]))
