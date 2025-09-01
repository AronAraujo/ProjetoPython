from submenus import *

Dic_Clientes={}
Dic_Reservas={}
Dic_Aps={}

if existe_arquivo("clientes.txt"):
    lerarq_clientes(Dic_Clientes)

retorno=menu(["Submenu Clientes" , "Submenu Apartamentos", "Submenu Reservas " , "Relatorio" , "Finalizar"],"PROGRAMA PRINCIPAL",42,"°")

while retorno != 5:
        if retorno == 1:
            menuclientes(Dic_Clientes)
        elif retorno == 2:
            menuaps(Dic_Aps) 
        elif retorno == 3:
            menures(Dic_Reservas)
        elif retorno == 4:
            relatorio(Dic_Reservas)       
        else:
            print()
            print("------------<Erro>------------")
            print("Dgite um número entre 1 a 5...")
            input("Tecle <enter> para continuar...")
            print()
        
        retorno=menu(["Submenu Clientes" , "Submenu Apartamentos", "Submenu Reservas " , "Relaçoes" ,  "Finalizar"],"PROGRAMA PRINCIPAL",42,"°")


gravaarqc(Dic_Clientes)
print()
print("Dados gravados com sucesso...")
print("Finalizando Programa...")
