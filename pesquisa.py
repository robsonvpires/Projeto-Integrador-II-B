
lista_dados = [{'nome': 'relogios', 'descrição': 'vendo e compro relogios', 'ID': '1', 'categoria': 'venda', 'consultor': 'romario'},
                {'nome': 'cadeiras', 'descrição': 'vendo e compro cadeiras', 'ID': '2', 'categoria': 'venda', 'consultor': 'cezar'}]

def cadastro_especialidade():       
    dados = dict()
    dados ['nome'] = input('Nome')
    dados ['descrição'] = input('Descrição')
    dados ['ID'] = input('ID')
    dados ['categoria'] = input('Caregoria')
    dados ['consultor'] = input('Consultor')
    lista_dados.append(dados)

    print(lista_dados) 

def pesquisa_consultor():
    pesquisa = input("digite a sua pesquisa: ")
    lista_pesquisa = []

    tamanho = len(lista_dados)

    for i in range(tamanho):
        if pesquisa in (lista_dados[i]['nome']):
            lista_pesquisa.append(lista_dados[i]['consultor'])

    print(f"foram encontrados os seguintes consultores: \n {lista_pesquisa}")

while True:
    menu = input("oque deseja fazer?\n1-cadastrar especialidade\n2-pesquisar por especialidade")
    
    if menu == "1":
        cadastro_especialidade()
    elif menu == "2":
        pesquisa_consultor()