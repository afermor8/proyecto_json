#Programa principal

import json
from funciones import *


#Abrir fichero json
f=open("json_westworld.json")
westworld = json.load(f)
f.close()


#Listar títulos, la temporada a la que pertenece y el número de capítulo
titulos,temporadas,capitulos=listar_informacion(westworld)

print("\n   **Westworld**\n ----------------\n")
for titulo,temporada,capitulo in zip (titulos,temporadas,capitulos):
    print ("Temporada:",temporada,"- Capítulo:",capitulo,"-",titulo,"\n")


#Contar el total de episodios que tiene la serie
print(" ---------------\n   Total de capítulos de la serie:",contar_informacion(westworld),"\n ---------------")


#Pedir nombre de un episodio y mostrar sinopsis
episodiopedido=input("Dime el título de un episodio: ")
resultado=buscar_informacion(westworld,episodiopedido)
if not resultado:
    print ("ERROR. No existe información")
else:
    print ("Sinopsis:",resultado,"\n ---------------")
