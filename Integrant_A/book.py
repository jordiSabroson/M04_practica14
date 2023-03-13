class book:
    def __init__(self, titol, categoria, any, autor, preu, tapa): #Atributs del llibre
        self.titol = titol
        self.categoria = categoria
        self.any = any
        self.autor = autor
        self.preu = preu
        self.tapa = tapa

    # Getters i Setters dels atributs del llibre
    def getTitol(self):
        return self.titol
    def setTitol(self, titol):
        self.titol = titol

    def getCategoria(self):
        return self.categoria
    def setCategoria(self, categoria):
        self.categoria = categoria

    def getAny(self):
        return self.any
    def setAny(self, any):
        self.any = any

    def getAutor(self):
        return self.autor
    def setAutor(self, autor):
        self.autor = autor

    def getPreu(self):
        return self.preu
    def setPreu(self, preu):
        self.preu = preu

    def getTapa(self):
        return self.tapa
    def setTapa(self, tapa):
        self.tapa = tapa

    # Mètode que retorna els atributs del llibre
    def info(self):
        print("Títol: "+self.titol+"\nCategoria: "+self.categoria+"\nAny: "+self.any+"\nAutor: "+self.autor+"\nPreu: "+self.preu+"\nTapa: "+self.tapa+"\n")

    def to_dict(self):
        return {
            "titol":self.titol,
            "categoria":self.categoria,
            "any":self.any,
            "autor":self.autor,
            "preu":self.preu,
            "tapa":self.tapa
        }