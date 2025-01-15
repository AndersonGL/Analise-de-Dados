# Crie uma função que calcula a potencia de um número. A funçaõ recebe dois parâmetros, a base e o expoente e retorna o resultado. Se o expoente não for informado, o valor será 2.

def potencia(base, expoente=2):
    return base ** expoente
num = int(input('Digite um número: '))
num2 = input('Digite o expoente: ')    

if num2 == '':
    print(f'O resultado de {num} elevado a 2 é: {potencia(num)}')   
    
else:  # int foi digitado para converter o input em número inteiro.
    print(f'O resultado de {num} elevado a {num2} é: {potencia(num, int(num2))}') 
   
    



