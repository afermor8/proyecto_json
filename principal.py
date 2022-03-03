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
    print ("ERROR. No existe información.\n ---------------")
else:
    print ("Sinopsis:",resultado,"\n ---------------")


#Pedir puntuación entre 0 y 10 y mostrar títulos de los capítulos que tienen una puntuación superior o igual a la dada
#y la url de la imagen original de cada capítulo
puntuacion= float(input("Dime una puntuación entre 0 y 10 (puede ser un decimal): "))
while puntuacion <0 or puntuacion>10:
    print ("La puntuación debe ser entre 0 y 10 (puede ser un decimal).")
    puntuacion=float(input("Dime una puntuación entre 0 y 10:"))

titulos,urls=buscar_info_relacionada(westworld,puntuacion)

if not titulos and not urls:
    print ("ERROR. No hay capítulos con una puntuación mayor a la dada.")
else:
    print ("\n**Capítulos con puntuación igual o superior:**")
    for titulo,url in zip (titulos,urls):
        print ("  --Título:",titulo,"\n    Imagen:",url,"\n")
print(" ---------------")

