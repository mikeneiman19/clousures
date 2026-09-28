# Taller Practico de Alto Nivel: Programacion Funcional en Python

**Diseno de Arquitecturas Funcionales: HOFs, Closures Avanzados y Composicion con Lambdas**

| | |
|---|---|
| **Estudiante** | _Tu nombre completo_ |
| **Institucion** | _Nombre de tu institucion_ |
| **Materia** | _Nombre de la materia_ |
| **Docente** | _Nombre del docente_ |
| **Fecha** | _dd/mm/aaaa_ |

---

## Descripcion

Este repositorio contiene la solucion de los **20 ejercicios** del taller, organizados en 4 niveles de dificultad. Todos los ejercicios integran los patrones funcionales centrales del taller:

- **HOF (Funcion de Orden Superior):** funciones que reciben otras funciones como argumento o retornan una funcion.
- **Lambda:** funciones anonimas que se inyectan como comportamiento dinamico.
- **Closure:** funciones internas que recuerdan (encapsulan) el estado de la funcion que las creo.
- **`nonlocal`:** permite que un closure modifique su estado privado entre llamadas.

## Estructura del repositorio

```
Taller_Programacion_Funcional/
|
|-- README.md
|
|-- nivel_1_closures/
|   |-- ejercicio_01_formateador.py
|   |-- ejercicio_02_operador.py
|   |-- ejercicio_03_descuento_dinamico.py
|   |-- ejercicio_04_generador_sufijos.py
|   `-- ejercicio_05_conversor.py
|
|-- nivel_2_estado_encapsulado/
|   |-- ejercicio_06_contador_paso.py
|   |-- ejercicio_07_acumulador_validado.py
|   |-- ejercicio_08_promediador_filtrado.py
|   |-- ejercicio_09_limitador_avanzado.py
|   `-- ejercicio_10_conmutador.py
|
|-- nivel_3_hofs_complejas/
|   |-- ejercicio_11_procesar_coleccion.py
|   |-- ejercicio_12_agrupar_por.py
|   |-- ejercicio_13_ejecutar_y_rastrear.py
|   |-- ejercicio_14_componer_dos.py
|   `-- ejercicio_15_auditar_ejecucion.py
|
`-- nivel_4_patrones_avanzados/
    |-- ejercicio_16_validador_multiple.py
    |-- ejercicio_17_memoizar_avanzado.py
    |-- ejercicio_18_pipeline.py
    |-- ejercicio_19_sistema_eventos.py
    `-- ejercicio_20_consultor.py
