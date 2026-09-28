"""
Ejercicio 5 - Conversor de Divisas con Margen
crear_conversor(tasa, margen_lambda) retorna una funcion que convierte montos
calculando dinamicamente la comision adicional.
"""


def crear_conversor(tasa, margen_lambda):
    def convertir(monto):
        bruto = monto * tasa
        comision = margen_lambda(monto)
        return round(bruto - comision, 2)
    return convertir


if __name__ == "__main__":
    conversor = crear_conversor(0.92, lambda monto: monto * 0.02)

    print("Ejercicio 5:", conversor(100))
    print("Ejercicio 5:", conversor(250))
