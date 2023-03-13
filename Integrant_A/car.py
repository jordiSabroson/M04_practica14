class car:
    def __init__(self, model, portes, passatgers, quilometres, color):
        self.model = model
        self.portes = portes
        self.passatgers = passatgers
        self.quilometres = quilometres
        self.color = color

    def getModel(self):
        return self.model
    def setModel(self, model):
        self.model = model

    def getPortes(self):
        return self.portes
    def setPortes(self, portes):
        self.portes = portes

    def getPassatgers(self):
        return self.passatgers
    def setPassatgers(self, passatgers):
        self.passatgers = passatgers

    def getQuilometres(self):
        return self.quilometres
    def setQuilometres(self, quilometres):
        self.quilometres = quilometres

    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color

    def salutacio(self):
        print("Model de cotxe: "+self.model+"\nNúmero de portes: "+self.portes+"\nNúmero de passatgers: "+self.passatgers
              +"\nNúmero de quilòmetres: "+self.quilometres+"\nColor del cotxe: "+self.color+"\n")
        
    def to_dict(self):
        return {
            "model":self.model,
            "portes":self.portes,
            "passatgers":self.passatgers,
            "quilometres":self.quilometres,
            "color":self.color
        }

