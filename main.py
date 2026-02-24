import time
from clases.Usuario import Persona
from clases.acuaticos import Acuatico, RioLento, BotesChocones


def registrar_personas() -> list[Persona]:
    cantidad = int(input("Hola, tú eres el titular del grupo. ¿Cuántas personas vas a registrar? "))
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


def menu(grupo: list[Persona], tobogan: Acuatico):
    opcion = ""

    while opcion != "3":
        print("\n¿Qué quieres hacer?")
        print("1. Ingresar al parque con tus integrantes")
        print("2. Elegir sede")
        print("3. Salir")

        opcion = input("\nElige una opción: ").strip()

        if opcion == "1":
            tobogan.iniciar_atraccion_grupo(grupo)
        elif opcion == "2":
            print("Trabajando en ello...")
        elif opcion == "3":
            print("Hasta luego!")
        else:
            print("Teclea un número del 1 al 3 para recibir alguna atención. :)")


def main():
    tobogan = Acuatico(
        nombre="Tobogán del Dragón",
        capacidad=3,
        profundidad=1.70,
        propulsion="Gravedad",
        estatura_minima=1.20,
        edad_minima=8,
    )
    rio = RioLento(
        nombre="Río Amazonas",
        capacidad=10,
        profundidad=0.8,
        estatura_minima=1.0,
        edad_minima=5,
    )
    botes = BotesChocones(
        nombre="Botes Locos",
        capacidad=6,
        profundidad=1.0,
        estatura_minima=1.1,
        edad_minima=7,
    )

    grupo = registrar_personas()
    menu(grupo, tobogan)


main()
