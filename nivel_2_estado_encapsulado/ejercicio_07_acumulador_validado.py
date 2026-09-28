"""
Ejercicio 7 - Acumulador con Filtro de Aceptacion
crear_acumulador_validado(criterio_lambda) mantiene un total privado y solo
suma los valores que superan la prueba de la lambda.
"""


def crear_acumulador_validado(criterio_lambda):
    total = 0

    def acumular(valor):
        nonlocal total
        if criterio_lambda(valor):
            total += valor
        return total
    return acumular


if __name__ == "__main__":
    acumulador = crear_acumulador_validado(lambda v: v > 0)

    print("Ejercicio 7:", acumulador(10), acumulador(-5), acumulador(20))
