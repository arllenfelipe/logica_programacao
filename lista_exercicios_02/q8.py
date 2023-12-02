print("A duração mínima é de 1 minuto e a duração máxima é de 24 horas.")
hora_Inicial = int(input("Digite a hora inicial: "))
min_Inicial = int(input("Digite o minuto inicial: "))
hora_final = int(input("Digite a hora final: "))
min_final = int(input("Digite o minuto final: "))
hora_duracao = hora_Inicial - hora_final
if hora_duracao < 1:
        hora_duracao = hora_duracao * (-1)
        min_duracao = min_Inicial - min_final
if  min_duracao < 1:
        hduracao = hora_duracao * (-1)
        totalduracao = hora_duracao + min
if  totalduracao > 24:
         print("A duração tem que ser menor.")
elif totalduracao < 1:
         print("A duração tem que ser maior.")

print(f"O jogo durou {hora_duracao} horas e {min_duracao} minutos.")



