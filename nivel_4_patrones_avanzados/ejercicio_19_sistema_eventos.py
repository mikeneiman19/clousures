"""
Ejercicio 19 - Sistema Pub/Sub (Event Listener)
crear_sistema_eventos() devuelve un closure gestor capaz de registrar
suscriptores (lambdas) y emitir eventos notificando a cada uno.
"""


def crear_sistema_eventos():
    suscriptores = {}

    def suscribirse(nombre_evento, callback):
        suscriptores.setdefault(nombre_evento, []).append(callback)

    def emitir(nombre_evento, *args, **kwargs):
        for callback in suscriptores.get(nombre_evento, []):
            callback(*args, **kwargs)

    def gestor(accion, *args, **kwargs):
        if accion == "suscribir":
            return suscribirse(*args, **kwargs)
        elif accion == "emitir":
            return emitir(*args, **kwargs)
        raise ValueError("Accion no reconocida: usa 'suscribir' o 'emitir'")
    return gestor


if __name__ == "__main__":
    eventos = crear_sistema_eventos()
    eventos("suscribir", "usuario_creado", lambda nombre: print(f"   Bienvenida a {nombre}"))
    eventos("suscribir", "usuario_creado", lambda nombre: print(f"   Log: se creo el usuario {nombre}"))

    print("Ejercicio 19: emitiendo evento 'usuario_creado'")
    eventos("emitir", "usuario_creado", "Maria")
