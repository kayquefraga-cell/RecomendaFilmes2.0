from flask import Flask, request, jsonify
from tinydb import TinyDB, Query
from FilaFilmes import filaFilmes

app = Flask(__name__)

@app.route('/api/pesquisaFilme', methods=['POST'])
def pesquisa_filme():
    if not request.is_json:
        return jsonify({"erro": "Requisição deve ser em JSON"}), 400

    dados = request.get_json()

    db = TinyDB('baseDadosFilmes.json')
    Filmes = db.table('Filmes')
    
    Filmes.insert(dados)

   # todos = Filmes.all()

    filmes_query = dados.get('filme', '')
    print(filmes_query)
    Filmes = Query()

    resultado = db.search(Filmes.nome == filmes_query)
    resposta = {
        "mensagem": "Pesquisa realizada",
        "titulo_pesquisado": dados,
        "filme_encontrado": resultado,
       # "total_filmes": todos
    }

    return jsonify(resposta), 200


@app.route('/api/recomendarFilme', methods=['POST'])
def recomendar_filme():
    if not request.is_json:
        return {"erro": "Requisição deve ser em JSON"}, 400
    
    dados = request.get_json()
    filaFilmes.put(dados)
    
    resposta = {
        "mensagem": "Filme adicionado à fila de recomendações",
        "dados_recebidos": dados
    }

    return jsonify(resposta), 200


if __name__ == '__main__':
    app.run(debug=True)