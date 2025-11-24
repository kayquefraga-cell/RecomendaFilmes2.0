from FilaFilmes import FilaFilmes

def pesquisa_filme(titulo, fila_filmes: FilaFilmes):
    for filme in fila_filmes.filmes:
        if filme.titulo.lower() == titulo.lower():
            return filme
    return None