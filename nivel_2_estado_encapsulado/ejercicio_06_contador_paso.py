"""
Ejercicio 6 - Contador Ponderado
crear_contador_paso(fn_paso) incrementa su estado interno usando la lambda
fn_paso(cuenta_actual) en lugar de un incremento fijo.
"""


def crear_contador_paso(fn_paso):
    cuenta = 0

    def incrementar():
        nonlocal cuenta
        cuenta = fn_paso(cuenta)
        return cuenta
    return incrementar


if __name__ == "__main__":
    contador = crear_contador_paso(lambda actual: actual + 2)
    duplicador = crear_contador_paso(lambda actual: actual * 2 if actual else 1)

    print("Ejercicio 6:", contador(), contador(), contador())
    print("Ejercicio 6:", duplicador(), duplicador(), duplicador(), duplicador())
