import customtkinter as ctk
from services.services_salle import ServiceSalle
from models.salle import Salle


class ViewSalle(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("400x500")

        self.service = ServiceSalle()

        # Inputs
        self.entry_code = ctk.CTkEntry(self, placeholder_text="Code")
        self.entry_code.pack(pady=5)

        self.entry_libelle = ctk.CTkEntry(self, placeholder_text="Libellé")
        self.entry_libelle.pack(pady=5)

        self.entry_type = ctk.CTkEntry(self, placeholder_text="Type")
        self.entry_type.pack(pady=5)

        self.entry_capacite = ctk.CTkEntry(self, placeholder_text="Capacité")
        self.entry_capacite.pack(pady=5)

        # Buttons
        btn_add = ctk.CTkButton(self, text="Ajouter", command=self.ajouter_salle)
        btn_add.pack(pady=5)

        btn_show = ctk.CTkButton(self, text="Afficher", command=self.afficher_salles)
        btn_show.pack(pady=5)

        btn_update = ctk.CTkButton(self, text="Modifier", command=self.modifier_salle)
        btn_update.pack(pady=5)

        btn_delete = ctk.CTkButton(self, text="Supprimer", command=self.supprimer_salle)
        btn_delete.pack(pady=5)

        btn_search = ctk.CTkButton(self, text="Rechercher", command=self.rechercher_salle)
        btn_search.pack(pady=5)

    def ajouter_salle(self):
        code = self.entry_code.get()
        libelle = self.entry_libelle.get()
        type_s = self.entry_type.get()

        try:
            capacite = int(self.entry_capacite.get())
        except:
            print("Capacité invalide")
            return

        s = Salle(code, libelle, type_s, capacite)
        self.service.ajouter_salle(s)

    def afficher_salles(self):
        liste = self.service.recuperer_salles()
        for s in liste:
            s.afficher_infos()
            print("------")

    def modifier_salle(self):
        code = self.entry_code.get()
        libelle = self.entry_libelle.get()
        type_s = self.entry_type.get()

        try:
            capacite = int(self.entry_capacite.get())
        except:
            print("Capacité invalide")
            return

        s = Salle(code, libelle, type_s, capacite)
        self.service.modifier_salle(s)

    def supprimer_salle(self):
        code = self.entry_code.get()
        self.service.supprimer_salle(code)

    def rechercher_salle(self):
        code = self.entry_code.get()
        s = self.service.rechercher_salle(code)

        if s is not None:
            self.entry_libelle.delete(0, "end")
            self.entry_libelle.insert(0, s.libelle)

            self.entry_type.delete(0, "end")
            self.entry_type.insert(0, s.type)

            self.entry_capacite.delete(0, "end")
            self.entry_capacite.insert(0, str(s.capacite))
        else:
            print("Salle non trouvée")