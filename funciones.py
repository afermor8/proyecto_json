#Funciones proyecto_json

def listar_informacion(diccionario):
    listatitulos= []
    listatemporadas=[]
    listaepisodios=[]

    episodios=diccionario.get("_embedded").get("episodes")
    for episodio in episodios:
        listatitulos.append(episodio.get("name"))
        listatemporadas.append(episodio.get("season"))
        listaepisodios.append(episodio.get("number"))
    return listatitulos,listatemporadas,listaepisodios


def contar_informacion(diccionario):
    return len (diccionario.get("_embedded").get("episodes"))


def buscar_informacion(diccionario,titulo):
    episodios=diccionario.get("_embedded").get("episodes")
    for episodio in episodios:
        if titulo.lower()==episodio.get("name").lower():
            return episodio.get("summary")

