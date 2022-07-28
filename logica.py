from string import ascii_uppercase
DIMENSION = 5
ESTADO = ["o", "."]
TABLERO = []
NIVELES = [ [ ['o', 'o', '.', 'o', 'o'], ['o', '.', 'o', '.', 'o'], ['.', 'o', 'o', 'o', '.'], ['o', '.', 'o', '.', 'o'], ['o', 'o', '.', 'o', 'o'] ], 
            [ ['.', 'o', '.', 'o', '.'], ['o', 'o', '.', 'o', 'o'], ['.', 'o', '.', 'o', '.'], ['o', '.', 'o', '.', 'o'], ['o', '.', 'o', '.', 'o'] ],
            [ ['o', '.', '.', '.', 'o'], ['o', 'o', '.', 'o', 'o'], ['.', '.', 'o', '.', '.'], ['o', '.', 'o', '.', '.'], ['o', '.', 'o', 'o', '.'] ],
            [ ['o', 'o', '.', 'o', 'o'], ['.', '.', '.', '.', '.'], ['o', 'o', '.', 'o', 'o'], ['.', '.', '.', '.', 'o'], ['o', 'o', '.', '.', '.'] ],
            [ ['.', '.', '.', 'o', 'o'], ['.', '.', '.', 'o', 'o'], ['.', '.', '.', '.', '.'], ['o', 'o', '.', '.', '.'], ['o', 'o', '.', '.', '.'] ] ]


def iniciar_juego(nivel):
    """Inicia el juego en cada nivel correspondiente"""
    
    TABLERO = NIVELES[nivel] 
    return TABLERO


def interfaz_juego(tablero):
    """Crea la interfaz del juego"""
    
    tablero = copia_tablero(tablero)
    parte_superior = " "
    for i in range(DIMENSION):
        parte_superior += f"{ascii_uppercase[i]} "
        tablero[i] = " ".join(tablero[i])
    print(f"   {parte_superior}")
    for i in range(DIMENSION):
        print(f"{i + 1} | {tablero[i]}" )


def pedir_direccion():
    """Pide el movimiento al usuario"""

    while True:
        posicion = input("Ingrese una posición de encendido o apagado: ")
        if len(posicion) == 2 and posicion[0].isalpha() and posicion[1].isdigit() and posicion[0] in ascii_uppercase[:DIMENSION] and int(posicion[1]) in list(range(1,DIMENSION+1)):
            break
        else:
            print("Ingrese una posicion de la forma A1.")
    return posicion


def copia_tablero(tablero):
    """Crea una copia del tablero"""
    
    copia = []
    for i in range(DIMENSION):
        copia.append([])
        for j in range(DIMENSION):
            copia[i].append(tablero[i][j])
    return copia


def prender_apagar (tablero, posicion):
    """Prende o apaga, según corresponda, la posición seleccionada y sus adyacentes"""

    columna = ascii_uppercase.index(posicion[0])
    fila = int(posicion[1])-1
    tablero_2 = copia_tablero(tablero)

    tablero_2[fila][columna] = ESTADO[(ESTADO.index(tablero_2[fila][columna])+1)%2]
    if columna != 0:
        tablero_2[fila][columna-1] = ESTADO[(ESTADO.index(tablero_2[fila][columna-1])+1)%2]
    if columna != DIMENSION-1:
        tablero_2[fila][columna+1] = ESTADO[(ESTADO.index(tablero_2[fila][columna+1])+1)%2]
    if fila != 0:
        tablero_2[fila-1][columna] = ESTADO[(ESTADO.index(tablero_2[fila-1][columna])+1)%2]
    if fila != DIMENSION-1:
        tablero_2[fila+1][columna] = ESTADO[(ESTADO.index(tablero_2[fila+1][columna])+1)%2]

    return tablero_2


def nivel_ganado(tablero, nivel):
    """Comprueba si se ganó el nivel"""

    if nivel < 4:
        for i in range(DIMENSION):
            if "o" in tablero[i]:
                return False
        return True

    
def juego_ganado(tablero, nivel):
    """Comprueba si el juego está ganado"""

    if nivel == 4:
        for i in range(DIMENSION):
            if "o" in tablero[i]:
                return False
        return True