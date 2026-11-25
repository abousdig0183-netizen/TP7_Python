
import json
import csv
from datetime import datetime


# Mixin 1 : Sérialisation JSON
class Serializable:

    def to_json(self):
        donnees = {
            "id": self.id,
            "description": self.description
        }
        return json.dumps(donnees, ensure_ascii=False)

    @classmethod
    def from_json(cls, json_str):
        donnees = json.loads(json_str)
        return cls(**donnees)


# Mixin 2 : Historique des modifications
class Historisable:

    def __init__(self):
        self.historique = []

    def enregistrer_etat(self):
        etat = {
            "id": self.id,
            "description": self.description,
            "date": datetime.now().isoformat()
        }
        self.historique.append(etat)


# Mixin 3 : Journalisation
class Journalisable:

    def journaliser(self, message):
        print(f"[Journal] {datetime.now()}: {message}")


# Mixin 4 : Horodatage
class Horodatable:

    def horodatage(self):
        return datetime.now()


# Classe principale
class Contrat(Serializable, Historisable, Journalisable, Horodatable):

    def __init__(self, id, description):
        Historisable.__init__(self)
        self.id = id
        self.description = description

    def modifier(self, nouvelle_desc):
        self.journaliser(f"Modification du contrat {self.id}")

        self.enregistrer_etat()

        date_modification = self.horodatage()
        self.description = nouvelle_desc

        print(f"Modification effectuée à {date_modification}")


# Programme principal
if __name__ == "__main__":

    contrat = Contrat(1, "Initial")

    print("=== Modification ===")
    contrat.modifier("Révisé")

    print("\n=== JSON ===")
    donnees_json = contrat.to_json()
    print(donnees_json)

    print("\n=== Restauration depuis JSON ===")
    contrat2 = Contrat.from_json(donnees_json)
    print(contrat2.id, contrat2.description)

    print("\n=== Historique ===")
    for etat in contrat.historique:
        print(etat)
