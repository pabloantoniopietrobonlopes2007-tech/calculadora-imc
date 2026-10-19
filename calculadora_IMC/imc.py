def calcular_imc(peso,altura):
    imc = peso/(altura**2)
    return imc

def classificacao_imc(imc):
    if imc < 18.5: return "Magreza / Baixo peso"
    elif imc <= 24.9: return "Peso normal (ideal)"
    elif imc <= 29.9: return "Sobrepeso (Grau I)"
    elif imc <= 34.9: return "Obesidade Grau I"
    elif imc <= 39.9: return "Obesidade Grau II (Severa)"
    else: return "Obesidade Grau III (Mórbida / Grave)"

def validacao(msg):
    num=None
    while(num is None):
        try:
            num = float(input(msg))
            if num<=0:
                print("Dado incorreto.")
                num=None
        except ValueError:
            print("Tipo de dado incorreto.")
            num=None
    return num
        

peso = validacao("Qual seu peso? ")
altura = validacao("Qual sua altura? ")
        
imc = calcular_imc(peso,altura)
classificacao = classificacao_imc(imc)

print(f"Seu IMC é {imc:.2f}.")
print(f"Você esta em {classificacao}") 