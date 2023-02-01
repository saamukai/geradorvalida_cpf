from random import randint

def geraCpf():
    novo_cpf = str(randint(100000000, 999999999))
    reverso = 10            # variável contadora reverso para gerar o valor, vem da formula de validade de cpf
    soma = 0

    for index in range(19):
        if index > 8:               # primeiro indice vai de 0 a 9, depois "reseta" os indices para gerar o segundo digito
            index -= 9

        soma += int(novo_cpf[index])*reverso
        reverso -= 1
        if reverso < 2:
            reverso = 11
            dig = 11 - (soma % 11)

            if dig > 9:
                dig = 0

            soma = 0
            novo_cpf += str(dig)

    print('\n------------------------------------------')
    print(f'\nCPF GERADO: {novo_cpf}\n')
