"""
Ejercicio 20 - Mini-Query Engine sobre Listas de Objetos
crear_consultor(campo) devuelve una HOF que genera filtros dinamicos sobre
listas de diccionarios mediante expresiones lambda.
"""


def crear_consultor(campo):
    def generar_filtro(operador_lambda, valor_comparar):
        def filtro(lista_objetos):
            return [obj for obj in lista_objetos if operador_lambda(obj.get(campo), valor_comparar)]
        return filtro
    return generar_filtro


if __name__ == "__main__":
    productos = [
        {"nombre": "Laptop", "precio": 800},
        {"nombre": "Mouse", "precio": 15},
        {"nombre": "Monitor", "precio": 250},
    ]

    consultor_precio = crear_consultor("precio")
    filtro_caros = consultor_precio(lambda valor, comparar: valor > comparar, 100)
    filtro_baratos = consultor_precio(lambda valor, comparar: valor <= comparar, 100)

    print("Ejercicio 20 (caros):", filtro_caros(productos))
    print("Ejercicio 20 (baratos):", filtro_baratos(productos))
