from pymongo import MongoClient
from datetime import datetime

# Configurar conexão com o MongoDB local
client = MongoClient('mongodb://localhost:27017/')
db = client['loja']  # Nome do banco de dados
collection = db['produtos']  # Nome da coleção

# Função para inserir um novo produto
def inserir_produto():
    nome_produto = input("Digite o nome do novo produto: ")
    descricao = input("Digite a descrição do produto: ")
    preco = float(input("Digite o preço do produto: "))
    estoque = int(input("Digite a quantidade em estoque: "))
    
    # Criar dicionário com os dados do novo produto
    novo_produto = {
        'nome': nome_produto,
        'descricao': descricao,
        'preco': preco,
        'estoque': estoque,
        'data_criacao': datetime.now()  # Armazena a data e hora da criação
    }
    
    # Inserir o novo produto no MongoDB
    resultado = collection.insert_one(novo_produto)
    
    # Verificar se a inserção foi bem-sucedida
    if resultado.inserted_id:
        print(f"Produto '{nome_produto}' foi inserido com sucesso. ID: {resultado.inserted_id}")
    else:
        print("Ocorreu um erro ao inserir o produto.")


# Função para listar todos os produtos
def listar_produtos():
    produtos = collection.find()  # Buscar todos os documentos da coleção
    for produto in produtos:
        print(f"Nome: {produto['nome']}")
        print(f"Descrição: {produto['descricao']}")
        print(f"Preço: R$ {produto['preco']}")
        print(f"Estoque: {produto['estoque']}")
        print(f"Data de Criação: {produto['data_criacao']}")
        print('-' * 40)


# Função para atualizar produtos
def atualizar_produtos():
    nome_produto = input("Digite o nome do produto a ser atualizado: ")
    
    # Solicitar novos dados ao usuário
    nome_produto_atualizado = input("Digite o novo nome do produto: ")
    descricao_atualizada = input("Digite a nova descrição: ")
    preco_novo = float(input("Digite o novo preço: "))
    estoque_novo = int(input("Digite o novo estoque: "))

    novos_dados = {
        'nome': nome_produto_atualizado,
        'descricao': descricao_atualizada,
        'preco': preco_novo,
        'estoque': estoque_novo
    }

    # Atualizar o produto no MongoDB
    resultado = collection.update_one(
        {'nome': nome_produto},  # Filtro: produto com o nome especificado
        {'$set': novos_dados}    # Dados que serão atualizados
    )
    
    # Verificar se o produto foi encontrado e atualizado
    if resultado.matched_count > 0:
        print(f"Produto '{nome_produto}' foi atualizado com sucesso.")
    else:
        print(f"Nenhum produto com o nome '{nome_produto}' foi encontrado.")


# Função para deletar produto
def deletar_produto():
    nome_produto = input("Digite o nome do produto que deseja deletar: ")

    # Deletar o produto no MongoDB
    resultado = collection.delete_one({'nome': nome_produto})  # Filtrar pelo nome do produto

    # Verificar se algum produto foi deletado
    if resultado.deleted_count > 0:
        print(f"Produto '{nome_produto}' foi deletado com sucesso.")
    else:
        print(f"Nenhum produto com o nome '{nome_produto}' foi encontrado.")


# Função para exibir o menu
def menu():
    while True:
        print("\nMenu de Operações:")
        print("1. Criar produto")
        print("2. Listar produtos")
        print("3. Atualizar produto")
        print("4. Deletar produto")
        print("5. Sair")
        
        escolha = input("Escolha uma opção (1-4): ")
  
        opcoes = {
            '1': inserir_produto,
            '2': listar_produtos,
            '3': atualizar_produtos,
            '4': deletar_produto,
            '5': sair
        }
        
        funcao = opcoes.get(escolha)  # Obter a função correspondente à escolha
        
        if funcao:
            funcao()  # Executar a função
        else:
            print("Opção inválida. Tente novamente.")
        
        if escolha == '4':  # Sair do loop se o usuário escolher 'Sair'
            break


# Função para sair do programa
def sair():
    print("Saindo do programa.")
    exit()


# Executar o menu
menu()