import csv
from pymongo import MongoClient
import model.palavra as pa
import model.dicionario as dc
from flask import Blueprint, request, jsonify
db = MongoClient('mongodb://localhost:27017')

collection = db.dicionario_db.dicionario #COLLECTION CALLED DEVELOPERS
dicionario = Blueprint('dicionario', __name__)

class ImportDicionario(object):

    def __init__(self, linguagem):
        self.linguagem = linguagem
        self.dicionario = dc.Dicionario()

    def createDB(self, host, port):
          client = MongoClient(host, port) #localhost", 27017
          database = client["dicionario_db"]
          list_of_db = client.list_database_names()
          print(list_of_db)
          if "dicionario_db" in list_of_db:
            print("O Banco de Dados já existe.")
          else:
            print("Criando o Banco de Dados")

          return database

    def fromCsv(self):
        lista_palavras = []
        dic = dc.Dicionario()
        with open('//base/dicionario_paraense.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=':')

            lista_palavras = []
            for row in csv_reader:
                # print(len(row))
                try:
                    palavra = pa.Palavra(termo= row[0],traducao=row[1])
                    lista_palavras.append(palavra)
                except:
                    print("linha em branco")

            dic.lista_palavras = lista_palavras

            #dic.save()
        return dic


"""imp = ImportDicionario("Paraense")
db = imp.createDB("localhost", 27017)
dicionario = imp.fromCsv()
print(dicionario.save())
"""