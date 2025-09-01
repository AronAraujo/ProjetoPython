def addap(apartamentos):
    lista = []
    codigo = int(input('Qual o código do apartamento? '))
    if codigo in apartamentos :
        print(f"Um apartamento com o código {codigo} já foi cadastrado. Tente consultá-lo no menu!")
        input("Tecle <enter> para continuar...")
    
    else:
        tipo = input('Qual o tipo do apartamento? (Standard / Pro / Superpro)  ')
        pessoas = int(input('Quantas pessoas são a capacidade máxima do apartamento? '))
        valor = int(input('Qual o valor da diária em R$? '))
        lista.append(tipo)
        lista.append(pessoas)
        lista.append(valor)
        apartamentos[codigo] = lista


def alterarap(apartamentos):
    lista = []
    codigo = int(input('Qual o código do apartamento? '))
    if codigo in apartamentos is True:
        tipo = input('Qual o tipo do apartamento? (Standard / Pro / Superpro)  ')
        pessoas = int(input('Quantas pessoas são a capacidade máxima do apartamento? '))
        valor = int(input('Qual o valor da diária em R$? '))
        lista.append(tipo)
        lista.append(pessoas)
        lista.append(valor)
        apartamentos[codigo] = lista
    else:
        print(f"Não há nenhum apartamento com o código {codigo} cadastrado. Tente adicioná-lo no menu!")
        input("Tecle <enter> para continuar...")


def exibirtdsap(apartamentos):
    if len(apartamentos) == 0:
        print("Não há nenhum apartamento cadastrado. Tente adicionar algum no menu!")
        input("Tecle <enter> para continuar...")
    else:
        for chave in apartamentos:
            print("Código do Apartamtnto:", chave)
            listinha = apartamentos[chave]
            print("Tipo do Apartamento:", listinha[0])
            print(f"Lotação Máxima do apartamento: {listinha[1]} pessoas")
            print("Preço:",listinha[2])
           
           


def exibirumap(apartamentos):
    codigo = input('Qual é o código? ')
    if codigo in apartamentos:
        listinha = apartamentos[codigo]
        print("CPF:", codigo)
        print("Nome:", listinha[0])
        print("Rua:", listinha[1])
        print("Cidade:", listinha[2])
        print("Telefone:", listinha[3])
        print("Data de nascimento:", listinha[4])
        print()
        input("Tecle <enter> para continuar...")

    else:
        print(f"Não há nenhum apartamento com código {codigo} Tente adicioná-lo no menu!")
        input("Tecle <enter> para continuar...")


def excluirap(apartamentos):
    codigo = int(input("Tecle o código do apartamento que deseja excluir: "))
    if codigo in apartamentos:
        del apartamentos[codigo]
        print('Apartamento deletado com sucesso! ')
        input("Tecle <enter> para continuar...")
    else:
        print(f"Não há nenhum apartamento com o código {codigo}. Tente cadastrá-lo no menu! ")
        input("Tecle <enter> para continuar...")


def addres(reservas):
    lista = []
    codigo = int(input('Qual o código do apartamento? '))
    cpf = int(input('Qual o CPF do cliente? '))
    entrada = input('Digite a data de entrada "no formato dd/mm/aaaa ":')
    saida = input('Digite a data de saída "no formato dd/mm/aaaa ":')
    chave = (codigo, cpf, entrada, saida,)
    if chave in reservas:
        print(f"Uma reserva como essa já foi cadastrada. Tente consultá-la no menu!")
        input("Tecle <enter> para continuar...")
    else:   
        nome = input('Nome dos ocupantes ("fim" para parar)')
        flag=False
        while nome != 'fim':
            if flag == False:
                lista.append(nome)
                flag=False
            nome = input('Nome dos ocupantes ("fim" para parar)')
            for elementos in lista:
                if nome == elementos:
                    print(f'O nome {elementos} já foi cadastrado!')
                    input('Tecle <enter> para continuar...')
                    flag=True
        reservas[chave] = lista



def alterarres(reservas):
    lista = []
    codigo = int(input('Qual o código do apartamento? '))
    cpf = int(input('Qual o CPF do cliente? '))
    entrada = input('Digite a data de entrada "no formato dd/mm/aaaa ":')
    saida = input('Digite a data de saída "no formato dd/mm/aaaa ":')
    chave = (codigo, cpf, entrada, saida,)
    if chave in reservas is True:
        nome = input('Nome dos ocupantes ("fim" para parar)')
        while nome != 'fim':
            lista.append(nome)
            nome = input('Nome dos ocupantes ("fim" para parar)')
            for elementos in lista:
                if nome == elementos:
                    print(f'O nome {elementos} já foi cadastrado!')
                    input('Tecle <enter> para continuar...')
        reservas[chave] = lista
        
    else:
        print(f"Não há nenhuma reserva como essa cadastrada. Tente adicioná-la no menu!")
        input("Tecle <enter> para continuar...")


def exibirtdsres(reservas):
    if len(reservas) == 0:
        print("Não há nenhum apartamento cadastrado. Tente adicionar algum no menu!")
        input("Tecle <enter> para continuar...")
    else:
        for chave in reservas:
            Lista=[chave]
            elemento = chave
            print("Código do Apartamento:", elemento[0])
            print("Cpf do Cliente:", elemento[1])
            print("Data de Entrada:", elemento[2])
            print("Data de Saída:", elemento[3])
            for elementos in Lista:
                print("Nome dos Ocupantes: ", elementos)


def exibirumres(reservas):
    codigo = int(input('Qual o código do apartamento? '))
    cpf = int(input('Qual o CPF do cliente? '))
    entrada = input('Digite a data de entrada "no formato dd/mm/aaaa ":')
    saida = input('Digite a data de saída "no formato dd/mm/aaaa ":')
    chave = (codigo, cpf, entrada, saida,)
    if chave in reservas:
        tupla = chave
        print("Código do Apartamento:", tupla[0])
        print("Cpf do Cliente:", tupla[1])
        print("Data de Entrada:", tupla[2])
        print("Data de Saída:", tupla[3])
        for elementos in chave.values():
            print("Nome dos Ocupantes: ", elementos)
        print()
        input("Tecle <enter> para continuar...")

    else:
        print(f"Não há nenhuma apartamento com código {codigo} Tente adicioná-lo no menu!")
        input("Tecle <enter> para continuar...")


def excluirumres(reservas):
    codigo = int(input("Tecle o código do apartamento que deseja excluir: "))
    cpf = int(input('Qual o CPF do cliente? '))
    entrada = input('Digite a data de entrada "no formato dd/mm/aaaa ":')
    saida = input('Digite a data de saída "no formato dd/mm/aaaa ":')
    chave = (codigo, cpf, entrada, saida,)
    if chave in reservas:
        del reservas[chave]
        print('Apartamento deletado com sucesso! ')
        input("Tecle <enter> para continuar...")
    else:
        print(f"Não há nenhuma reserva como essa. Tente cadastrá-lo no menu! ")
        input("Tecle <enter> para continuar...")

