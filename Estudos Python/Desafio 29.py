# Crie uma função lambda que aceite um número e retorne o cubo desse número.


cubo = lambda num: num ** 3

user_number = int(input("Digite um número inteiro: "))

print(f'O cubo do número {user_number} é {cubo(user_number)}')


