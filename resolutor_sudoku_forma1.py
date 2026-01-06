# Función para imprimir el tablero de Sudoku
def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(str(num) if num != 0 else "." for num in fila))

# Verifica si un número puede colocarse en una celda específica
def es_valido(tablero, fila, columna, num):
    # Verificar fila
    if num in tablero[fila]:
        return False
    # Verificar columna
    if num in [tablero[i][columna] for i in range(9)]:
        return False
    # Verificar subcuadrícula 3x3
    inicio_fila, inicio_columna = 3 * (fila // 3), 3 * (columna // 3)
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_columna, inicio_columna + 3):
            if tablero[i][j] == num:
                return False
    return True

# Función principal para resolver el Sudoku
def resolver_sudoku(tablero):
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0: # Encontrar una celda vacía
                for num in range(1, 10): # Probar números del 1 al 9
                    if es_valido(tablero, fila, columna, num):
                        tablero[fila][columna] = num
                        if resolver_sudoku(tablero): # Llamada recursiva
                            return True
                        tablero[fila][columna] = 0 # Retroceder si no funciona
                return False # No se puede resolver
    return True # Resuelto

# Ejemplo de tablero de Sudoku (0 representa celdas vacías)
tablero = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

# Resolver y mostrar el resultado
if resolver_sudoku(tablero):
    print("Sudoku resuelto")
    imprimir_tablero(tablero)
else:
    print("No se pudo resolver el Sudoku")