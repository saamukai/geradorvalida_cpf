from gera_cpf import geraCpf
from valida_cpf import validaCpf

while True:
    print('--- GERADOR/VALIDADOR de CPFs ---')
    print('1 - Inserir CPF para Validar CPF\n2 - Gerar CPF\n3 - Sair')
    opcao = int(input('Escolha uma opcao: '))

    if opcao == 1:
        cpf_in = input("Digite um cpf: ")
        validaCpf(cpf_in)
    elif opcao == 2:
        geraCpf()
    else:
        break
