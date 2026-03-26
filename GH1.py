#miau 
from random import randint
print('\nPara jugar, elegir un elemento: piedra, papel, tijera, lagartija, o spock\n')

compu_l = ['piedra','papel', 'tijera','lagartija', 'spock']

jugador = input('Anotar elemento aquí: ').lower()
while jugador not in compu_l:
    jugador = input('Eso no es un elemento. Anotar elemento aquí: ').lower()

rando = randint(0, 4)
compu = compu_l[rando]


print('\nEl computador tiro', compu,'\n')

if jugador == compu:
    print("¡Empataron!")
elif jugador == 'piedra':
    if compu == 'papel' or compu == 'spock':
        print('¡Perdiste!', compu, 'vence a', jugador)
    else:
        print('¡Ganaste!', jugador, 'vence a', compu)
elif jugador == 'papel':
    if compu == 'tijera' or compu == 'lagartija':
        print('¡Perdiste!', compu, 'vence a', jugador)
    else:
        print('¡Ganaste!', jugador, 'vence a', compu)
elif jugador == 'tijera':
    if compu == 'spock' or compu == 'piedra':
        print('¡Perdiste!', compu, 'vence a', jugador)
    else:
        print('¡Ganaste!', jugador, 'vence a', compu)
elif jugador == 'lagartija':
    if compu == 'tijera' or compu == 'piedra':
        print('¡Perdiste!', compu, 'vence a', jugador)
    else:
        print('¡Ganaste!', jugador, 'vence a', compu)
else: #spocvk
    if compu == 'papel' or compu == 'lagartija':
        print('¡Perdiste!', compu, 'vence a', jugador)
    else:
        print('¡Ganaste!', jugador, 'vence a', compu)
