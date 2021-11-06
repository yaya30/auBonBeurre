# coding: utf-8

import socket
import threading
import json
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
        db =  bddConnection()
        db.insertTest()
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