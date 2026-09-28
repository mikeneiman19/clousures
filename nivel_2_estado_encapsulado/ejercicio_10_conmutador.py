"""
Ejercicio 10 - Interruptor Multiple (Maquina de Estados Ligera)
crear_conmutador(lista_estados) alterna ciclicamente entre una lista de estados
internos privados en cada llamada.
"""


def crear_conmutador(lista_estados):
    indice = -1

    def siguiente_estado():
        nonlocal indice
        indice = (indice + 1) % len(lista_estados)
        return lista_estados[indice]
    return siguiente_estado


if __name__ == "__main__":
    semaforo = crear_conmutador(["verde", "amarillo", "rojo"])

    print("Ejercicio 10:", semaforo(), semaforo(), semaforo(), semaforo())
