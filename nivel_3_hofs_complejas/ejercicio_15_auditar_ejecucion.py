"""
Ejercicio 15 - Decorador / HOF de Profiling y Auditoria
auditar_ejecucion(fn_objetivo, fn_logger) mide el tiempo de ejecucion y envia
el informe al closure/lambda de logging pasado por parametro.
"""

import time


def auditar_ejecucion(fn_objetivo, fn_logger):
    def envoltura(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = fn_objetivo(*args, **kwargs)
        duracion = time.perf_counter() - inicio
        fn_logger({
            "funcion": fn_objetivo.__name__,
            "duracion_seg": duracion,
            "resultado": resultado,
        })
        return resultado
    return envoltura


def tarea_pesada(n):
    return sum(range(n))


if __name__ == "__main__":
    tarea_auditada = auditar_ejecucion(tarea_pesada, lambda info: print("   Informe:", info))

    print("Ejercicio 15:", tarea_auditada(100000))
