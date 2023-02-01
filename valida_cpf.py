from imprimir_resultado import imprimeResultado

def validaCpf (cpf_format):
    cpf = cpf_format.replace('.','').replace('-','')
    dig1 = 0
    dig2 = 0

    # verifica se o CPF não é uma sequencia
    sequencia = cpf == str(cpf[0]) * len(cpf)
    if sequencia:
        print('\nO CPF é uma sequência numérica e portando é inválido\n')
        return

    # iteração que vai trabalhar a cerca do primeiro digito depois do hifen
    multiplicador = 10
    soma = 0
    for index in range(0, 9, 1):
        produto = int(cpf[index])*multiplicador
        soma += produto
        multiplicador -= 1

    # formula para calculo do primeiro digito, dos ultimos dois digitos:
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
