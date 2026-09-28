"""
Ejercicio 17 - Cache con Tamano Maximo (Memoizacion Profesional)
memoizar_avanzado(fn_costosa, max_items) retorna un closure que controla el
estado privado de una memoria cache con limite de capacidad. Al llenarse,
elimina la entrada mas antigua.
"""

import time


def memoizar_avanzado(fn_costosa, max_items):
    cache = {}
    orden_insercion = []

    def envoltura(*args):
        if args in cache:
            return cache[args]
        resultado = fn_costosa(*args)
        cache[args] = resultado
        orden_insercion.append(args)
        if len(orden_insercion) > max_items:
            clave_vieja = orden_insercion.pop(0)
            del cache[clave_vieja]
        return resultado
    return envoltura


def cuadrado_lento(x):
    time.sleep(0.05)
    return x * x


if __name__ == "__main__":
    cuadrado_memo = memoizar_avanzado(cuadrado_lento, max_items=2)

    print("Ejercicio 17:", cuadrado_memo(4), cuadrado_memo(5), cuadrado_memo(4), cuadrado_memo(6))
