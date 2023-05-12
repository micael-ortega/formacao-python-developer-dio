
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
from datetime import datetime
from pprint import pprint


load_dotenv()

mongodb_password = os.getenv('MONGODB_PASSWORD')
mongodb_user = os.getenv('MONGODB_USER')

uri = f"mongodb+srv://{mongodb_user}:{mongodb_password}@cluster0.ubia2zd.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

db = client.test

collection = db.bank


documents = [{
    "nome": "Micael",
    "cpf": "777777",
    "endereco": "Rua dos Bobos Nº 0",
    "conta": "0001",
    "agencia": "6547",
    "tipo": "Conta Corrente",
    "saldo": "1000"
},
    {
    "nome": "Lua",
    "cpf": "99998",
    "endereco": "Rua 10",
    "conta": "0002",
    "agencia": "4765",
    "tipo": "Conta Corrente",
    "saldo": "10000000"
}]

insert_result = collection.insert_many(documents)

print(insert_result.inserted_ids)

query_conta = {'tipo':'Conta Corrente'}
query_nome = {'nome': 'Lua'}

results = collection.find(query_conta)
print('\nResultado de query por tipo de conta')
for result in results:
    print(result)

results = collection.find(query_nome)
print("\nResultado de query por nome")
for result in results:
    print(result)
print(db.list_collection_names())
