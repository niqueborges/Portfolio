'''Tarefa: Abaixo estão as etapas:

Construa um jogo de adivinhação de números, no qual o usuário seleciona um intervalo.
Digamos que o usuário tenha selecionado um intervalo, ou seja, de A a B , onde A e B pertencem a inteiro.
Algum inteiro aleatório será selecionado pelo sistema e o usuário deve adivinhar esse inteiro no número mínimo de adivinhações.'''

# Importando a biblioteca random
from ast import While
import random
# Importando a biblioteca match
import math

# Definindo a função de adivinhação

lower = int(input("Enter Lower bound:- ")) # Definindo o limite inferior

upper = int(input("Enter Upper bound:- ")) # Definindo o limite superior

x = random.randint(lower, upper) # Definindo o número aleatório

print("\n\tYou've only ", round(math.log(upper - lower + 1, 2)), " chances to guess the integer!\n") # Definindo o número de chances

count = 0 # Definindo o contador


While count < math.log(upper - lower + 1, 2): # Definindo o loop
    count += 1 # Definindo o contador
    guess = int(input("Guess a number:- ")) # Definindo o palpite
    if x == guess: # Definindo a condição
        print("Congratulations you did it in ", count, " try") # Definindo a mensagem de parabéns
        
        break # Definindo o break
    elif x > guess: # Definindo a condição
        print("You guessed too small!") # Definindo a mensagem de erro
    elif x < guess: # Definindo a condição
        print("You Guessed too high!") # Definindo a mensagem de erro
        
if count >= math.log(upper - lower + 1, 2): # Definindo a condição
    print("\nThe number is %d" % x) # Definindo a mensagem de erro
    print("\tBetter Luck Next time!") # Definindo a mensagem de erro
