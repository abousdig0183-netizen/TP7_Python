
from datetime import datetime
import copy


# Mixin 1 : Validation du titre
class ValidationMixin:

    def valider(self):
        if not self.titre or not self.titre.strip():
            raise ValueError("Le titre est obligatoire.")

        return True


# Mixin 2 : Gestion de l'historique
class HistoriqueMixin:

    def __init__(self):
        self.historique = []

    def enregistrer_historique(self):
        ancienne_version = copy.deepcopy(self.description)
        self.historique.append(ancienne_version)

    def afficher_historique(self):
        print("=== Historique des modifications ===")

        for i, description in enumerate(self.historique, start=1):
            print(f"Version {i} : {description}")


# Mixin 3 : Journalisation
class JournalisationMixin:

    def journaliser(self, action):
        date_actuelle = datetime.now()
        print(f"[Journal] {date_actuelle} : {action}")


# Classe principale
class Tache(ValidationMixin, HistoriqueMixin, JournalisationMixin):

    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.date_creation = datetime.now()

        self.historique = []

        self.valider()
        self.journaliser(f"Création de la tâche '{self.titre}'")

    def mettre_a_jour(self, description):
        self.valider()

        self.enregistrer_historique()

        self.description = description

        self.journaliser(f"Modification de la tâche '{self.titre}'")

    def afficher(self):
        print(f"Titre : {self.titre}")
        print(f"Description : {self.description}")
        print(f"Date de création : {self.date_creation}")


# Programme principal
if __name__ == "__main__":

    tache = Tache("Projet Python", "Préparer le TP")

    print("\n=== Première modification ===")
    tache.mettre_a_jour("Créer les classes Python")

    print("\n=== Deuxième modification ===")
    tache.mettre_a_jour("Tester les mixins")

    print("\n=== Informations de la tâche ===")
    tache.afficher()

    print("\n=== Historique ===")
    tache.afficher_historique()
