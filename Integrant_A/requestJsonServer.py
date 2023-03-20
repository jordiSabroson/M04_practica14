import requests
# ----------- GET --------------
#Crear la consulta get de la api
responseCar = requests.get('http://localhost:3000/cotxes')
responseBook = requests.get('http://localhost:3000/llibres')

# Impressió objecte response
print(responseCar)
# Impressió contingut json
print(responseCar.json())

print(responseBook)
print(responseBook.json())

# ----------- POST -------------
# # Passar paràmetres a la URL
# parametresCar = {
#     'id': '6', 'model': 'Troncomovil', 'portes': '1', 'passatgers': '4', 'quilometres': '435', 'color': 'fusta'
# }
# # Afegir els paràmetres al JSON Server
# r = requests.post('http://localhost:3000/cotxes', data=parametresCar)
# print(r.text)
#
# parametresBook = {
#     'id': '6', 'titol': 'Pachis point', 'categoria': 'Acció', 'any': '1988', 'autor': 'Tio Manel', 'preu': '6,99', 'tapa': 'dura'
# }
# p = requests.post('http://localhost:3000/llibres', data=parametresBook)
# print(p.text)

# # -------------- DELETE -----------------
deleteCar = requests.delete('http://localhost:3000/cotxes/3')
deleteBook = requests.delete('http://localhost:3000/llibres/3')