import json
import mysql.connector

class DataSalle:
    def get_connection(self):
        with open("Data/config.json", "r") as f:
            config = json.load(f)

        con = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )

        return con