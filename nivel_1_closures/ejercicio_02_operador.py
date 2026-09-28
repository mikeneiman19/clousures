"""
Ejercicio 2 - Multiplicador Parametrico con Mapeo
crear_operador(factor, operacion_lambda) devuelve un closure que aplica la
operacion recibida usando el factor encapsulado.
"""


def crear_operador(factor, operacion_lambda):
    def operar(valor):
        return operacion_lambda(valor, factor)
    return operar


if __name__ == "__main__":
    multiplicar_y_sumar = crear_operador(3, lambda valor, factor: valor * factor + 1)
    potencia = crear_operador(2, lambda valor, factor: valor ** factor)

    print("Ejercicio 2:", multiplicar_y_sumar(5))
    print("Ejercicio 2:", potencia(4))
