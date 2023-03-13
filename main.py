from IntegranteB.animal import animal
from IntegranteB.cat import cat
import json
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
