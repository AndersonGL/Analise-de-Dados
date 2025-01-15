
#Desafio 24: Criei um programa que leia um número e mostre a sua raiz quadrada. ultilizei o método de potenciação para resolver o desafio. junto com o método de input para receber o número do usuário.


# criando o desafio com funções:

def quadrado(numero):
    return numero ** 2
num = int(input('Digite um número: '))
print(f'O quadrado de {num} é {quadrado(num)}')

#def raiz_quadrada(numero):
 #return numero ** 0.5  # 0.5 é a raiz quadrada de um número
#num = int(input('Digite um número: '))
#print(f'A raiz quadrada de {num} é {raiz_quadrada(num)}')
