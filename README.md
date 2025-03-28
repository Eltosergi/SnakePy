# Snake Game en Python

Este es un juego de Snake simple desarrollado en Python que se ejecuta en la terminal. El juego utiliza `numpy` para manejar la matriz del tablero y `pynput` para la detección de teclas.

## Requisitos

Asegúrate de tener instaladas las siguientes dependencias antes de ejecutar el juego:

```bash
pip install numpy pynput
```

## Cómo jugar

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Eltosergi/SnakePy
   cd SnakePy
   ```
2. Ejecuta el script en tu terminal con:
   ```bash
   snake.py
   ```
3. Controla la serpiente con las teclas de dirección:
   - ⬆️ Arriba
   - ⬇️ Abajo
   - ⬅️ Izquierda
   - ➡️ Derecha
   - `ESC` para salir del juego

## Funcionamiento

- La serpiente se mueve en una matriz de `20x20` por defecto.
- Come la comida (`☀`) para crecer y aumentar el puntaje.
- El juego termina si la serpiente choca consigo misma.
- La puntuación final se muestra al terminar el juego.

## Código principal

El juego consta de:
- `genMatrix(size)`: Crea la matriz del tablero.
- `printTable(Matrix)`: Muestra el tablero en la terminal.
- `keyBoardInput(list)`: Captura la entrada del teclado.
- `cleanTable(Matrix, size)`: Limpia el tablero en cada iteración.
- `addTable(Matrix, cords, body)`: Coloca la serpiente y la comida en el tablero.
- `endGame(points)`: Muestra la puntuación final.
- `game(size)`: Controla la lógica principal del juego.

## Mejoras posibles

- Implementar límites personalizables en el tamaño del tablero.
- Agregar niveles de dificultad con velocidades variables.
- Incluir una interfaz gráfica con `pygame`.

¡Diviértete jugando Snake en Python! 🐍



