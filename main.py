import time
from clases.Usuario import Persona
from clases.acuaticos import Acuatico
from clases.Electronicos import JuegoElectronico
from clases.mecanicos import Mecanicas
from clases.fisicos import JuegosFisicos
from clases.Atracciones import (
    juegos_acuaticos,
    juegos_electronicos,
    juegos_mecanicos,
    juegos_fisicos,
)


def registrar_personas() -> list[Persona]:
    cantidad = int(
        input("Hola, tú eres el titular del grupo. ¿Cuántas personas vas a registrar? ")
    )
    personas = []

    for i in range(cantidad):
        print(f"\nPersona {i + 1}:")
        nombre = input("  Nombre: ").strip()
        edad = int(input("  Edad: "))
        estatura = float(input("  Estatura (metros): "))
        peso = float(input("  Peso (kg): "))

        personas.append(Persona(nombre, edad, estatura, peso))
        print(f"  {nombre} registrado!")

    return personas


# ─── SEDES ────────────────────────────────────────────────


def menu_acuaticos(grupo, juegos):
    opcion = ""
    while opcion != str(len(juegos) + 1):
        print("\n¿A cuál juego acuático quieres entrar?")
        for i, juego in enumerate(juegos, 1):
            print(f"{i}. {juego.nombre}")
        print(f"{len(juegos) + 1}. Volver al menú principal")

        opcion = input("\nElige una opción: ").strip()

        if opcion.isdigit() and 1 <= int(opcion) <= len(juegos):
            juegos[int(opcion) - 1].iniciar_atraccion_grupo(grupo)
        elif opcion != str(len(juegos) + 1):
            print(
                f"No ingresó un número válido, vuélvalo a intentar del 1 al {len(juegos) + 1}."
            )


def menu_electronicos(grupo, juegos):
    opcion = ""
    while opcion != str(len(juegos) + 1):
        print("\n¿A cuál juego electrónico quieres entrar?")
        for i, juego in enumerate(juegos, 1):
            print(f"{i}. {juego.nombre}")
        print(f"{len(juegos) + 1}. Volver al menú principal")

        opcion = input("\nElige una opción: ").strip()

        if opcion.isdigit() and 1 <= int(opcion) <= len(juegos):
            juegos[int(opcion) - 1].iniciar_juego_grupo(grupo)
        elif opcion != str(len(juegos) + 1):
            print(
                f"No ingresó un número válido, vuélvalo a intentar del 1 al {len(juegos) + 1}."
            )


def menu_mecanicos(grupo, juegos):
    metodos = ["entrar_montana", "entrar_rueda", "entrar_barco", "entrar_carros"]
    opcion = ""
    while opcion != str(len(juegos) + 1):
        print("\n¿A cuál juego mecánico quieres entrar?")
        for i, juego in enumerate(juegos, 1):
            print(f"{i}. {juego.nombre}")
        print(f"{len(juegos) + 1}. Volver al menú principal")

        opcion = input("\nElige una opción: ").strip()

        if opcion.isdigit() and 1 <= int(opcion) <= len(juegos):
            juego = juegos[int(opcion) - 1]
            getattr(juego, metodos[int(opcion) - 1])(grupo)
        elif opcion != str(len(juegos) + 1):
            print(
                f"No ingresó un número válido, vuélvalo a intentar del 1 al {len(juegos) + 1}."
            )


def menu_fisicos(grupo, juegos):
    metodos = ["entrar_tirolesa", "entrar_muro", "entrar_salto", "entrar_tiro_arco"]
    opcion = ""
    while opcion != str(len(juegos) + 1):
        print("\n¿A cuál juego físico quieres entrar?")
        for i, juego in enumerate(juegos, 1):
            print(f"{i}. {juego.nombre_juego}")
        print(f"{len(juegos) + 1}. Volver al menú principal")

        opcion = input("\nElige una opción: ").strip()

        if opcion.isdigit() and 1 <= int(opcion) <= len(juegos):
            juego = juegos[int(opcion) - 1]
            getattr(juego, metodos[int(opcion) - 1])(grupo)
        elif opcion != str(len(juegos) + 1):
            print(
                f"No ingresó un número válido, vuélvalo a intentar del 1 al {len(juegos) + 1}."
            )


def menu_sedes(
    grupo, juegos_acuaticos, juegos_electronicos, juegos_mecanicos, juegos_fisicos
):
    opcion = ""
    while opcion != "5":
        print("\n¿A cuál sede vas a entrar?")
        print("1. Mecánicos")
        print("2. Electrónicos")
        print("3. Acuáticos")
        print("4. Físicos")
        print("5. Salir de las sedes")

        opcion = input("\nElige una opción: ").strip()

        if opcion == "1":
            menu_mecanicos(grupo, juegos_mecanicos)
        elif opcion == "2":
            menu_electronicos(grupo, juegos_electronicos)
        elif opcion == "3":
            menu_acuaticos(grupo, juegos_acuaticos)
        elif opcion == "4":
            menu_fisicos(grupo, juegos_fisicos)
        elif opcion != "5":
            print("No ingresó un número válido, vuélvalo a intentar del 1 al 5.")


def menu_principal(
    grupo, juegos_acuaticos, juegos_electronicos, juegos_mecanicos, juegos_fisicos
):
    opcion = ""
    while opcion != "2":
        print("\n¿Qué quieres hacer?")
        print("1. Elegir sede")
        print("2. Salir del parque")

        opcion = input("\nElige una opción: ").strip()

        if opcion == "1":
            menu_sedes(
                grupo,
                juegos_acuaticos,
                juegos_electronicos,
                juegos_mecanicos,
                juegos_fisicos,
            )
        elif opcion == "2":
            print("Hasta luego!")
        else:
            print("Teclea un número ya sea 1 o 2 para recibir atención ;)")


def main():
    grupo = registrar_personas()
    menu_principal(
        grupo, juegos_acuaticos, juegos_electronicos, juegos_mecanicos, juegos_fisicos
    )


main()
