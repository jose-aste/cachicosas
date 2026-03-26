#miau 
from random import randint
print('\nPara jugar, elegir un elemento: piedra, papel, tijera, lagartija, o spock\n')

compu_l = ['piedra','papel', 'tijera','lagartija', 'spock']

jugador = input('Anotar elemento aquí: ').lower()
while jugador not in compu_l:
    jugador = input('Eso no es un elemento. Anotar elemento aquí: ').lower()

rando = randint(0, 4)
compu = compu_l[rando]
