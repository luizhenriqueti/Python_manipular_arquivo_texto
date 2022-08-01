def leiaInt(msg):
    valor = 0
    while True:
        try:
            validator = str(input(msg))
            valor = int(validator)
        except ValueError:
            print(f'\033[31mERRO!: este não é um numero inteiro\033[m')
        else:
            break
    return valor


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c} - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[33mSua opção: \033[m')
    return opc

