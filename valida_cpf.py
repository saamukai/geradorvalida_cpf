# algumas das coisas realizadas abaixo são regras da validação de cpf

def imprimeResultado(cpf_format, value):
    if value == True:
        print('\n------------------------------------------')
        print(f'O CPF ({cpf_format}) é válido\n\n')
    else:
        print('\n-------------------------------------------')
        print(f'O CPF ({cpf_format}) é  inválido\n\n')



def validaCpf (cpf_format):
    cpf = cpf_format.replace('.','').replace('-','')
    dig1 = 0
    dig2 = 0

    # iteração que vai trabalhar a cerca do primeiro digito depois do hifen
    multiplicador = 10
    soma = 0
    for index in range(0, 9, 1):
        produto = int(cpf[index])*multiplicador
        soma += produto
        multiplicador -= 1

    #formula para calculo do primeiro digito, dos ultimos dois digitos:
    if 11 - (soma %11) > 9:
        dig1 = 0
    else:
        dig1 = 11 - (soma %11)

    # ja verifica se o primeiro digito encontrado é igual ao informado, caso contrario o cpf é invalido e já finaliza
    if dig1 != int(cpf[9]):
        imprimeResultado(cpf_format, False)
        return

    # iteração que vai trabalhar a cerca do primeiro digito depois do hifen
    multiplicador = 11
    soma = 0
    for index in range (0, 10, 1):
        produto = int(cpf[index])*multiplicador
        soma += produto
        multiplicador -= 1

    dig2 = 11 - (soma%11)

    # ja verifica se o primeiro digito encontrado é igual ao informado, caso contrario o cpf é invalido e já finaliza
    if dig2 != int(cpf[10]):
        imprimeResultado(cpf_format, False)
        return

    # se chegar até aqui, significa que o cpf cumpriu as regras e é valido
    imprimeResultado(cpf_format, True)
    return


while True:
    print('--- GERADOR/VALIDADOR de CPFs ---')
    print('1 - Gerar CPF\n2 - Inserir CPF\n3 - Sair')
    opcao = int(input('Escolha uma opcao: '))

    if opcao == 1:
        pass
    if opcao == 2:
        cpf_in = input("Digite um cpf: ")
        validaCpf(cpf_in)
    else:
        break
