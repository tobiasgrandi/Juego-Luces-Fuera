import logica

def main():

    contador_total = 0
    for nivel in range(0, 5):
        tablero = logica.iniciar_juego(nivel)
        contador_por_nivel = 0
        while True:
            logica.interfaz_juego(tablero)
            print(f"Te quedan {len(tablero)*3-contador_por_nivel} movimientos restantes")
            if contador_por_nivel < len(tablero)*3:
                if logica.nivel_ganado(tablero, nivel):
                    print(f"Ganaste el nivel, pasas al siguiente. Niveles restantes: {4-nivel}")
                    break
                posicion = logica.pedir_direccion()
                tablero = logica.prender_apagar(tablero, posicion)
                contador_por_nivel += 1
                contador_total += 1
            else:
                print(f"Perdiste.\nLlegaste hasta el nivel: {nivel+1}\nMovimientos totales realizados: {contador_total}")
                return
        if logica.juego_ganado(tablero, nivel):
            print(f"Ganaste el juego.\nMovimientos totales realizados: {contador_total}")
            break 
        
main()