import mongoengine
from pymongo import MongoClient
from model.palavra import Palavra

class Dicionario(mongoengine.Document):

    _id = mongoengine.SequenceField(required=True, primary_key=True)
    linguagem = mongoengine.StringField(default="Paraense")
    lista_palavras = mongoengine.ListField(mongoengine.EmbeddedDocumentField(Palavra), default=[Palavra(termo= "teste", traducao="teste traducao")])


mongoengine.connect('dicionario_db')