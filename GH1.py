#miau 
from random import randint
print('\nPara jugar, elegir un elemento: piedra, papel, tijera, lagartija, o spock\n')

compu_l = ['papel','piedra', 'lagartija','spock','tijera']

papel = ["-", 1, 2, 1, 2]

piedra = [2, "-", 1, 2, 1]

lagartija = [1, 2, "-", 1, 2]

spock = [2, 1, 2, "-", 1]

tijera = [1, 2, 1, 2, "-"]

listas = [papel, piedra, lagartija, spock, tijera]

puntaje_jugador = 0
puntaje_computador = 0

def jugada(jugador, computador):
    if listas[jugador][computador] ==1:
        return "Ganaste!"
    elif listas[jugador][computador] == "-":
        return "Es un empate!"  
    else:
        return "Perdiste :(" 


#brqnch?

jugar = True
while jugar == True:
    jugador = input('Anotar elemento aquí: ').lower()
    while jugador not in compu_l:
        jugador = input('Eso no es un elemento. Anotar elemento aquí: ').lower()
    if jugador == "piedra":
        jugador = 1
    elif jugador == "papel":
        jugador = 0
    elif jugador == "tijera":
        jugador = 4
    elif jugador == "lagartija":
        jugador = 2
    elif jugador == "spock":
        jugador = 3

    rando = randint(0, 4)
    print('El computador tiro',compu_l[rando])
    jug = int(compu_l.index(jugador))

    print(jugada(jug,rando))
    print("Quieres volver a jugar?")
    print("1. Sí!!")
    print("2. No :(")
    seguir = input()
    if seguir == "2":
        jugar = False
