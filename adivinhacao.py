import random

continuar = 1
while continuar == 1:
    print("Bem vindo ao jogo de Adivinhação! Tente acertar o número secreto")
    option = int(input('Antes de começar gostaria que o jogo definisse o número secreto'
                       ' ou uma pessoa? digite 1 para Jogo ou 0 para Pessoa: '))
    if option == 0:
        secreto = int(input("Primeiro peça a outra pessoa digitar um número qualquer entre 1 e 100): "))
        while secreto < 1 or secreto > 100:
            secreto = int(input("Você digitou um número menor que 1 ou maior que 100, "
                                "digite NOVAMENTE um número qualquer entre 1 e 100): "))

        loop = int(input("Agora digite quantas tentativas quer ter (max 100): "))
        while loop > 100 or loop < 1:
            loop = int(input("Você digitou um número de tentativas menor que 1 ou "
                             "maior que 100, Digite um número de tentativas entre 1 e 100: "))
    else:
        secreto = int(random.randrange(1, 101))
        print("Defina o nível de dificuldade")
        nivel = int(input("(1) fácil (2) médio (3) difícil: "))
        if nivel == 1:
            loop = int(random.randrange(15, 30))
        elif nivel == 2:
            loop = int(random.randrange(8, 10))
        else:
            loop = int(random.randrange(1, 5))

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
    print("FIM DE JOGO O NÚMERO SECRETO ERA ", secreto)
    continuar = int(input("Deseja jogar novamente? 1 pra sim e 0 pra não: "))
