import sqlite3


class Banco:

    def conectar(self):

        conn = sqlite3.connect(
            "data/esg.db"
        )

        return conn