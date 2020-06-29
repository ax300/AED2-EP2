class Person(object):

    def __init__(self, id):
        # Id Pess
        self.id = id
        # lista de Ids de pessoas adjacentes
        self.adjacentes = []

    def add_adjacentes(self, id):
        if (id not in self.adjacentes): #adiciona id dos frequentadores sem repetir
            self.adjacentes.append(id)