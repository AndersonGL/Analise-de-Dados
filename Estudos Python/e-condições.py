# Conceito: Condições em Python


#idade = 16

#if idade >= 18:
    #print('Maior de idade')
    
#else:
    #print('Menor de idade')
  
  
  
# Refatorado para uma função  

    
def new_func():
    idade = (int(input('Digite sua idade: ')))

    if idade < 18:
        print('Menor de idade') 
        
    elif idade < 60:
        print('Adulto')
    
    else:  
        print('Idoso')

new_func()