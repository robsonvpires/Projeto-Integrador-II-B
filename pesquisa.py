
lista_dados = [{'nome': 'dart', 'área_de_atuação': 'dart area', 'email': 'dar@gmail.com', 'telefone': '321', 'cnpj/cpf': '123456', 'lista_de_especialidades':''}, 
               {'nome': 'shot', 'área_de_atuação': 'shot area', 'email': 'shot@gmail.com', 'telefone': '123', 'cnpj/cpf': '567876', 'lista_de_especialidades':''}]

def cadastro_consultor():

    dados = dict()
    dados ['nome'] = input('Nome')
    dados ['área_de_atuação'] = input('Área de Atuação')
    dados ['email'] = input('E-mail')
    dados ['telefone'] = input('Telefone')
    dados ['cnpj/cpf'] = input('CNPJ/CPF')
    dados ['lista_de_especialidades'] = input('Lista de Especialidades')
    print(dados) 

def pesquisa_consultor():
    pesquisa = input("digite a sua pesquisa: ")
    lista_pesquisa = []

    tamanho = len(lista_dados)

    for i in range(tamanho):
        if pesquisa in (lista_dados[i]['nome']):
            lista_pesquisa.append(lista_dados[i]['nome'])

    print(f"foram encontrados os seguintes consultores: \n {lista_pesquisa}")

while True:
    menu = input("oque deseja fazer?\n1-cadastrar consultor\n2-pesquisar consultor")
    
    if menu == "1":
        cadastro_consultor()
    elif menu == "2":
        pesquisa_consultor()