from Data.dao_salle import DataSalle


class ServiceSalle:
    def __init__(self):
        self.dao = DataSalle()

    def ajouter_salle(self, salle):
        if not salle.code or not salle.libelle or not salle.type:
            print("Erreur: champs vides")
            return

        if salle.capacite < 1:
            print("Erreur: capacité invalide")
            return

        exist = self.dao.get_salle(salle.code)
        if exist is not None:
            print("Erreur: salle déjà existe")
            return

        self.dao.insert_salle(salle)
        print("Salle ajoutée avec succès")

    def modifier_salle(self, salle):
        if not salle.code or not salle.libelle or not salle.type:
            print("Erreur: champs vides")
            return

        if salle.capacite < 1:
            print("Erreur: capacité invalide")
            return

        exist = self.dao.get_salle(salle.code)
        if exist is None:
            print("Erreur: salle non trouvée")
            return

        self.dao.update_salle(salle)
        print("Salle modifiée avec succès")

    def supprimer_salle(self, code):
        if not code:
            print("Erreur: code vide")
            return

        exist = self.dao.get_salle(code)
        if exist is None:
            print("Erreur: salle non trouvée")
            return

        self.dao.delete_salle(code)
        print("Salle supprimée avec succès")

    def rechercher_salle(self, code):
        if not code:
            print("Erreur: code vide")
            return None

        return self.dao.get_salle(code)

    def recuperer_salles(self):
        return self.dao.get_salles()