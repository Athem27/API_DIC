import controller.import_dicionario as imp
import model.dicionario as model_dicionario
from flask import Flask, jsonify, request
#from controller.dicionario import dicionario
from controller import dicionario

app = Flask(__name__)
app.register_blueprint(dicionario.dicionario)

@app.route('/')
def index():
    return '<h1>Teste Valendo</h1><h3>API sobre Desenvolvedores!</h3><br><img src="https://thumbs.dreamstime.com/b/programador-de-software-for%C3%A7ado-com-o-escrit%C3%B3rio-do-computador-em-casa-82755034.jpg">', 200

 
if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()
