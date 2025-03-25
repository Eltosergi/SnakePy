# Snake Game en C#

Este proyecto es una implementación del clásico juego de la serpiente, convertido de Python a C#. Utiliza hilos para la captura de entrada del teclado y simula una interfaz de consola.

## Características
- Representación de la serpiente en una matriz de caracteres.
- Captura de teclas para controlar la dirección.
- Generación aleatoria de comida.
- Finalización del juego cuando la serpiente choca consigo misma.

## Requisitos
- .NET 6.0 o superior.
- Sistema operativo Windows (para limpiar la consola con `Console.Clear()`).

## Instalación y ejecución
1. Clonar el repositorio:
   ```sh
   git clone https://github.com/Eltosergi/SnakePy.git
   ```
2. Navegar al directorio del proyecto:
   ```sh
   cd SnakeGame
   ```
3. Compilar y ejecutar:
   ```sh
   dotnet run
   ```

## Controles
- Flecha arriba (↑): Mover arriba.
- Flecha abajo (↓): Mover abajo.
- Flecha izquierda (←): Mover izquierda.
- Flecha derecha (→): Mover derecha.
- ESC: Salir del juego.

## Conversión de Python a C#
El código original en Python utilizaba la biblioteca `pynput` para capturar la entrada del teclado y `numpy` para manejar matrices. En la versión en C#, se han implementado equivalentes usando `Console.ReadKey` en un hilo separado para la captura de entrada y arreglos bidimensionales (`char[,]`) para la representación de la tabla.

## Licencia
Este proyecto se distribuye bajo la licencia MIT.


