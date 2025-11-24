from FilaFilmes import FilaFilmes
import json

from PesquisaFilme import pesquisa_filme

def gerencia_filmes(catalogo: FilaFilmes):
    filme = FilaFilmes.get()
    arquivo = open('baseDadosFilmes.json', 'r', encoding='utf-8')
    dados = json.load(arquivo)
    arquivo.close()
    for filme in dados:
        try:
            existe = pesquisa_filme(filme['titulo'], catalogo)
            if existe is None:
                catalogo.adicionar_filme(filme['titulo'], filme['generos'], filme['ano'], filme['diretor'])
        except Exception as e:
            print(f"Erro ao adicionar filme {filme['titulo']}: {e}")

def recomenda_filmes(catalogo: FilaFilmes, genero: str, quantidade: int):
    recomendados = []
    for filme in catalogo.filmes:
        if genero.lower() in [g.lower() for g in filme.generos]:
            recomendados.append(filme)
        if len(recomendados) == quantidade:
            break
    return recomendados