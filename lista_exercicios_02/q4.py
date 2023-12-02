distancia = int(input('qual a distância que você deseja percorrer?'))
if distancia <= 200 :
    print(f'o preço da passagem é: {distancia * 0.50}')
elif distancia > 200 :
    print(f'o preço da passagem é: {distancia * 0.45}')