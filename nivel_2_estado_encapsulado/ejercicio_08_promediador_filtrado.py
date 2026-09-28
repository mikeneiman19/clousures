"""
Ejercicio 8 - Promediador con Eliminacion de Valores Extremos
crear_promediador_filtrado(filtro_ruido_lambda) acumula datos de forma privada
y aplica la lambda para descartar valores atipicos antes de recalcular el
promedio.
"""


def crear_promediador_filtrado(filtro_ruido_lambda):
    datos = []

    def promediar(valor):
        datos.append(valor)
        datos_limpios = [d for d in datos if filtro_ruido_lambda(d)]
        if not datos_limpios:
            return 0
        return sum(datos_limpios) / len(datos_limpios)
    return promediar


if __name__ == "__main__":
    promediador = crear_promediador_filtrado(lambda v: 0 <= v <= 100)

    print("Ejercicio 8:", promediador(50), promediador(999), promediador(70))