```

## Ejercicios

### Nivel 1: Closures con Inyeccion de Comportamiento

| # | Funcion | Descripcion | Archivo |
|---|---------|-------------|---------|
| 1 | `crear_formateador(prefijo, fn_transformacion)` | Closure que transforma un texto con una lambda y le antepone un prefijo. | [ejercicio_01](nivel_1_closures/ejercicio_01_formateador.py) |
| 2 | `crear_operador(factor, operacion_lambda)` | Closure que aplica una operacion usando el factor encapsulado. | [ejercicio_02](nivel_1_closures/ejercicio_02_operador.py) |
| 3 | `crear_descuento_dinamico(regla_condicional_lambda)` | Closure que aplica un descuento prefijado si la lambda se cumple. | [ejercicio_03](nivel_1_closures/ejercicio_03_descuento_dinamico.py) |
| 4 | `crear_generador_sufijos(patron_lambda)` | Closure que genera nombres de archivo unicos segun un patron. | [ejercicio_04](nivel_1_closures/ejercicio_04_generador_sufijos.py) |
| 5 | `crear_conversor(tasa, margen_lambda)` | Closure que convierte montos y calcula la comision dinamicamente. | [ejercicio_05](nivel_1_closures/ejercicio_05_conversor.py) |

### Nivel 2: Estado Encapsulado Avanzado (`nonlocal` + Lambdas)

| # | Funcion | Descripcion | Archivo |
|---|---------|-------------|---------|
| 6 | `crear_contador_paso(fn_paso)` | Contador cuyo incremento lo define una lambda. | [ejercicio_06](nivel_2_estado_encapsulado/ejercicio_06_contador_paso.py) |
| 7 | `crear_acumulador_validado(criterio_lambda)` | Acumulador privado que solo suma valores que pasan el criterio. | [ejercicio_07](nivel_2_estado_encapsulado/ejercicio_07_acumulador_validado.py) |
| 8 | `crear_promediador_filtrado(filtro_ruido_lambda)` | Promediador que descarta valores atipicos con una lambda. | [ejercicio_08](nivel_2_estado_encapsulado/ejercicio_08_promediador_filtrado.py) |
| 9 | `crear_limitador_avanzado(max_intentos, fn_alerta)` | Rate limiter con alerta al superar el limite y funcion de reset. | [ejercicio_09](nivel_2_estado_encapsulado/ejercicio_09_limitador_avanzado.py) |
| 10 | `crear_conmutador(lista_estados)` | Maquina de estados que alterna ciclicamente entre estados. | [ejercicio_10](nivel_2_estado_encapsulado/ejercicio_10_conmutador.py) |

### Nivel 3: HOFs Complejas combinadas con Closures y Lambdas

| # | Funcion | Descripcion | Archivo |
|---|---------|-------------|---------|
| 11 | `procesar_coleccion(lista, fn_predicado, fn_transformacion)` | Combina `filter` y `map` con lambdas. | [ejercicio_11](nivel_3_hofs_complejas/ejercicio_11_procesar_coleccion.py) |
| 12 | `agrupar_por(lista, fn_clave)` | Agrupa diccionarios en un dict segun una lambda de clave. | [ejercicio_12](nivel_3_hofs_complejas/ejercicio_12_agrupar_por.py) |
| 13 | `ejecutar_y_rastrear(fn_tarea, n)` | Ejecuta una tarea N veces y expone su historial mediante un closure. | [ejercicio_13](nivel_3_hofs_complejas/ejercicio_13_ejecutar_y_rastrear.py) |
| 14 | `componer_dos(f, g)` | Compone dos funciones: `f(g(x))`. | [ejercicio_14](nivel_3_hofs_complejas/ejercicio_14_componer_dos.py) |
| 15 | `auditar_ejecucion(fn_objetivo, fn_logger)` | Mide el tiempo de ejecucion y envia el informe al logger. | [ejercicio_15](nivel_3_hofs_complejas/ejercicio_15_auditar_ejecucion.py) |

### Nivel 4: Patrones Avanzados de Arquitectura Funcional

| # | Funcion | Descripcion | Archivo |
|---|---------|-------------|---------|
| 16 | `crear_validador_multiple(*lambdas_criterios)` | Valida que un objeto cumpla todas las reglas dadas. | [ejercicio_16](nivel_4_patrones_avanzados/ejercicio_16_validador_multiple.py) |
| 17 | `memoizar_avanzado(fn_costosa, max_items)` | Cache con capacidad maxima (elimina la entrada mas antigua). | [ejercicio_17](nivel_4_patrones_avanzados/ejercicio_17_memoizar_avanzado.py) |
| 18 | `crear_pipeline(*funciones_transformacion)` | Hace fluir un dato por una secuencia de funciones (middleware). | [ejercicio_18](nivel_4_patrones_avanzados/ejercicio_18_pipeline.py) |
| 19 | `crear_sistema_eventos()` | Sistema Pub/Sub para suscribir lambdas y emitir eventos. | [ejercicio_19](nivel_4_patrones_avanzados/ejercicio_19_sistema_eventos.py) |
| 20 | `crear_consultor(campo)` | Mini motor de consultas con filtros dinamicos sobre listas de diccionarios. | [ejercicio_20](nivel_4_patrones_avanzados/ejercicio_20_consultor.py) |

## Requisitos

- Python 3.8 o superior.
- No se necesitan librerias externas: solo se usan `time` y `functools` de la biblioteca estandar.

## Como ejecutar

Clona el repositorio y ejecuta cualquier ejercicio desde la raiz del proyecto:

```bash
git clone https://github.com/TU_USUARIO/Taller_Programacion_Funcional.git
cd Taller_Programacion_Funcional

python nivel_1_closures/ejercicio_01_formateador.py
python nivel_4_patrones_avanzados/ejercicio_19_sistema_eventos.py
```

Cada archivo incluye al final un bloque `if __name__ == "__main__":` con pruebas de ejecucion mediante `print()` que verifican el comportamiento del ejercicio.

Para ejecutar todos los ejercicios de una vez:

```bash
# Windows (PowerShell)
Get-ChildItem -Recurse -Filter "ejercicio_*.py" | ForEach-Object { python $_.FullName }

# Linux / macOS
for f in nivel_*/ejercicio_*.py; do python3 "$f"; done
```

## Ejemplo de salida

```
Ejercicio 3: 135.0 | 50
Ejercicio 9: True True False
Ejercicio 11: [4, 16, 36, 64, 100]
Ejercicio 14: 11
Ejercicio 18: hola_mundo_funcional
```

## Autor

_Tu nombre_ - _tu correo o usuario de GitHub_
