from flask import Flask, request, jsonify
from tinydb import TinyDB, Query
from FilaFilmes import filaFilmes

app = Flask(__name__)

@app.route('/api/pesquisaFilme', methods=['POST'])
def pesquisa_filme():
    if not request.is_json:
        return {"erro": "Requisição deve ser em JSON"}, 400

    dados = request.get_json()
    titulo = dados.get("titulo")

    db = TinyDB('baseDadosFilmes.json')
    filmes = db.table('filmes')
    Filmes = Query()

    resultado = filmes.search(Filmes.titulo == titulo)

    resposta = {
        "mensagem": "Pesquisa realizada",
        "titulo_pesquisado": titulo,
        "filme_encontrado": resultado,
        "total_filmes": filmes.all()
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