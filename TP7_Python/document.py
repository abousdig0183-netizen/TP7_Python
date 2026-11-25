
from datetime import datetime
import json


# Mixin 1 : Gestion de la date et heure
class Horodatable:
    def horodatage(self):
        date_actuelle = datetime.now()
        print(f"[LOG] Action à {date_actuelle}")
        return date_actuelle


# Mixin 2 : Validation
class Validable:
    def valider(self):
        if not getattr(self, "titre", None):
            raise ValueError("Titre manquant")

        if not getattr(self, "contenu", None):
            raise ValueError("Contenu manquant")

        print("Validation OK")


# Mixin 3 : Sérialisation JSON
class Serializable:
    def to_json(self):
        donnees = {
            "titre": self.titre,
            "contenu": self.contenu
        }
        return json.dumps(donnees, ensure_ascii=False)


# Mixin 4 : Historique des actions
class Historisable:
    def ajouter_action(self, action):
        self.historique.append({
            "action": action,
            "date": datetime.now().isoformat()
        })

    def afficher_historique(self):
        for element in self.historique:
            print(element)


# Classe principale
class Document(Horodatable, Validable, Serializable, Historisable):

    def __init__(self, titre, contenu):
        self.titre = titre
        self.contenu = contenu
        self.historique = []

    def sauvegarder(self):
        self.horodatage()
        self.valider()
        self.ajouter_action("Document sauvegardé")
        print(f"Document '{self.titre}' sauvegardé.")


if __name__ == "__main__":

    doc = Document("Rapport", "Contenu important")

    print("=== Sauvegarde ===")
    doc.sauvegarder()

    print("\n=== JSON ===")
    print(doc.to_json())

    print("\n=== Historique ===")
    doc.afficher_historique()
