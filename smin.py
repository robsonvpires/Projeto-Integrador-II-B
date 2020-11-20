#lista de todos os fornecedores
lista_fornecedores = [[]]

def cadastro_fornecedor():

    #lista com todos os dados do fornecedor
    fornecedor = []

    #lista com os produtos que o fornecedores criar
    lista_produtos = []

    fornecedor_nome = input("digite seu nome completo: ")
    
    fornecedor_area = input("qual sua area de atuação: ")
    fornecedor_email = input("digite o seu email: ")
    fornecedor_telefone = input("digite o seu telefone: ")
    fornecedor_cpf = ""

    #verifica se o cpf tem pelo menos 10 digitos, se não pede cpf novamente
    while len(fornecedor_cpf) < 10:
        fornecedor_cpf = input("digite o seu CPF/CNPJ: ")
        if len(fornecedor_cpf) < 10:
            print("cpf não valido")
         
    #adiciona todos os itens na lista do fornecedor
    fornecedor.append(fornecedor_nome)
    fornecedor.append(fornecedor_area)
    fornecedor.append(fornecedor_email)
    fornecedor.append(fornecedor_telefone)
    fornecedor.append(fornecedor_cpf)

    #adiciona a lista do fornecedor a lista de fornecedores
    lista_fornecedores.append(fornecedor)
    print("cadastro realizado com sucesso!")
    print(lista_fornecedores)
    
while True: 
    menu = input("oque deseja fazer? \n 1-cadastrar fronecedor")

    if menu == "1":
        cadastro_fornecedor()