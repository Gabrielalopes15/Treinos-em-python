#Calculadora
op = " "
def menu():
    print("---Bem vindo--- \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão")
        
menu()
id_menu = int(input("Informe a operaçao desejada:"))

p_num = float(input("Informe o primeiro operador:\n"))

s_num = float(input("Informe o segundo operador:\n")) 
if id_menu == 1:
        total = p_num + s_num
        op = "+"
elif id_menu == 2:
        total = p_num - s_num
        op = "-"
elif id_menu == 3:
        total = p_num * s_num
        op = "*"
elif id_menu == 4:
        total = p_num / s_num
        op ="//"
else:
        print("Essa opcao não existe")
        menu()
        
print(f' Você escolheu {op} \n {p_num} {op} {s_num} = {total}')
