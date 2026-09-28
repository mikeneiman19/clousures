"""
Ejercicio 9 - Limitador de Tasa Inteligente (Rate Limiter con Reset)
crear_limitador_avanzado(max_intentos, fn_alerta) cuenta ejecuciones privadas y
ejecuta fn_alerta cuando el limite es superado. Devuelve tambien una funcion
para reiniciar el contador.
"""


def crear_limitador_avanzado(max_intentos, fn_alerta):
    intentos = 0

    def ejecutar():
        nonlocal intentos
        intentos += 1
        if intentos > max_intentos:
            fn_alerta(intentos)
            return False
        return True

    def reiniciar():
        nonlocal intentos
        intentos = 0

    return ejecutar, reiniciar


if __name__ == "__main__":
    limitador, reiniciar = crear_limitador_avanzado(
        2, lambda intentos: print(f"   Limite superado en intento {intentos}")
    )

    print("Ejercicio 9:", limitador(), limitador(), limitador())
    reiniciar()
    print("Ejercicio 9 (despues del reset):", limitador())
