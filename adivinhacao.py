print("Bem vindo ao jogo de Adivinhação! Tente acertar o número secreto")
secreto = int(input("Primeiro peça a outra pessoa digitar um número qualquer entre 1 e 100): "))
while secreto < 1 or secreto > 100:
    secreto = int(input("Você digitou um número menor que 1 ou maior que 100, "
                        "digite NOVAMENTE um número qualquer entre 1 e 100): "))

loop = int(input("Agora digite quantas tentativas quer ter (max 100): "))
while loop > 100 or loop < 1:
    loop = int(input("Você digitou um número de tentativas menor que 1 ou "
                     "maior que 100, Digite um número de tentativas entre 1 e 100: "))

for i in range(1, loop + 1):
    chute = int(input("Digite o seu número : "))
    print("Você digitou ", chute)

    acertou = chute == secreto
    maior = chute > secreto
    menor = chute < secreto

    if acertou:
        print("ACERTOU!!!!")
        break
    else:
        if maior:
            print("ERROU!!! O CHUTE FOI MAIOR QUE O NÚMERO SECRETO")
            print("VOCÊ TEM ", loop - i, " TENTATIVA(S)")
        elif menor:
            print("ERROU!!! O CHUTE FOI MENOR QUE O NÚMERO SECRETO")
            print("VOCÊ TEM ", loop - i, " TENTATIVA(S)")
print("FIM DE JOGO     ")
