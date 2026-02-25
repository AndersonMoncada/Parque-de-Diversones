# 🎡 Parque de Diversiones

Sistema de gestión de acceso para un parque de diversiones desarrollado en Python. Permite registrar grupos de visitantes y validar su ingreso a las distintas atracciones según edad, estatura y peso.

---

## Estructura del proyecto

```
Parque-de-Diversones/
├── main.py                  # Punto de entrada del programa
├── clases/
│   ├── Usuario.py           # Clase Persona
│   ├── acuaticos.py         # Atracciones acuáticas
│   ├── Electronicos.py      # Juegos electrónicos
│   ├── mecanicos.py         # Juegos mecánicos
│   ├── fisicos.py           # Juegos físicos
│   └── Atracciones.py       # Instancias de todas las atracciones
└── .gitignore
```

---

## Sedes y atracciones

### Acuáticos
- Tobogán del Dragón
- Río Peligro *(Río Lento)*
- Botes Locos *(Botes Chocones)*

### Electrónicos
- Simulación Apocalipsis Zombie *(Simulador VR)*
- Doom Arcade *(Shooter FPS)*
- Tetris Versus *(Arcade)*

### Mecánicos
- Montaña Rusa Extrema
- Rueda de la Fortuna
- Barco Pirata
- Carros Chocones

### Físicos
- Tirolesa Extrema
- Muro de Escalada
- Salto Bungee
- Tiro con Arco

---

## Cómo ejecutarlo

```bash
python main.py
```

El programa pedirá registrar al grupo de visitantes y luego mostrará el menú principal.

---

## Flujo del programa

```
Registro de personas
        ↓
Menú principal
        ↓
Elegir sede → Mecánicos / Electrónicos / Acuáticos / Físicos
        ↓
Elegir juego
        ↓
Validación de acceso (edad, estatura, peso)
        ↓
Iniciar atracción
```

---

## Requisitos

- Python 3.10 o superior
- No requiere librerías externas

---

## Ramas del repositorio

| Rama | Descripción |
|------|-------------|
| `dev` | Rama de desarrollo principal |
| `qa` | Pruebas y revisión |
| `prod` | Versión estable para producción |

---

## Autores
Daniela Restrepo Cano , Anderson Moncada Marin

Proyecto desarrollado como práctica de Programación Orientada a Objetos con herencia, encapsulamiento y polimorfismo en Python.