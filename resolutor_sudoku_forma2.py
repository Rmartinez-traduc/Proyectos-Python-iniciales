import pygame
import time

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ancho, alto = 540, 540
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Resolutor de Sudoku")

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
gris = (200, 200, 200)
azul = (0, 0, 255)

# Fuente
fuente = pygame.font.SysFont(None, 40)

# Sudoku inicial (0 representa celdas vacías)
tablero = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Dibujar la cuadrícula
def dibujar_cuadricula():
    for i in range(10):
        grosor = 4 if i % 3 == 0 else 1
        pygame.draw.line(pantalla, negro, (i * 60, 0), (i * 60, alto), grosor)
        pygame.draw.line(pantalla, negro, (0, i * 60), (ancho, i * 60), grosor)

# Dibujar los números en el tablero
def numeros_dibujados():
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] != 0:
                texto = fuente.render(str(tablero[fila][columna]), True, negro)
                pantalla.blit(texto, (columna * 60 + 20, fila * 60 + 15))

# Verificar si un número es válido en una posición
def es_valido(numero, fila, columna):
    # Verificar fila
    if numero in tablero[fila]:
        return False
    # Verificar columna
    if numero in [tablero[i][columna] for i in range(9)]:
        return False
    # Verificar subcuadrícula 3x3
    start_fila, start_columna = 3 * (fila // 3), 3 * (columna // 3)
    for i in range(start_fila, start_fila + 3):
        for j in range(start_columna, start_columna + 3):
            if tablero[i][j] == numero:
                return False
    return True

# Resolver el Sudoku usando backtracking
def resolver_sudoku():
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0:
                for numero in range(1, 10):
                    if es_valido(numero, fila, columna):
                        tablero[fila][columna] = numero
                        dibujar_tablero()
                        pygame.display.update()
                        time.sleep(0.05)  # Pausa para visualizar el proceso
                        if resolver_sudoku():
                            return True
                        tablero[fila][columna] = 0
                        dibujar_tablero()
                        pygame.display.update()
                return False
    return True

# Dibujar el tablero completo
def dibujar_tablero():
    pantalla.fill(blanco)
    dibujar_cuadricula()
    numeros_dibujados()

# Bucle principal
def main():
    running = True
    solved = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not solved:
            # Mostrar el estado inicial y resolver una vez
            dibujar_tablero()
            pygame.display.update()
            resolver_sudoku()
            solved = True
            time.sleep(2)  # Pausa para mostrar el resultado final

        # Actualizar pantalla cada iteración
        dibujar_tablero()
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()