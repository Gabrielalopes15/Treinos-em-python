
cad_login = []
cad_nome = []
cad_tel = []
cad_email = []

def menu():
    print("\n 1 - Cadastrar \n 2 - Consultar \n 3 - Remover \n 4 - Sair")
    id_menu = int(input("Informe a opção: "))
    return id_menu

def retorna_menu():
    print("Deseja retornar ao menu? (sim/não)")
    if input().lower() == "sim":
        return menu()
    else:   
        return 4
    
def login():
    nome = input("Informe seu nome: \n")
    cad_login.append(nome)
    return nome

# Captura o valor retornado pela função login
nome = login()

def cadastro():
    nome_cliente = str(input("Informe o nome do cliente: \n"))
    cad_nome.append((nome_cliente))
    telefone = int(input("Informe o telefone: \n"))
    cad_tel.append(( telefone,))
    email = str(input("Informe o email: \n"))
    cad_email.append(( email))
    return nome_cliente, telefone, email

def consulta():
    print("Lista de clientes: \n|   Nome              |      Telefone      |         E-mail             |")
    for j in range(0, len(cad_nome)):
        print(f"|         {cad_nome[j]}    | {cad_tel[j]}        | {cad_email[j]}           |")
def remove():
    for i, cliente in enumerate(cad_nome):
        print(f"\n| Id      |   Nome              |      Telefone      |         E-mail             |")
        print(f"___________________________________________________________________________________" )
        print(f"| {i}       |{cad_nome[i]}        | {cad_tel[i]}       | {cad_email[i]}             |")
    id = int(input("Informe o índice do item que deseja remover: "))
    if 0 <= id < len(cad_nome):
        cad_nome.pop(id)
        cad_tel.pop(id)
        cad_email.pop(id)
    else:
        print("Índice inválido")

print(f'--- Bem vindo {nome} ---')
id_menu = menu()

while id_menu != 4:
    if id_menu == 1:
        cadastro()
    elif id_menu == 2:
        consulta()
    elif id_menu == 3:
        remove()
    else:
        print("Opção Inválida")
    
    id_menu = retorna_menu()
