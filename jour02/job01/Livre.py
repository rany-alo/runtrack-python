class Livre:
    def __init__(self, titre):
        self.titre = titre
        self.auteur = None

    def get_titre(self):
        return self.titre
    
    def set_titre(self, new_titre):
        self.titre = new_titre
    
    def get_auteur(self):
        return self.auteur
    
    def set_auteur(self, new_auteur):
        self.auteur = new_auteur
        new_auteur.livre = self

    def print(self):
        print(f"Le titre du livre est : {self.get_titre}")