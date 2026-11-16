pontos = 0
certos = 0

perguantas = [
    "Qual é o maior animal terrestre do mundo: ",
    "Quanto é 8 x 8 + 4: ",
    "Qual é o planeta mais quente do sistema solar: ",
    "Em que ano o homem pisou na Lua pela primeira vez: ",
    "Quantos corações tem um polvo: ",
]
respostas = ["elefante", "68", "vênus", "1969", "3"]

for i in range(5):
    resposta = input(perguantas[i]).lower()
    if resposta == respostas[i]:
        print("Resposta correta!")
        pontos += 1
        certos += 1
    else:
        print(f"Errou! Próxima pergunta.")

print(f"Você marcou {pontos} ponto!, acertando {certos} perguntas.")
if pontos == 5:
    print("Você acertou todas as perguntas muito bem.")
elif pontos >= 2:
    print("Você acertou muitas, na próxima você sai melhor.")
else:
    print("O impotante e participar.")
