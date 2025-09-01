def lin(tam,i):
    return i*tam

def exibe_cliente(dici, cpf):
    if cpf in dici:
        listinha = dici[cpf]
        print("CPF:", cpf)
        print("Nome:", listinha[0])
        print("Rua:", listinha[1])
        print("Cidade:", listinha[2])
        print("Telefone:", listinha[3])
        print("Data de nascimento:", listinha[4])
        print()
        input("Tecle <enter> para continuar...")

    else:
        print("Não há nenhum apartamento com código",cpf," Tente adicioná-lo no menu!")
        input("Tecle <enter> para continuar...")

def excluir(dici):
    cod=int(input("Tecle o CPF do cliente que deseja excluir:"))
    if cod in dici:
        print("Deletando cliente...")
        input("Tecle <enter> para continuar...")
        del dici[cod]
    else:
        print("Não há nenhum apartamento com código",cod," Tente adicioná-lo no menu!")
        input("Tecle <enter> para continuar...")


def alterar(dic):
    cod=int(input("Tecle o CPF do cliente:"))
    print()
    if cod in dic:
        print("Oque você deseja Alterar?")
        print(lin(72, "-"))
        print("1.CPF / 2.Nome / 3.Rua  / 4.Cidade / 5.Telefone / 6.Data de nascimento  ")
        print(lin(72, "-"))
        opc=int(input("Digite uma opção:"))
        if opc == 1:
            novo=int(input("Tecle o novo CPF do cliente :"))
            GUARDADO = dic[cod]
            del dic[cod]
            dic[novo] = GUARDADO
        elif opc == 2:
            nome = input("Digite o Nome do cliente:")
            listanova = dic[cod]
            listanova[0] = nome
            dic[cod] = listanova
        elif opc == 3:
            rua = input("Insira a Rua do cliente:")
            listanova = dic[cod]
            listanova[1] = rua
            dic[cod] = listanova
        elif opc == 4:
            cidade = input("Insira a Cidede do cliente:")
            listanova = dic[cod]
            listanova[2] = cidade
            dic[cod] = listanova
        elif opc == 5:
            elefone = int(input("Insira o número de ftelefone(Todo Junto!):"))
            listanova = dic[cod]
            listanova[3] = elefone
            dic[cod] = listanova
        elif opc == 6:
            data =input("Insira a data de nascimento no formato(dd/mm/aaaa):")
            listanova = dic[cod]
            listanova[4] = data
            dic[cod] = listanova
    
        print("Dados alterados com sucesso!")
        input("Tecle <enter> para continuar...")
    else:
        print("Não há nenhum apartamento com código", cod ," Tente adicioná-lo no menu!")
        input("Tecle <enter> para continuar...")


def incluir_cliente(dic):
    cpf = int(input("Insira o CPF do cliente:"))
    if cpf in dic:
        print(f"Um apartamento com o código {cpf} já foi cadastrado. Tente consultá-lo no menu!")
        input("Tecle <enter> para continuar...")
    else:
        nome = input("Insira o Nome do cliente:")
        endereco = input("Insira a Rua do cliente:")
        cidede = input("Insira a Cidede do cliente:")
        telefone = int(input("Insira o número de ftelefone(Todo Junto!):"))
        date =input("Insira a data de nascimento no formato(dd/mm/aaaa):")
        listacliente = [nome, endereco, cidede, telefone, date]
        dic[cpf] = listacliente
        print()
        print("Dados inseridos com sucesso!")
        input("Tecle <enter> para continuar...")


def exibe_todos(dici):
    if len(dici)==0:
        print("Não há nenhum cliente cadastrado, Tente adicionar algum no menu!")
        input("Tecle <enter> para continuar...")
    else:
        for chave in dici:
            print("CPF:",chave)
            listinha=dici[chave]
            print("Nome:",listinha[0])
            print("Rua:",listinha[1])
            print("Cidade:",listinha[2])
            print("Telefone:",listinha[3])
            print("Data de nascimento:",listinha[4])
            print(lin(30,"-"))
        




