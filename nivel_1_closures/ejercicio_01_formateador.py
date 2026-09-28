"""
Ejercicio 1 - Generador de Formateadores con Transformacion
crear_formateador(prefijo, fn_transformacion) devuelve un closure que aplica
la transformacion al texto y le concatena el prefijo.
"""


def crear_formateador(prefijo, fn_transformacion):
    def formatear(texto):
        return f"{prefijo}{fn_transformacion(texto)}"
    return formatear


if __name__ == "__main__":
    formateador_mayus = crear_formateador("[LOG] ", lambda t: t.upper())
    formateador_titulo = crear_formateador(">> ", lambda t: t.title())

    print("Ejercicio 1:", formateador_mayus("mensaje de prueba"))
    print("Ejercicio 1:", formateador_titulo("hola mundo funcional"))
