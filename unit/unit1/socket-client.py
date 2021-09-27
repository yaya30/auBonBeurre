# coding: utf-8
import os
import socket
import unit

num_unit = 1
data , epochTime = unit.auto()
print(type(epochTime))
title = 'paramunite_' + str(num_unit)+ "_"+ str(epochTime) +'.json'
cwd = os.getcwd()
print("cwd:",cwd)
with open("./data/"+title,'w') as outfile:
    outfile.write(data)
host, port = (socket.gethostbyname('reseauProduct'), 5566)
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    socket.connect((host, port))
    print("Client connecté")
    data = title.encode("utf8")
    socket.sendall(data)
except ConnectionRefusedError:
    print("Connexion au serveur échoué !")
finally:
    socket.close()
