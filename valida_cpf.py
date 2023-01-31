cpf_in = input("Digite um CPF: ")
# algumas das coisas realizadas abaixo são regras da validação de cpf

def validaCpf (cpf_format):
    cpf = cpf_format.replace('.','').replace('-','') # 16899535209
    print(cpf)
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
        print(f'O CPF ({cpf_format}) informado, é inválido')
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
        print(f'O CPF ({cpf_format}) informado, é inválido')
        return

    # se chegar até aqui, significa que o cpf cumpriu as regras e é valido
    print(f'O CPF ({cpf_format}) informado, é realmente válido')
    return


validaCpf(cpf_in)
