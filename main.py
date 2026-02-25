
import time
from clases.Usuario import Persona
from clases.acuaticos import Acuatico
from clases.Electronicos import JuegoElectronico
from clases.mecanicos import Mecanicas
from clases.fisicos import JuegosFisicos
from clases.entradas import Entrada
from clases.Atracciones import (
    juegos_acuaticos,
    juegos_electronicos,
    juegos_mecanicos,
    juegos_fisicos,
)


def registrar_personas() -> list[Persona]:
    """
    Registra un grupo de personas visitantes del parque de diversiones.
    
    Solicita al usuario la cantidad de personas a registrar y luego recopila
    información básica de cada una (nombre, edad, estatura y peso).
    
    Returns:
        list[Persona]: Lista de objetos Persona registrados.
    
    Example:
        >>> personas = registrar_personas()
        Hola, tú eres el titular del grupo. ¿Cuántas personas vas a registrar? 2
        Persona 1:
          Nombre: Juan
          Edad: 25
          Estatura (metros): 1.75
          Peso (kg): 70
    """
    
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


def menu_acuaticos(grupo: list[Persona], juegos: list[Acuatico]) -> None:
    """
    Muestra y maneja el menú de juegos acuáticos.
    
    Permite al usuario seleccionar un juego acuático para que el grupo
    participe. Incluye validación de entrada y opción de regreso.
    
    Args:
        grupo (list[Persona]): Lista de personas del grupo.
        juegos (list[Acuatico]): Lista de juegos acuáticos disponibles.
    """
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


def menu_electronicos(grupo: list[Persona], juegos: list[JuegoElectronico]) -> None:
    """
    Muestra y maneja el menú de juegos electrónicos.
    
    Permite al usuario seleccionar un juego electrónico para que el grupo
    participe. Incluye validación de entrada y opción de regreso.
    
    Args:
        grupo (list[Persona]): Lista de personas del grupo.
        juegos (list[JuegoElectronico]): Lista de juegos electrónicos disponibles.
    """
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


def menu_mecanicos(grupo: list[Persona], juegos: list[Mecanicas]) -> None:
    """
    Muestra y maneja el menú de juegos mecánicos.
    
    Permite al usuario seleccionar un juego mecánico específico para el grupo.
    Utiliza métodos dinámicos según el tipo de juego seleccionado.
    
    Args:
        grupo (list[Persona]): Lista de personas del grupo.
        juegos (list[Mecanicas]): Lista de juegos mecánicos disponibles.
    """
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


def menu_fisicos(grupo: list[Persona], juegos: list[JuegosFisicos]) -> None:
    """
    Muestra y maneja el menú de juegos físicos.
    
    Permite al usuario seleccionar un juego físico específico para el grupo.
    Utiliza métodos dinámicos según el tipo de juego seleccionado.
    
    Args:
        grupo (list[Persona]): Lista de personas del grupo.
        juegos (list[JuegosFisicos]): Lista de juegos físicos disponibles.
    """
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
    grupo: list[Persona],
    juegos_acuaticos: list[Acuatico],
    juegos_electronicos: list[JuegoElectronico],
    juegos_mecanicos: list[Mecanicas],
    juegos_fisicos: list[JuegosFisicos]
) -> None:
    """
    Muestra el menú principal de sedes del parque de diversiones.
    
    Permite al usuario navegar entre las diferentes sedes (mecánicos,
    electrónicos, acuáticos, físicos) y regresar al menú principal.
    
    Args:
        grupo (list[Persona]): Lista de personas del grupo.
        juegos_acuaticos (list[Acuatico]): Juegos acuáticos disponibles.
        juegos_electronicos (list[JuegoElectronico]): Juegos electrónicos disponibles.
        juegos_mecanicos (list[Mecanicas]): Juegos mecánicos disponibles.
        juegos_fisicos (list[JuegosFisicos]): Juegos físicos disponibles.
    """
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
    grupo: list[Persona],
    juegos_acuaticos: list[Acuatico],
    juegos_electronicos: list[JuegoElectronico],
    juegos_mecanicos: list[Mecanicas],
    juegos_fisicos: list[JuegosFisicos]
) -> None:
    """
    Muestra el menú principal del sistema del parque de diversiones.
    
    Ofrece opciones para entrar a las sedes o salir del parque.
    
    Args:
        grupo (list[Persona]): Lista de personas del grupo.
        juegos_acuaticos (list[Acuatico]): Juegos acuáticos disponibles.
        juegos_electronicos (list[JuegoElectronico]): Juegos electrónicos disponibles.
        juegos_mecanicos (list[Mecanicas]): Juegos mecánicos disponibles.
        juegos_fisicos (list[JuegosFisicos]): Juegos físicos disponibles.
    """
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
            print("Hasta luego, esperamos que se haya divertido 🎆🎇🎆!!")
        else:
            print("Teclea un número ya sea 1 o 2 para recibir atención ;)")


def main() -> None:
    """
    Función principal del programa del parque de diversiones.
    
    Registra el grupo de personas y ejecuta el menú principal del sistema.
    """
    grupo = registrar_personas()
    entrada = Entrada(costo=30000) 
    entrada.calcular_total(grupo)
    menu_principal(
        grupo, juegos_acuaticos, juegos_electronicos, juegos_mecanicos, juegos_fisicos
    )


if __name__ == "__main__":
    main()
