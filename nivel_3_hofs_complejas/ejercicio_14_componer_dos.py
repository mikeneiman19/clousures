"""
Ejercicio 14 - Compositor de Cadenas de Operaciones
componer_dos(f, g) devuelve un closure que aplica f(g(x)).
"""


def componer_dos(f, g):
    def compuesta(x):
        return f(g(x))
    return compuesta


if __name__ == "__main__":
    combinada = componer_dos(lambda x: x + 1, lambda x: x * 2)

    print("Ejercicio 14:", combinada(5))  # f(g(5)) = (5 * 2) + 1
