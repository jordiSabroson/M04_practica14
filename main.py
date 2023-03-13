from IntegranteB.animal import animal
from IntegranteB.cat import cat
import json
from Integrant_A.car import car
from Integrant_A.book import book
#crea una llita per cada classe creada con 5 instàncies
cat = [
    cat("pepe", "negre", "10kg", "2 anys"),
    cat("tete", "blanca", "5kg", "1 anys"),
    cat("tadi", "naranja", "10kg", "3 mesos"),
    cat("pepi", "verde", "5kg", "10 mesos"),
    cat("lol","azul","7kg","1 anys")
]

animal = [
    animal("pepe", "cat", "negre", "10kg", "2 anys", "comer poco"),
    animal("tete", "perro", "blanca", "5kg", "1m esos", "comer mucho"),
    animal("tadi", "cocodrid", "naranja", "55kg", "3 anys", "comer mucho"),
    animal("pepi", "pez", "verde", "2kg", "1 anys", "comer poco"),
    animal("lol", "cerdo", "azul", "35kg", "1 anys", "comer mucho")
]

#convertir les instancies de les persones a una llista de diccionaris JSON
cat_liis = [c.to_dict() for c in cat]
animal_liis = [a.to_dict() for a in animal]
#Envolvemos las llistas dentro de un objeto contenedor
data = {"cat": cat_liis, "animal": animal_liis}
#Guardar l'objecte contenidor en un arxiu
with open("jsonAPI/b.json", 'w') as file:
    json.dump(data, file)



cotxes = [
    car("Ford Tourneo","5","7","700.000","blanc"),
    car("Crosta Car","3","9","100.000.000","marró"),
    car("Citroen Berlingo","7","5","0","negre"),
    car("Citroen Saxo","3","5","123","vermell"),
    car("Jeep 2","6","5","40.362","oliva")
 ]
llibres = [
     book("Les tres besones","infantil","1999","La Tere","19","tova"),
     book("Bricolaje para novatos","bricolatge","1966","Don José","5","de butxaca"),
     book("Guía telefónica Valladolid","guia","1780","Ayuntamiento de Valladolid","gratis","gegant"),
     book("Com sobreviure a un tsunami","supervivència","2012","John McJohn","60","dura"),
     book("LA BIBLIA","respostes","0","déu beneit","gratis","dura")
 ]

#Convertir les instàncies de les persones a una llista de diccionaris JSON
car_list = [k.to_dict() for k in cotxes]
book_list = [b.to_dict() for b in llibres]

#Guardem les llistes en un objecte contenidor en format diccionari
data = {"cotxes":car_list, "llibres":book_list}

#Guardar l'objecte contenidor en un arxiu en format .json
with open("jsonAPI/a.json", "w") as file:
    json.dump(data, file)
