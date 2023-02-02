import random


def play():
    """
    Función que dará inicio al juego y dará el ganador
    :return: Texto de resultado del juego
    """
    tupla = ('piedra', 'papel', 'tijera')
    usuario = int(input('Seleccione un numero como opcion: 1= Piedra, 2= Papel, 3= Tijera.\n'))
    if (usuario == 1) or (usuario == 2) or (usuario == 3):
        computadora = random.choice([1, 2, 3])

        if usuario == computadora:
            return print('¡Empate!\n')

        elif gano_el_jugador(usuario, computadora) is True:
            return print('¡Ganaste usando', tupla[usuario-1], 'contra', tupla[computadora-1], '!\n')

        else:
            return print('¡Perdiste!. Vos usaste', tupla[usuario-1], 'y el rival uso', tupla[computadora-1], '\n')
    else:
        print('No selecciono una opcion valida. Intente de nuevo.\n')


def gano_el_jugador(jugador, oponente):
    """
    Función que comprueba si el jugador es el ganador del juego
    :param jugador: el valor elegido por el jugador
    :param oponente: el valor elegido por la maquina
    :return: True si ganó el jugador, False si perdió el jugador
    """
    if (jugador == 1 and oponente == 3) or (jugador == 2 and oponente == 1) or (jugador == 3 and oponente == 2):

        return True
    else:
        return False


def menu():
    """
    La función inicio del programa, ejecuta un menú de opciones.
    """
    opcion = -1
    while opcion != 0:
        print('Bienvenido a el juego Piedra Papel o Tijeras.\n Quiere jugar una partida o dejar de jugar?\n')
        opcion = input('Seleccione una opcion: \n 1 - Jugar partida. \n 0 - Dejar de jugar.\n')
        if opcion == str(1):
            play()
        elif opcion == str(0):
            print('Gracias por jugar.')
            break
        else:
            print('Porfavor seleccione una opcion correcta.')


menu()
