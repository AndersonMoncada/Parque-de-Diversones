"""
Módulo de instanciación de todas las atracciones del parque de diversiones.

Contiene las listas preconfiguradas de todos los juegos organizados por categoría:
- juegos_acuaticos: Atracciones de agua
- juegos_electronicos: Juegos de realidad virtual y arcade
- juegos_mecanicos: Atracciones mecánicas clásicas
- juegos_fisicos: Actividades deportivas y de aventura

Cada juego está configurado con parámetros realistas basados en estándares de parques
de diversiones. Los valores reflejan requisitos típicos de seguridad, capacidad
y restricciones de edad/estatura.
"""

from clases.acuaticos import Acuatico, RioLento, BotesChocones
from clases.Electronicos import SimuladorVR, ShooterFPS, JuegoArcade
from clases.mecanicos import (
    MontanaRusa,
    RuedaDeLaFortuna,
    BarcoPirata,
    CarrosChocones,
)
from clases.fisicos import Tirolesa, MuroEscalada, SaltoBungee, TiroConArco


"""
Lista de 3 atracciones acuáticas con diferentes características:
- Tobogán del Dragón: Alta velocidad por gravedad
- Río Peligro: Río lento familiar con corriente natural  
- Botes Locos: Botes chocones motorizados
"""
juegos_acuaticos: list[Acuatico] = [
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


"""
Lista de 3 juegos electrónicos inmersivos:
- Simulación VR: Experiencia grupal de terror
- Shooter FPS: Experiencia individual intensa
- Tetris Versus: Competencia arcade relajada
"""
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


"""
Lista de 4 atracciones mecánicas clásicas:
- Montaña Rusa: Adrenalina máxima con loopings
- Rueda Fortuna: Vista panorámica relajada
- Barco Pirata: Balanceo intenso grupal
- Carros Chocones: Choques controlados
"""
juegos_mecanicos = [
    MontanaRusa(
        nombre="Montaña Rusa Extrema",
        estatura_minima=1.40,  
        edad_minima=12,
        reglas="Permanecer sentado",
        precauciones="No recomendado para cardiacos",
        velocidad_maxima=120.0, 
        inversiones=3,      
    ),
    RuedaDeLaFortuna(
        nombre="Rueda de la Fortuna",
        estatura_minima=1.0,   
        edad_minima=5,
        reglas="No balancear la cabina",
        precauciones="No recomendado para vértigo",
        altura_maxima=40.0,  
    ),
    BarcoPirata(
        nombre="Barco Pirata",
        estatura_minima=1.20,
        edad_minima=8,
        reglas="Sujetarse en todo momento",
        precauciones="No recomendado para mareos",
        capacidad=20,        
    ),
    CarrosChocones(
        nombre="Carros Chocones",
        estatura_minima=1.10,
        edad_minima=7,
        reglas="No chocar de frente",
        precauciones="Usar cinturón",
        numero_carros=10,
        duracion=5.0,         
    ),
]


"""
Lista de 4 actividades físicas extremas:
- Tirolesa: Descenso aéreo con límite de peso
- Muro Escalada: Escalada deportiva
- Salto Bungee: Salto elástico desde altura
- Tiro Arco: Precisión deportiva
"""
juegos_fisicos = [
    Tirolesa(
        nombre_juego="Tirolesa Extrema",
        altura_juego=15.0,     
        edad_minima=10,
        estatura_minima=1.20,
        velocidad=50.0,        
        peso_maximo=100.0,    
    ),
    MuroEscalada(
        nombre_juego="Muro de Escalada",
        altura_juego=8.0,      
        edad_minima=8,
        estatura_minima=1.10,
        dificultad="Media",
    ),
    SaltoBungee(
        nombre_juego="Salto Bungee",
        altura_juego=30.0,     
        edad_minima=14,        
        estatura_minima=1.50,
    ),
    TiroConArco(
        nombre_juego="Tiro con Arco",
        edad_minima=8,
        estatura_minima=1.10,  
    ),
]
