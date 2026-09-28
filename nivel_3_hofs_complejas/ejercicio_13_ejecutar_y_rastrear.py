"""
Ejercicio 13 - Ejecutor Repetitivo con Estado Accesible
ejecutar_y_rastrear(fn_tarea, n) retorna un closure con el historial de
resultados de haber ejecutado fn_tarea N veces.
"""


def ejecutar_y_rastrear(fn_tarea, n):
    historial = []
    for i in range(n):
        historial.append(fn_tarea(i))

    def obtener_historial():
        return list(historial)
    return obtener_historial


if __name__ == "__main__":
    obtener = ejecutar_y_rastrear(lambda i: i ** 2, 5)

    print("Ejercicio 13:", obtener())
