import time
from .Usuario import Persona

class Mecanicas:
    """
    Clase base para todas las atracciones mecánicas del parque.
    
    Define validaciones comunes de acceso y presentación de información
    para montañas rusas, ruedas de la fortuna, barcos piratas y carros chocones.
    """

    def __init__(
        self,
        nombre: str,
        estatura_minima: float,
        edad_minima: int,
        reglas: str,
        precauciones: str,
    ) -> None:
        """
        Inicializa una atracción mecánica con requisitos de seguridad básicos.
        
        Args:
            nombre (str): Nombre de la atracción mecánica.
            estatura_minima (float): Estatura mínima requerida en metros.
            edad_minima (int): Edad mínima en años.
            reglas (str): Reglas de seguridad obligatorias.
            precauciones (str): Advertencias médicas/contra indicaciones.
        """
        self.nombre = nombre
        self.estatura_minima = estatura_minima
        self.edad_minima = edad_minima
        self.reglas = reglas
        self.precauciones = precauciones

    def validar_condiciones_entrada(self, persona: Persona) -> bool:
        """
        Valida si una persona cumple requisitos básicos de edad y estatura.
        
        Args:
            persona (Persona): Instancia de Persona a validar.
            
        Returns:
            bool: True si cumple ambos requisitos, False otherwise.
        """
        if (
            persona.edad >= self.edad_minima
            and persona.estatura >= self.estatura_minima
        ):
            return True
        else:
            return False

    def verificar_entrada(self, compro_entrada: bool) -> bool:
        """
        Verifica si el usuario compró entrada válida.
        
        Args:
            compro_entrada (bool): Estado de compra de entrada.
            
        Returns:
            bool: True si tiene entrada válida.
        """
        return compro_entrada

    def mostrar_informacion(self) -> None:
        """
        Muestra información básica de la atracción mecánica.
        
        Incluye nombre, estatura mínima, reglas y precauciones de seguridad.
        """
        print(f"\nAtracción: {self.nombre}")
        print(f"Estatura mínima: {self.estatura_minima} m")
        print(f"Reglas: {self.reglas}")
        print(f"Precauciones: {self.precauciones}")


class MontanaRusa(Mecanicas):
    """
    Montaña rusa con loopings e inversiones.
    
    Atracción de alta adrenalina con velocidad máxima y giros completos.
    """

    def __init__(
        self,
        nombre: str,
        estatura_minima: float,
        edad_minima: int,
        reglas: str,
        precauciones: str,
        velocidad_maxima: float,
        inversiones: int,
    ):
        """
        Inicializa montaña rusa con especificaciones técnicas.
        
        Args:
            nombre (str): Nombre de la montaña rusa.
            estatura_minima (float): Altura de seguridad obligatoria.
            edad_minima (int): Edad mínima por velocidad.
            reglas (str): Instrucciones de seguridad.
            precauciones (str): Advertencias médicas.
            velocidad_maxima (float): Velocidad pico en km/h.
            inversiones (int): Número de loopings/inversiones.
        """
        super().__init__(
            nombre,
            estatura_minima,
            edad_minima,
            reglas,
            precauciones,
        )
        self.velocidad_maxima = velocidad_maxima
        self.inversiones = inversiones

    def mostrar_informacion(self) -> None:
        """
        Muestra información específica de montaña rusa.
        
        Incluye velocidad máxima y número de inversiones además de datos base.
        """
        super().mostrar_informacion()
        print("Velocidad maxima: ", self.velocidad_maxima, "km/h")
        print("Numero de inversiones: ", self.inversiones)

    def entrar_montana(self, grupo: list[Persona]) -> None:
        """
        Procesa entrada de grupo a la montaña rusa.
        
        Valida cada persona y solo inicia si hay al menos una apta.
        
        Args:
            grupo (list[Persona]): Lista de personas del grupo.
        """
        personas_abordo = []
        for persona in grupo:
            if self.validar_condiciones_entrada(persona):
                print("Puedes entrar ", persona.nombre, "😁")
                personas_abordo.append(persona)
            else:
                print("Lo siento, no puedes entrar ", persona.nombre, " :c")
            print("=" * 40)
        if personas_abordo:
            self.iniciar_recorrido(personas_abordo)
        else:
            print("No hay personas que puedan subir")

    def iniciar_recorrido(self, lista_personas: list[Persona]) -> None:
        """
        Simula recorrido de montaña rusa con animación.
        
        Muestra lista de pasajeros y animación de 4 segundos.
        
        Args:
            lista_personas (list[Persona]): Pasajeros aprobados a bordo.
        """
        print("Personas abordo: ")
        for persona in lista_personas:
            print(persona.nombre)
            time.sleep(1)
        print("Iniciando recorrido 🎢")
        for i in range(0, 4):
            print("🎢")
            time.sleep(1)
        print("Recorrido finalizado")


