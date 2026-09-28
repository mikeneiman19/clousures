"""
Ejercicio 4 - Generador de Seriales / Nombres Unicos
crear_generador_sufijos(patron_lambda) devuelve un closure que transforma
nombres de archivo segun una lambda de formato.
"""


def crear_generador_sufijos(patron_lambda):
    contador = 0

    def generar(nombre_base):
        nonlocal contador
        contador += 1
        return patron_lambda(nombre_base, contador)
    return generar


if __name__ == "__main__":
    generador = crear_generador_sufijos(lambda nombre, n: f"{nombre}_backup_{n:03d}")

    print("Ejercicio 4:", generador("reporte"), "|", generador("reporte"))
