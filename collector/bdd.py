import mariadb
import sys

class bddConnection():
    conn= None
    def __init__(self):
            self.conn = self.runConnect()
    def runConnect(self):
        try:
            conn = mariadb.connect(
                user="root",
                password="root",
                host="localhost",
                port=3309,
                database="Unites"
                )
            print("dans runConnect",conn)
            return conn
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            return "error"
    def insertTest(self):
        print("dans insertTest:",self.conn)
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO Unites (id, unit_id, num_automate, type_auto) VALUES (1, 1,1,new)")

    def closeBdd(self):
        self.conn.close()
            


