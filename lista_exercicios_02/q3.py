instalacao = input("Digite a letra que representa o tipo da sua instalação:\nR - Residencial\nC - Comercial\nI - Industrial\n")
consumo = int(input("Digite a quantidade de kWh consumido: "))
if instalacao == "R" or "r":
 if consumo <= 500:
            consumo = consumo * 0.40 
elif consumo > 500:
            consumo = consumo * 0.65
elif instalacao == "C" or "c":
        if consumo <= 1000:
            consumo = consumo * 0.55
        elif consumo > 1000:
            consumo = consumo * 0.60
elif instalacao == "I" or "i":
        if consumo <= 5000:
            consumo = consumo * 0.55
        elif consumo > 5000:
            consumo = consumo * 0.60
else: print("Ocorreu um erro. Tente novamente.")
print(f"Você deverá pagar {consumo} R$.")
