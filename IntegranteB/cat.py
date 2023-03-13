class cat:   #crea new class
    def __init__(self,name,color,peso,any): #Atributs del cat
        self.name = name
        self.color = color
        self.peso = peso
        self.any = any
    # Getters i Setters dels atributs del cat
    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name
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
    def to_dict(self):
        return {
            "name":self.name,
            "color":self.color,
            "peso":self.peso,
            "any":self.any,
        }
    # Mètode que retorna els atributs del animal
    def salutacio(self):
        print("El nom de aquesta animal es " + self.name)
        print("El color de aquesta animal es " + self.color)
        print("El peso de aquesta animal es " + self.peso)
        print("El edat de aquesta animal es " + self.any)



