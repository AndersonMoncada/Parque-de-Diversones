import time
from clases.Usuario import Persona
from clases.acuaticos import Acuatico, RioLento, BotesChocones
from clases.Electronicos import JuegoElectronico, SimuladorVR, JuegoArcade, ShooterFPS


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


def menu_acuaticos(grupo: list[Persona], juegos: list[Acuatico]):
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


def menu_electronicos(grupo: list[Persona], juegos: list[JuegoElectronico]):
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


def menu_sedes(grupo, juegos_acuaticos, juegos_electronicos):
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
            print("Trabajando en ello...")
        elif opcion == "2":
            menu_electronicos(grupo, juegos_electronicos)
        elif opcion == "3":
            menu_acuaticos(grupo, juegos_acuaticos)
        elif opcion == "4":
            print("Trabajando en ello...")
        elif opcion != "5":
            print("No ingresó un número válido, vuélvalo a intentar del 1 al 5.")


# ─── MENÚ PRINCIPAL ───────────────────────────────────────


def menu_principal(grupo, juegos_acuaticos, juegos_electronicos):
    opcion = ""

    while opcion != "2":
        print("\n¿Qué quieres hacer?")
        print("1. Elegir sede")
        print("2. Salir del parque")

        opcion = input("\nElige una opción: ").strip()

        if opcion == "1":
            menu_sedes(grupo, juegos_acuaticos, juegos_electronicos)
        elif opcion == "2":
            print("Hasta luego!")
        else:
            print("Teclea un número ya sea 1 o 2 para recibir atención ;)")


# ─── MAIN ─────────────────────────────────────────────────


def main():
    juegos_acuaticos = [
        Acuatico(
            nombre="Tobogán del Dragón",
            capacidad=3,
            profundidad=1.70,
            propulsion="Gravedad",
            estatura_minima=1.20,
            edad_minima=8,
        ),
        RioLento(
            nombre="Río Peligro",
            capacidad=10,
            profundidad=0.8,
            estatura_minima=1.0,
            edad_minima=5,
        ),
        BotesChocones(
            nombre="Botes Locos",
            capacidad=6,
            profundidad=1.0,
            estatura_minima=1.1,
            edad_minima=7,
        ),
    ]

    juegos_electronicos = [
        SimuladorVR(
            nombre="Simulación Apocalipsis Zombie",
            capacidad=4,
            duracion=10,
            edad_minima=12,
            estatura_minima=1.30,
        ),
        ShooterFPS(
            nombre="Doom Arcade",
            capacidad=1,
            duracion=15,
            edad_minima=15,
            estatura_minima=1.40,
        ),
        JuegoArcade(
            nombre="Tetris Versus",
            capacidad=2,
            duracion=20,
            edad_minima=5,
            estatura_minima=1.20,
        ),
    ]

    grupo = registrar_personas()
    menu_principal(grupo, juegos_acuaticos, juegos_electronicos)


main()
