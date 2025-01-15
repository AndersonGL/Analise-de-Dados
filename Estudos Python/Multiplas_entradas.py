#Multiplas entradas de input na mesma linha, Declarando variáveis com split() e input() e depois imprimindo na tela 
#usando o método upper() para deixar o texto em maiúsculo.


dados = input('Digite seu nome e idade: ').split() #Anderson 38 #split() separa os dados por espaço

nome =(dados[0]) 
idade = (dados[1])  

#usando o método upper() para deixar o texto em maiúsculo.

print(f'Seu nome é {nome.upper()} e você tem {idade} anos.') 


#upper() deixa o texto em maiusculo
#Lower() deixa o texto em minusculo 