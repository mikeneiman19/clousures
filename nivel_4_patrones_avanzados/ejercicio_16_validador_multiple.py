"""
Ejercicio 16 - Validador Compuesto de Reglas de Negocio
crear_validador_multiple(*lambdas_criterios) retorna un closure que evalua si
un objeto cumple todas las reglas pasadas como argumento.
"""


def crear_validador_multiple(*lambdas_criterios):
    def validar(objeto):
        return all(criterio(objeto) for criterio in lambdas_criterios)
    return validar


if __name__ == "__main__":
    validar_usuario = crear_validador_multiple(
        lambda u: len(u.get("nombre", "")) > 0,
        lambda u: u.get("edad", 0) >= 18,
        lambda u: "@" in u.get("email", ""),
    )

    print("Ejercicio 16:", validar_usuario({"nombre": "Carlos", "edad": 25, "email": "c@mail.com"}))
    print("Ejercicio 16:", validar_usuario({"nombre": "Ana", "edad": 15, "email": "a@mail.com"}))
