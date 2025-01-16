#função crie duas funcoes a primera deve receber um numero e retornar o dobro dele. depois chame a primeira função dentro da segunda função para retornar o quadrado do dobro do numero.

def dobro(n):
    return n * 2    

def quadrado(n):
    return dobro(n) ** 2 

#Chamando a função dobro dentro da função quadrado.

user_numeber = int(input("Digite um número inteiro: "))
print(f'O quadrado do dobro de {user_numeber} é {quadrado(user_numeber)}')

