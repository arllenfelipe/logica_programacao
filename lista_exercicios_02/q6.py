A = float(input("Digite o valor A: "))
B = float(input("Digite o valor B: "))
C = float(input("Digite o valor C: "))
equilatero = A == B == C
eita = ((B**2) + (C**2))
opa = (A**2)
if A >= (B + C):
        print("Não forma triângulo.")
else:
        if opa == eita:
            print("Triângulo retângulo.")
        elif opa > eita:
            print("Triângulo obtusângulo.")
        elif opa < eita:
            print("Triângulo acutangulo.")
if equilatero == False and A == B or A == C or B == C:
            print("Triângulo isosceles.")
elif equilatero == True:
        print("Triângulo equilatero.")