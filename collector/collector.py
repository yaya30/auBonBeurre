# coding: utf-8

import socket
import threading
import json
class ThreadForCLient(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn
    def run(self):
        data = self.conn.recv(1024)
        title = data.decode("utf8")
        # Get unit_id in title
        unit_id = title[11:12]
        print("unit_id is ", unit_id)
        with open("./data/"+title,'r') as jsonFile:
            jsonObject = json.load(jsonFile)
            jsonOther = jsonFile
            jsonFile.close()
        
        print("le fichier à lire est : ", jsonObject['data'][0])
#----------------------------------------------------------
host, port = (socket.gethostbyname('reseauProduct'),5566)

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