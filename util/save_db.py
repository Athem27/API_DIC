from model import dicionario as model
from pymongo import MongoClient
import controller.import_dicionario as imp

from flask import Blueprint, request, jsonify
db = MongoClient('mongodb://localhost:27017')
collection = db.avaliacao_db.indicadores #COLLECTION CALLED DEVELOPERS

indicadores = Blueprint('dicionario_db', __name__)

class excel_import(object):

    def __init__(self):
        self.name = "excel_import"

    def createDB(self, host, port):
      client = MongoClient(host, port) #localhost", 27017
      database = client["avaliacao_db"]
      list_of_db = client.list_database_names()
      if "avaliacao_db" in list_of_db:
        print("O Banco de Dados já existe.")
      else:
        print("Criando o Banco de Dados  avaliacao_db")

      return database

    def importExcel_V2(self, path, sheet):
        data_df = pandas.read_excel(path, sheet_name=sheet)
        colunas = data_df.columns
        situacao_value = None
        print(data_df.columns)
        print(data_df.shape)

        excel_data_df = data_df.fillna("")
        erros = []
        for row in range(excel_data_df.shape[0]):
            ind = model.Indicadores()
            print(excel_data_df['UNIDADE RESPONSÁVEL'][row])
            print(excel_data_df['ENTREGA'][row])
            try:
                ind.unidade_responsavel = excel_data_df['UNIDADE RESPONSÁVEL'][row]
                ind.produto = excel_data_df['PRODUTO'][row] if excel_data_df['PRODUTO'][row] != "NaN" else ""
                ind.tipologia = excel_data_df['TIPOLOGIA'][row] if excel_data_df['TIPOLOGIA'][row] != "NaN" else ""

                print(type(excel_data_df['ENTREGA'][row]))
                if(type(excel_data_df['ENTREGA'][row]) is np.int64):
                    print("é inteiro")
                    ind.meta_entrega = str(excel_data_df['ENTREGA'][row]) if str(excel_data_df['ENTREGA'][row]) != "NaN" else ""
                else:
                    ind.meta_entrega = excel_data_df['ENTREGA'][row] if excel_data_df['ENTREGA'][row] != "NaN" else ""

                if (excel_data_df['SITUAÇÃO'][row] == "NaN" or excel_data_df['SITUAÇÃO'][row] == ""):

                    situacao_value = "Em branco"
                else:
                    situacao_value = excel_data_df['SITUAÇÃO'][row]

                print("Situação: ", situacao_value)
                prog = model.Progresso(situacao= situacao_value, status= float(excel_data_df['CONCLUSÃO EM PORCENTAGEM'][row])*100 if (excel_data_df['CONCLUSÃO EM PORCENTAGEM'][row] != "") else 0, data_salvo = None)

                ind.progresso = [prog]
                ind.diretoria_responsavel = excel_data_df['DIRETORIA RESPONSÁVEL'][row] if excel_data_df['DIRETORIA RESPONSÁVEL'][row] != "NaN" else ""
                ind.coordenacao_responsavel = excel_data_df['COORDENAÇÃO RESPONSÁVEL'][row] if excel_data_df['COORDENAÇÃO RESPONSÁVEL'][row] != "NaN" else ""
                ind.unidade_administrativa_parceira = excel_data_df['UNIDADE ADMINISTRATIVA PARCEIRA'][row] if excel_data_df['UNIDADE ADMINISTRATIVA PARCEIRA'][row] != "NaN" else ""
                ind.unidade_academica_parceira = excel_data_df['UNIDADE ACADÊMICA PARCEIRA'][row] if excel_data_df['UNIDADE ACADÊMICA PARCEIRA'][row] != "NaN" else ""
                ind.onde_verifica = excel_data_df['ONDE VERIFICAR'][row] if excel_data_df['ONDE VERIFICAR'][row] != "NaN" else "teste"
                #print(ind.to_json())

                ind.save()
            except Exception as e:
                #print(excel_data_df.loc[row])
                print(type(excel_data_df['ONDE VERIFICAR'][row]))
                print(e)
                print("--------------------------------")
                erros.append(e)


        return erros

if __name__ == '__main__':
    ex = excel_import()
    db = ex.createDB("localhost", 27017)
    xls = pandas.ExcelFile('../base/Acompanhamento 100 dias.xlsx')
    print(xls.sheet_names)
    for sheet in xls.sheet_names:

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("Sheet -> ", sheet)
        file_json = ex.importExcel_V2("../base/Acompanhamento 100 dias.xlsx", sheet)
        print(file_json)

