from flask import Flask, jsonify, redirect, request, make_response, Response
import requests
import json
from modulos.usuarios import usuario
from modulos.view import view

app = Flask(__name__)
app.register_blueprint(usuario)
app.register_blueprint(view)

@app.route('/', methods=['GET'])
def index():

    headers = {"content-type":"application/json"}
    mensagem = {"mensagem": "api rest"}
    return make_response (json.dumps(mensagem), 301, headers)

    #return Response(json.dumps(mensagem))

@app.route('/', methods=['POST'])
def metodo_post():
    print(request.form['idade'])
    return redirect('/')

@app.route('/cep/<string:cep>')
def buscar_end(cep):
    re = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    return jsonify(re.json())

@app.route('/rota/<string:dinamico>')
def rota_dinamico(dinamico):
    return dinamico

if __name__ == "__main__":
    app.run()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000) 