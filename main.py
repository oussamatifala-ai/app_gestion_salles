from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

# ajouter
s1 = Salle("S01", "Salle A", "Classe", 30)
dao.insert_salle(s1)
print("Salle ajoutée")

# rechercher
salle = dao.get_salle("S01")
if salle is not None:
    salle.afficher_infos()

# modifier
s2 = Salle("S01", "Salle A Modifiée", "Laboratoire", 40)
dao.update_salle(s2)
print("Salle modifiée")

# afficher toutes les salles
liste = dao.get_salles()
for s in liste:
    s.afficher_infos()
    print("-----")

# supprimer
dao.delete_salle("S01")
print("Salle supprimée")

from views.view_salle import ViewSalle

app = ViewSalle()
app.mainloop()
from views.view_salle import ViewSalle

app = ViewSalle()
app.mainloop()