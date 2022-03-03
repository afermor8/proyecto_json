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


def buscar_info_relacionada(diccionario,num):
    capitulos=[]
    urls=[]
    episodios=diccionario.get("_embedded").get("episodes")
    for episodio in episodios:
        if num<=episodio.get("rating").get("average"):
            capitulos.append(episodio.get("name"))
            urls.append(episodio.get("image").get("original"))
    return capitulos,urls
