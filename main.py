import random

pecas = []
tamanhos = ["P","M","G"]
cores = ["branco","preto","azul"]
for i in range(1,51):
    tamanho = random.choice(tamanhos)
    cor = random.choice(cores)
    pecas.append((tamanho,cor))

print(pecas)
pecasP = []
pecasM = []
pecasG = []

for item in pecas:
    if item[0] == "P":
        pecasP.append(item[0])
    else:
        if item[0] == "M":
            pecasM.append(item[0])
        else:
            if item[0] == "G":
                pecasG.append(item[0])

maior = 0
if len(pecasP)>len(pecasM) and len(pecasP)>len(pecasG):
    maior = pecasP
    print("O tamanho mais vendido foi o tamanho P.")
elif len(pecasM)>len(pecasP) and len(pecasM)>len(pecasG):
    maior = pecasM
    print("O tamanho mais vendido foi o tamanho m.")
else:
    maior = pecasG
    print("O tamanho mais vendido foi o tamanho G.")


tamanhoM = []
for item in pecas:
    if item[0] == 'M':
        tamanhoM.append(item[0])

print("Foram vendidas ", len(tamanhoM),"peças tamanho M.")

cormaisvendida = 0
corbranco = []
corpreto = []
corazul = []

for item in pecas:
    if item[1] == "branco":
        corbranco.append(item[1])
    else:
        if item[1] == "preto":
            corpreto.append(item[1])
        else:
            if item[1] == "azul":
                corazul.append(item[1])

if len(corbranco)>len(corpreto) and len(corbranco)>len(corazul):
    cormaisvendida = corbranco
    print("A cor preferida dos clientes foi a cor branco.")
elif len(corpreto)>len(corbranco) and len(corpreto)>len(corazul):
    cormaisvendida = corpreto
    print("A cor preferida dos clientes foi a cor preto.")
else:
    cormaisvendida = corazul
    print("A cor preferida dos clientes foi a cor azul.")





