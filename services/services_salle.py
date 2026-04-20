from Data.dao_salle import DataSalle

class ServiceSalle:

    def __init__(self):
        self.dao = DataSalle()

    def ajouter_salle(self, salle):
        exist = self.dao.get_salle(salle.code)

        if exist is not None:
            print("Erreur: salle déjà existe")
            return

        self.dao.insert_salle(salle)
        print("Salle ajoutée avec succès")

    def modifier_salle(self, salle):
        if salle.capacite <= 0:
            print("Erreur: capacité invalide")
            return

        self.dao.update_salle(salle)
        print("Salle modifiée")

    def supprimer_salle(self, code):
        self.dao.delete_salle(code)
        print("Salle supprimée")

    def rechercher_salle(self, code):
        return self.dao.get_salle(code)

    def recuperer_salles(self):
        return self.dao.get_salles()