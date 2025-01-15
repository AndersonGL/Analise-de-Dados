capitais ={
    
    
    'Brasil': 'Brasília', 
    'Argentina': 'Buenos Aires', 
    'Chile': 'Santiago', 
    'Colômbia': 'Bogotá', 
    'Uruguai': 'Montevidéu'
    
}

pais_usuario= input('Digite o nome de um país: ')


if pais_usuario in capitais:
    
    print(f'A capital do país {pais_usuario} é {capitais[pais_usuario]}.')
    
else:
    
    print('Desculpe, não temos informaçoes sobre esse país ou capital.')