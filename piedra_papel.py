# Elección aleatoria Maq
import random

# function randint(min-max)
rand_int = random.randint(1,3)
if rand_int == 1:
    choice_maq = 'Piedra'
elif rand_int == 2:
    choice_maq = 'Papel'    
else:
    choice_maq = 'Tijeras'

# Elección de usuario
choice_text = '''
Escribe una de las opciones:
    Piedra
    Papel
    Tijeras
'''
choice_user = input(choice_text)

# Impresión de Opciones
print('Usuario eligio ->', choice_user)
print('Maquina eligio ->', choice_maq)

# Ganador!
if choice_maq == choice_user:
    print("Es un empate");
else:
    if choice_maq == 'Piedra' and choice_user == 'Papel':
        print("Gana Usuario!")
    elif choice_maq == 'Piedra' and choice_user == 'Tijeras':
        print("Gana Maquina!")
    elif choice_maq == 'Papel' and choice_user == 'Tijeras':
        print("Gana Usuario!")
    elif choice_maq == 'Papel' and choice_user == 'Piedra':
        print("Gana Maquina!")
    elif choice_maq == 'Tijeras' and choice_user == 'Piedra':
        print("Gana Usuario!")
    else:
        print("Gana Maquina!")
        

