
# Crie uma funçaõ lambda aonde aceite um número e retorne par e o outro que retorne impar.


#def par_ou_impar(num):

 #if num % 2 == 0:
    
  #  return 'Par'

 #else:
    
  # return 'Impar' 
  
par_ou_impar = lambda num: 'Par' if num % 2 == 0 else 'Impar'
  
    
user_number = int(input('Digite um número: '))
print(f'O número {user_number} é {par_ou_impar(user_number)}')

