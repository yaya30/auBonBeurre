# coding: utf-8

import socket
import threading
import json
import time
import datetime
from bdd import bddConnection
class ThreadForCLient(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn
    def run(self):
        data = self.conn.recv(4096)
        jsonFile = data.decode("utf8")
        print("jsonFile: ",jsonFile)
        jsonObject = json.loads(str(jsonFile))
        # Get unit_id in title
        unit_id = jsonObject['title'][11:12]
        print("unit_id is ", unit_id)
        print("le fichier à lire est : ", jsonObject['data'][0])
        # convert json to tuple
        db =  bddConnection()
        n=0
        for recording in jsonObject['data']:
            try:
                id_automate = db.selectIdAutomate(unit_id,jsonObject['data'][n]['numAutomate'])
                print("id_automate is:",id_automate[0][0])
                if(id_automate[0][0] is None):
                    n = n+1
                    continue
                date_unit=datetime.datetime.fromtimestamp(float(jsonObject['title'][13:len(jsonObject['title'])-5]))
                val = (
                    id_automate[0][0],
                    jsonObject['data'][n]['cuveTemp'],
                    jsonObject['data'][n]['outsideTemp'],
                    jsonObject['data'][n]['weightCuveMilk'],
                    jsonObject['data'][n]['weightFinalProduct'],
                    jsonObject['data'][n]['ph'],
                    jsonObject['data'][n]['kp'],
                    jsonObject['data'][n]['naCl'],
                    jsonObject['data'][n]['bactSalmo'],
                    jsonObject['data'][n]['bactEcoli'],
                    jsonObject['data'][n]['bactListeria'],
                    datetime.datetime.fromtimestamp(time.time()),
                    date_unit
                )
                db.insertFact(val)
                n = n+1
            except  NameError:
                print("iteration",n)
                print(NameError)    
        db.closeBdd()  
#----------------------------------------------------------
host, port = ('0.0.0.0',5566)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print("Le serveur est démarré")

while True:
    socket.listen(5)
    conn, address = socket.accept()
    print("Un client vient de se connecter...")

    my_thread = ThreadForCLient(conn)
    my_thread.start()

    
conn.close()
socket.close()