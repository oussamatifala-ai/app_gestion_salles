import customtkinter as ctk
from tkinter import ttk
from services.services_salle import ServiceSalle
from models.salle import Salle


class ViewSalle(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("700x500")

        self.service = ServiceSalle()

        self.cadre_info = ctk.CTkFrame(self)
        self.cadre_info.pack(pady=10, padx=10)

        self.entry_code = ctk.CTkEntry(self.cadre_info, placeholder_text="Code", width=200)
        self.entry_code.grid(row=0, column=0, padx=10, pady=5)

        self.entry_libelle = ctk.CTkEntry(self.cadre_info, placeholder_text="Libellé", width=200)
        self.entry_libelle.grid(row=1, column=0, padx=10, pady=5)

        self.entry_type = ctk.CTkEntry(self.cadre_info, placeholder_text="Type", width=200)
        self.entry_type.grid(row=2, column=0, padx=10, pady=5)

        self.entry_capacite = ctk.CTkEntry(self.cadre_info, placeholder_text="Capacité", width=200)
        self.entry_capacite.grid(row=3, column=0, padx=10, pady=5)

        self.cadre_btn = ctk.CTkFrame(self)
        self.cadre_btn.pack(pady=10, padx=10)

        ctk.CTkButton(self.cadre_btn, text="Ajouter", command=self.ajouter_salle).grid(row=0, column=0, padx=5, pady=5)
        ctk.CTkButton(self.cadre_btn, text="Modifier", command=self.modifier_salle).grid(row=0, column=1, padx=5, pady=5)
        ctk.CTkButton(self.cadre_btn, text="Supprimer", command=self.supprimer_salle).grid(row=0, column=2, padx=5, pady=5)
        ctk.CTkButton(self.cadre_btn, text="Rechercher", command=self.rechercher_salle).grid(row=0, column=3, padx=5, pady=5)
        ctk.CTkButton(self.cadre_btn, text="Afficher", command=self.lister_salles).grid(row=0, column=4, padx=5, pady=5)

        self.cadre_list = ctk.CTkFrame(self)
        self.cadre_list.pack(pady=10, padx=10, fill="both", expand=True)

        self.treeList = ttk.Treeview(
            self.cadre_list,
            columns=("code", "libelle", "type", "capacite"),
            show="headings"
        )

        self.treeList.heading("code", text="CODE")
        self.treeList.heading("libelle", text="LIBELLE")
        self.treeList.heading("type", text="TYPE")
        self.treeList.heading("capacite", text="CAPACITE")

        self.treeList.column("code", width=100)
        self.treeList.column("libelle", width=180)
        self.treeList.column("type", width=150)
        self.treeList.column("capacite", width=100)

        self.treeList.pack(fill="both", expand=True, padx=10, pady=10)

        self.lister_salles()

    def vider_champs(self):
        self.entry_code.delete(0, "end")
        self.entry_libelle.delete(0, "end")
        self.entry_type.delete(0, "end")
        self.entry_capacite.delete(0, "end")

    from tkinter import messagebox

    def ajouter_salle(self):
        code = self.entry_code.get()
        libelle = self.entry_libelle.get()
        type_s = self.entry_type.get()

        try:
            capacite = int(self.entry_capacite.get())
        except:
            messagebox.showerror("Erreur", "Capacité invalide")
            return

        s = Salle(code, libelle, type_s, capacite)
        self.service.ajouter_salle(s)

        messagebox.showinfo("Succès", "Salle ajoutée")

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
        self.lister_salles()
        self.vider_champs()

    def supprimer_salle(self):
        code = self.entry_code.get()
        self.service.supprimer_salle(code)
        self.lister_salles()
        self.vider_champs()

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

    def lister_salles(self):
        for item in self.treeList.get_children():
            self.treeList.delete(item)

        liste = self.service.recuperer_salles()
        for s in liste:
            self.treeList.insert("", "end", values=(s.code, s.libelle, s.type, s.capacite))