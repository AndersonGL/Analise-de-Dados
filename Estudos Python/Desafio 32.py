
# Crie uma função lambda  que eleve um número ao quadrado em seguida use a funçaõ para calcular o quadrado de todos os números dentro de um for loop´.

numeros = [1 ,2 ,3 ,4 ,5 ,6]

quadrado = lambda num: num ** 2

resultados = []

for i in numeros:
 resultados.append(quadrado(i))
 
print(f'O quadrado dos números é: {numeros} são {resultados}')
 
 


