from Person import Person
from Livre import Livre

class Auteur(Person):
    def __init__(self, firstname, lastname):
        Person.__init__(self, firstname, lastname)
        self.œuvre = []

    def ecrireUnLivre(self, titre):
        livre = Livre(titre)
        livre.auteur = self
        self.œuvre.append(livre)
        
    def listerOeuvre(self):
        for livre in self.œuvre:
            print(f"{livre.titre}")

    
