"""
Ejercicio 3 - Calculador de Descuentos con Regla Dinamica
crear_descuento_dinamico(regla_condicional_lambda) devuelve un closure que
evalua el precio con la lambda para decidir si aplica un descuento prefijado.
"""


def crear_descuento_dinamico(regla_condicional_lambda):
    DESCUENTO = 0.10  # descuento prefijado del 10%

    def calcular(precio):
        if regla_condicional_lambda(precio):
            return round(precio * (1 - DESCUENTO), 2)
        return precio
    return calcular


if __name__ == "__main__":
    descuento = crear_descuento_dinamico(lambda precio: precio > 100)

    print("Ejercicio 3:", descuento(150), "|", descuento(50))