class RuedaDeLaFortuna(Mecanicas):
    """
    Rueda de la fortuna panorámica.
    
    Atracción relajada con vista 360° desde gran altura.
    """

    def __init__(
        self,
        nombre: str,
        estatura_minima: float,
        edad_minima: int,
        reglas: str,
        precauciones: str,
        altura_maxima: float,
    ):
        """
        Inicializa rueda de la fortuna.
        
        Args:
            nombre (str): Nombre de la rueda.
            estatura_minima (float): Estatura mínima.
            edad_minima (int): Edad mínima.
            reglas (str): Reglas de comportamiento.
            precauciones (str): Advertencias por altura.
            altura_maxima (float): Altura máxima en metros.
        """
        super().__init__(
            nombre,
            estatura_minima,
            edad_minima,
            reglas,
            precauciones,
        )
        self.altura_maxima = altura_maxima

    def mostrar_informacion(self) -> None:
        """Muestra información específica incluyendo altura máxima."""
        super().mostrar_informacion()
        print("Altura maxima:", self.altura_maxima)

    def entrar_rueda(self, grupo: list[Persona]) -> None:
        """
        Procesa entrada de grupo a la rueda de la fortuna.
        
        Args:
            grupo (list[Persona]): Lista de personas.
        """
        personas_abordo = []
        for persona in grupo:
            if self.validar_condiciones_entrada(persona):
                print("Puedes entrar", persona.nombre, "😁")
                personas_abordo.append(persona)
            else:
                print("Lo siento, no puedes entrar", persona.nombre, ":c")
            print("=" * 40)
        if personas_abordo:
            self.iniciar_vuelta()
        else:
            print("No hay personas que puedan subir")

    def iniciar_vuelta(self) -> None:
        """
        Simula una vuelta completa de la rueda con animación diurna.
        
        Animación de 4 segundos con rueda y sol.
        """
        print("Iniciando vuelta 🎡")
        for i in range(0, 4):
            print("🎡")
            time.sleep(1)
            print("⛅")
        print("Vuelta finalizada")


class BarcoPirata(Mecanicas):
    """
    Barco pirata oscilante.
    
    Atracción grupal con balanceo intenso tipo péndulo.
    """

    def __init__(
        self,
        nombre: str,
        estatura_minima: float,
        edad_minima: int,
        reglas: str,
        precauciones: str,
        capacidad: int,
    ):
        """
        Inicializa barco pirata.
        
        Args:
            nombre (str): Nombre del barco.
            estatura_minima (float): Estatura mínima.
            edad_minima (int): Edad mínima.
            reglas (str): Instrucciones de sujeción.
            precauciones (str): Advertencias por mareo.
            capacidad (int): Capacidad máxima de pasajeros.
        """
        super().__init__(
            nombre,
            estatura_minima,
            edad_minima,
            reglas,
            precauciones,
        )
        self.capacidad = capacidad

    def mostrar_informacion(self) -> None:
        """Muestra información específica incluyendo capacidad."""
        super().mostrar_informacion()
        print("Capacidad personas:", self.capacidad)

    def entrar_barco(self, grupo: list[Persona]) -> None:
        """
        Procesa entrada de grupo al barco pirata.
        
        Args:
            grupo (list[Persona]): Lista de personas.
        """
        personas_abordo = []
        for persona in grupo:
            if self.validar_condiciones_entrada(persona):
                print("Puedes entrar", persona.nombre, "😁")
                personas_abordo.append(persona)
            else:
                print("Lo siento, no puedes entrar", persona.nombre, ":c")
            print("=" * 40)
        if personas_abordo:
            self.iniciar_barco()
        else:
            print("No hay personas que puedan subir")

    def iniciar_barco(self) -> None:
        """
        Simula oscilación del barco pirata.
        
        Animación de 5 segundos con barco.
        """
        print("Iniciando juego ⚓")
        for i in range(0, 5):
            print("🚢")
            time.sleep(1)
        print("Juego finalizado")


class CarrosChocones(Mecanicas):
    """
    Carros chocones/bumpers.
    
    Atracción de choques controlados con múltiples vehículos.
    """

    def __init__(
        self,
        nombre: str,
        estatura_minima: float,
        edad_minima: int,
        reglas: str,
        precauciones: str,
        numero_carros: int,
        duracion: float,
    ):
        """
        Inicializa carros chocones.
        
        Args:
            nombre (str): Nombre de la pista.
            estatura_minima (float): Estatura mínima.
            edad_minima (int): Edad mínima.
            reglas (str): Reglas de choque.
            precauciones (str): Instrucciones de seguridad.
            numero_carros (int): Cantidad de carros disponibles.
            duracion (float): Duración de ronda en minutos.
        """
        super().__init__(
            nombre,
            estatura_minima,
            edad_minima,
            reglas,
            precauciones,
        )
        self.numero_carros = numero_carros
        self.duracion = duracion

    def mostrar_informacion(self) -> None:
        """Muestra información específica de carros chocones."""
        super().mostrar_informacion()
        print("Numero de carritos: ", self.numero_carros)
        print("Duracion ronda: ", self.duracion)

    def entrar_carros(self, grupo: list[Persona]) -> None:
        """
        Procesa entrada requiriendo mínimo 2 personas.
        
        Solo inicia si hay al menos 2 personas aptas.
        
        Args:
            grupo (list[Persona]): Lista de personas.
        """
        personas_abordo = []
        for persona in grupo:
            if self.validar_condiciones_entrada(persona):
                print("Puedes entrar", persona.nombre, "😁")
                personas_abordo.append(persona)
            else:
                print("Lo siento, no puedes entrar", persona.nombre, ":c")
            print("=" * 40)
        if len(personas_abordo) >= 2:
            self.iniciar_carros()
        else:
            print("No hay personas suficientes para iniciar el juego")

    def iniciar_carros(self) -> None:
        """
        Simula sesión de choques con carros.
        
        Animación de 5 segundos con carros y explosiones.
        """
        print("Iniciando juego 🏎")
        for i in range(0, 5):
            print("🏎")
            time.sleep(1)
            print("💥")
        print("Juego finalizado")
