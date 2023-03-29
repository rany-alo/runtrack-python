from Person import Person
from Auteur import Auteur
from Livre import Livre

auteur1 = Auteur("Gabriel", "García Márquez")
auteur1.ecrireUnLivre("Cent Ans de solitude")
auteur1.ecrireUnLivre("L'Amour aux temps du choléra")
auteur1.sePresenter()
auteur1.listerOeuvre()
print("\n")
auteur2 = Auteur("Bill", "gates")
auteur2.ecrireUnLivre("How to Prevent the Next Pandemic")
auteur2.sePresenter()
auteur2.listerOeuvre()