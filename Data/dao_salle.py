import json
import mysql.connector
from models.salle import Salle


class DataSalle:
    def get_connection(self):
        with open("Data/config.json", "r", encoding="utf-8") as f:
            config = json.load(f)

        con = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        return con

    def insert_salle(self, salle):
        con = self.get_connection()
        cursor = con.cursor()

        try:
            req = "INSERT INTO salle (code, libelle, type, capacite) VALUES (%s, %s, %s, %s)"
            val = (salle.code, salle.libelle, salle.type, salle.capacite)

            cursor.execute(req, val)
            con.commit()
        finally:
            cursor.close()
            con.close()

    def update_salle(self, salle):
        con = self.get_connection()
        cursor = con.cursor()

        req = "UPDATE salle SET libelle=%s, type=%s, capacite=%s WHERE code=%s"
        val = (salle.libelle, salle.type, salle.capacite, salle.code)

        cursor.execute(req, val)
        con.commit()

        cursor.close()
        con.close()

    def delete_salle(self, code):
        con = self.get_connection()
        cursor = con.cursor()

        req = "DELETE FROM salle WHERE code=%s"
        val = (code,)

        cursor.execute(req, val)
        con.commit()

        cursor.close()
        con.close()

    def get_salle(self, code):
        con = self.get_connection()
        cursor = con.cursor()

        req = "SELECT * FROM salle WHERE code=%s"
        val = (code,)

        cursor.execute(req, val)
        result = cursor.fetchone()

        cursor.close()
        con.close()

        if result is not None:
            return Salle(result[0], result[1], result[2], result[3])
        return None

    def get_salles(self):
        con = self.get_connection()
        cursor = con.cursor()

        req = "SELECT * FROM salle"
        cursor.execute(req)

        results = cursor.fetchall()

        cursor.close()
        con.close()

        liste_salles = []
        for r in results:
            s = Salle(r[0], r[1], r[2], r[3])
            liste_salles.append(s)

        return liste_salles