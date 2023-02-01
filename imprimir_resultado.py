def imprimeResultado(cpf_format, value):
    print('\n------------------------------------------')
    if value:
        print(f'O CPF ({cpf_format}) é válido\n\n')
    else:
        print(f'O CPF ({cpf_format}) é  inválido\n\n')
