
#Pedir ao usuário que digite 2 números

#int para base 10 no caso usaremos o float para armazenar tanto inteiro quanto flotoante

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite  o segundo número: '))

# resolver as tarefas


soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
exponenciacao = num1 ** num2

print(f'Soma: {soma}')
print(f'Subtração: {subtracao}')
print(f'Multiplicação: {multiplicacao}')
print(f'Divisão: {divisao}')
print(f'Exponenciação: {exponenciacao}')