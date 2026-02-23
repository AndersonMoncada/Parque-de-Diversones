import time
from clases.Usuario import Persona
from clases.acuaticos import Acuatico


def crear_personas_interactivo() -> list[Persona]:
    """Crea personas de forma interactiva."""
    personas = []

    print("\n" + "=" * 20)
    print(" REGISTRO DE VISITANTES")
    print("=" * 20)

    while True:
        print(f"\nPersona #{len(personas) + 1}")
        print("─" * 10)

        try:
            nombre = input("Nombre (o 'fin' para terminar): ").strip()

            if nombre.lower() == "fin":
                break

            edad = int(input("Edad (años): "))
            estatura = float(input("Estatura (metros, ej: 1.75): "))
            peso = float(input("Peso (kg): "))

            persona = Persona(nombre, edad, estatura, peso)
            personas.append(persona)

            print(f"\n {nombre} registrado exitosamente!")

        except ValueError as e:
            print(f"\nError: {e}")
            print("Por favor, intenta de nuevo.")

    return personas


def main():
    """Función principal."""
    print("\n" + "🌊" * 10)
    print("  PARQUE ACUÁTICO - SISTEMA DE ACCESO")
    print("🌊" * 10 + "\n")

    # Crear atracción
    tobogan = Acuatico(
        nombre="Tobogán del Dragón",
        capacidad=3,
        profundidad=1.70,
        propulsion="Gravedad",
        estatura_minima=1.20,
        edad_minima=8,
    )

    print(f" Atracción: {tobogan.nombre}")
    print(f" Estatura mínima: {tobogan.estatura_minima} m")
    print(f" Edad mínima: {tobogan.edad_minima} años")

    time.sleep(1)

    # Crear personas
    juan = Persona("Juan", 25, 1.75, 70)
    maria = Persona("María", 10, 1.35, 35)
    pedro = Persona("Pedro", 6, 1.10, 25)
