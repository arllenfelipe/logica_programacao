import random
num_secreto = random.randint (1, 100)

palpite = 0 
while palpite != num_secreto:
    palpite = int(input('faça um palpite entre 1 e 100: '))
    
    if palpite > num_secreto:
        print('tente um numero menor.')
    elif palpite < num_secreto:
        print('tente um numero maior.')

print(f'parabens !! você acertou o número secreto {num_secreto}.')