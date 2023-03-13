class animal:   #crea new class
    def __init__(self,name,tipo,color,peso,any,other): #Atributs del animal
        self.name = name
        self.tipo = tipo
        self.color = color
        self.peso = peso
        self.any = any
        self.other = other
    # Getters i Setters dels atributs del animal
    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name
    def getTipo(self):
        return self.tipo
    def setTipo(self,tipo):
        self.tipo = tipo
    def getColor(self):
        return self.color
    def setColor(self,color):
        self.color = color
    def getPeso(self):
        return self.peso
    def setPeso(self,peso):
        self.peso = peso
    def getAny(self):
        return self.any
    def setAny(self,any):
        self.any = any
    def getOther(self):
        return self.other
    def setOther(self,other):
        self.other = other
    def to_dict(self):
        return {
            "name":self.name,
            "tipo":self.tipo,
            "color":self.color,
            "peso":self.peso,
            "any":self.any,
            "other":self.other
        }
    # Mètode que retorna els atributs del animal
    def salutacio(self):
        print("El nom de aquesta animal es " + self.name)
        print("El tipo de aquesta animal es " + self.tipo)
        print("El color de aquesta animal es " + self.color)
        print("El peso de aquesta animal es " + self.peso)
        print("El edat de aquesta animal es " + self.any)
        print("El otra informacio de aquesta animal es " + self.other)

