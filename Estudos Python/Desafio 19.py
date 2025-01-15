# lopp de frutas aonde a fruta escolhida é a abacate caso o contraio o lopp continua rodando ate achar a fruta abacate.

while True:
    fruta = input("Digite o nome de uma fruta: ")
    if fruta.lower() == 'abacate':
        break
    
print("Você acertou a fruta abacate!")