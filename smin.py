#lista de todos os fornecedores
lista_fornecedores = [[]]

def cadastro_fornecedor():

    #lista com todos os dados do fornecedor
    fornecedor = []

    #lista com os produtos que o fornecedores criar
    lista_produtos = []

    fornecedor_nome = input("digite seu nome completo: ")
    
    fornecedor_area = ""
    fornecedor_email = ""
    arroba = "@"
    pontocom = ".com"
    
    fornecedor_telefone = ""
    fornecedor_cpf = ""

    #verifica se a area de atuação não esta em branco
    while len(fornecedor_area) < 2:
        fornecedor_area = input("qual sua area de atuação: ")
        if (len(fornecedor_area)) < 2:
            print("nome muito curto, tente denovo")

    #verifica se o email é valido
    while (len(fornecedor_email) < 6) or (arroba not in fornecedor_email or pontocom not in fornecedor_email):
        
        fornecedor_email = input("digite o seu email: ")
        if (len(fornecedor_email) < 6) or (arroba not in fornecedor_email or pontocom not in fornecedor_email):
            print("email invalido, digite um email valido")
                

    #verifica se o numero tem pelo menos 9 digitos, se não pede novamente
    while len(fornecedor_telefone) < 9:
        fornecedor_telefone = input("digite o seu telefone: ")
        if len(fornecedor_telefone) < 9:
            print("numero incompleto, pelo menos 9 digitos")

    #verifica se o cpf tem o numero certo de digitos, se não pede cpf novamente
    while len(fornecedor_cpf) != 11 :
        fornecedor_cpf = input("digite o seu CPF/CNPJ: ")
        if len(fornecedor_cpf) != 11:
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