import fclientes
from datetime import *
from ApRes import *
################################################
def lin(tam,i):
    return i*tam

def cabecalho(txt,tam,i):
    print(lin(tam,i))
    print(txt.center(42))
    print(lin(tam,i))

def menu(lis,txt,tam,i):
    cabecalho(txt,tam,i)
    a=1
    for guardado in lis:
        print(a,"-",guardado)
        a = a+1
    print()
    opc=int(input("Digite uma opção:"))
    return opc

################################################

def lerarq_clientes(dici):
    arq=open("clientes.txt","r")
    for linha in arq:
        linha = linha[:-1]
        listinha=linha.split("#")
        cpf= int(listinha[0])
        del listinha[0]
        tel=int(listinha[3])
        listinha[3]=tel
        dici[cpf] = listinha
    arq.close()

def gravaarqc(dicionario):
    arq=open("clientes.txt","w")
    for chave in dicionario:
        cliente=dicionario[chave]
        string = str(chave) + "#" + cliente[0] + "#" + cliente[1] + "#" + cliente[2] + "#" + str(cliente[3]) + "#" + cliente[4]  + "\n"
        arq.write(string)
    arq.close()        

def existe_arquivo(arq):
    import os
    if os.path.exists(arq):
        return True
    else:
        return False

################################################

def menuclientes(DIC): 

    retorno=menu(["Incluir" , "Listsar todos", "Listar um cliente específico " , "Alterar" , "Excluir" ,"Voltar para o programa principal"],"Menu de Clientes",21,"==")

    while retorno != 6:
        if retorno == 1:
            print()
            fclientes.incluir_cliente(DIC)
        elif retorno == 2:
            print()
            fclientes.exibe_todos(DIC)
        elif retorno == 3:
            print()
            CPF=int(input("Tecle o CPF do cliente que deseja exibir:"))
            fclientes.exibe_cliente(DIC,CPF)
        elif retorno == 4:
            print()
            fclientes.alterar(DIC)
        elif retorno == 5:
            print()
            fclientes.excluir(DIC)
     
        else:
            print()
            print("------------<Erro>------------")
            print("Dgite um número entre 1 a 6...")
            input("Tecle <enter> para continuar...")
            print()

        retorno=menu(["Incluir" , "Listsar todos", "Listar um cliente específico " , "Alterar" , "Excluir" ,"Voltar para o programa principal"],"Menu de Clientes",21,"==")
        print()
    

def menuaps(DIC): 

    retorno=menu(["Incluir" , "Listsar todos", "Listar um apartemento específico " , "Alterar" , "Excluir" ,"Voltar para o programa principal"],"Menu de Apartamentos",21,"==")
    while retorno != 6:
        if retorno == 1:
            print()
            addap(DIC)
        elif retorno == 2:
            print()
            exibirtdsap(DIC)
        elif retorno == 3:
            print()
            exibirumap(DIC)
        elif retorno == 4:
            print()
            exibirumap(DIC)
        elif retorno == 5:
            print()
            excluirap(DIC)
            
        else:
            print()
            print("------------<Erro>------------")
            print("Dgite um número entre 1 a 6...")
            input("Tecle <enter> para continuar...")
            print()

        retorno=menu(["Incluir" , "Listsar todos", "Listar um apartemento específico " , "Alterar" , "Excluir" ,"Voltar para o programa principal"],"Menu de Apartamentos",21,"==")
        print()
    
def menures(DIC): 

    retorno=menu(["Incluir" , "Listsar todos", "Listar um apartemento específico " , "Alterar" , "Excluir" ,"Voltar para o programa principal"],"Menu de Reservas",21,"==")
    while retorno != 6:
        if retorno == 1:
            print()
            addres(DIC)
        elif retorno == 2:
            print()
            exibirtdsres(DIC)
        elif retorno == 3:
            print()
            exibirumres(DIC)
        elif retorno == 4:
            print()
            exibirumres(DIC)
        elif retorno == 5:
            print()
            excluirumres(DIC)
            
        else:
            print()
            print("------------<Erro>------------")
            print("Dgite um número entre 1 a 6...")
            input("Tecle <enter> para continuar...")
            print()

        retorno=menu(["Incluir" , "Listsar todos", "Listar um apartemento específico " , "Alterar" , "Excluir" ,"Voltar para o programa principal"],"Menu de Reservas",21,"==")
        print()



def relatorio(dicionario):
    print("Essa função mostra as reservas ente uma data X e Y...")
    if len(dicionario)==0:
        print("Não há nenhuma reserva!")
        input("Tecle <enter> para continuar...")
    else:
        print("Digite as datas no formato dd/mm/aaaa :")
        s1=input("Digite a primeira data:")
        s2=input("Digite a segunda data:")
        d2 = datetime.strptime(s2, '%d/%m/%Y')
        d1 = datetime.strptime(s1, '%d/%m/%Y')
        if d1>d2:
            print("A primeira data deve ser menor que a segunda")
            input("Tecle <enter> para voltar...")
        else:
            achou=False
            for chave in dicionario:
                guardado=chave
                lista=dicionario[chave]
                entrada=guardado[2]
                saida=guardado[3]
                Dentrada = datetime.strptime(entrada, '%d/%m/%Y')
                Dsaida = datetime.strptime(saida, '%d/%m/%Y')
                if d1 <= Dentrada <= d2 and d1 <= Dsaida <= d2 :
                    achou=True
                    print("Código do Apartamento:", guardado[0])
                    print("Cpf do Cliente:", guardado[1])
                    print("Data de Entrada:", entrada)
                    print("Data de Saída:", saida)
                    for elemento in lista:
                        print("Nome dos Ocupantes: ", elemento)
                        print(lin(30,"-"))

            if achou==False:
                print("Não há nenhuma reserva entre essas duas datas!")
                input("Tecle <enter> para continuar...")
                    
