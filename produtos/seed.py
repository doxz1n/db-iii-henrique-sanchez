# Feito por Henrique Alcici Sanchez - 3° DS

from pymongo import MongoClient
from faker import Faker
import random

# Configurar conexão com o MongoDB local
client = MongoClient('mongodb://localhost:27017/')
db = client['loja']  # Nome do banco de dados
collection = db['produtos']  # Nome da coleção

# Gerador de dados aleatórios
fake = Faker('pt_BR')

# Função para criar um produto aleatório
def criar_produto():
    return {
        'nome': fake.word().capitalize() + ' ' + fake.word().capitalize(),
        'descricao': fake.text(max_nb_chars=50),
        'preco': round(random.uniform(10.0, 1000.0), 2),
        'estoque': random.randint(1, 100),
        'data_criacao': fake.date_time_this_year(),
    }

# Gerar e inserir 150 produtos no MongoDB
produtos = [criar_produto() for _ in range(150)]
collection.insert_many(produtos)

print("150 produtos foram inseridos com sucesso no MongoDB!")