import mariadb
import sys

class bddConnection():
    conn= None
    def __init__(self):
            self.conn = self.runConnect()
    def runConnect(self):
        try:
            conn = mariadb.connect(
                user="first",
                password="first",
                host="mariadb",
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
            "INSERT INTO fact_automate (id, unit_id, num_automate, type_auto) VALUES (1, 1,1,new)")
    def selectIdAutomate(self,unit_id,num_automate):
        cur = self.conn.cursor()
        cur.execute(
            "select id from automate where unit_id=%s and num_automate=%s",
            (unit_id,num_automate)
        )
        return cur.fetchall()
    def insertFact(self,val):
        cur = self.conn.cursor()
        query = """Insert INTO fact_automate (
            automate_id,cuveTemp,outsideTemp,
            cuveMilkWeigth,finalProductWeight,
            ph,kp,naCl,bactSalmo,bactEcoli,
            bactListeria,date_bdd,date_unit
        ) 
        VALUES 
        (?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        try:
            print("insert recording",val)
            cur.execute(query,val)
            self.conn.commit()
        except mariadb.Error as e:
            print(f"Error: {e}")
        
    def closeBdd(self):
        self.conn.close()
            


