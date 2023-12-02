import random
opcao_computador = random.randint (0, 2)
match opcao_computador:
    case 0:
        print('pedra')
    case 1:
        print('papel')
    case 2:
        print('tesoura')
opcao_jogador = input('escolha uma opção: pedra,papel ou tesoura: ')
opcao = 2
if opcao_jogador == 0:
    print('jogador venceu')
elif opcao_computador == 1:
    print('computador venceu')
elif opcao_jogador == 2:
    print('jogador venceu')
else: 
    print('computador venceu.')

if opcao_jogador == opcao_computador:
    print('empate')

    


    
