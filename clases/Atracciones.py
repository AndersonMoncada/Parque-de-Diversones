from clases.acuaticos import Acuatico, RioLento, BotesChocones
from clases.Electronicos import SimuladorVR, ShooterFPS, JuegoArcade


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
