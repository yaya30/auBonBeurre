# coding: utf-8
import os
import socket
import unit
import json


num_unit = 1
data , epochTime = unit.auto()
path = "./data/"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

print(type(epochTime))
title = 'paramunite_' + str(num_unit)+ "_"+ str(epochTime) +'.json'
print(type(data))
data_addTitle = {**data , 'title' : title}
cwd = os.getcwd()
print("cwd:",cwd)
with open(path+title,'w') as outfile:
    outfile.write(json.dumps(data_addTitle))
filesize = os.path.getsize(path+title)
print("filesize: ",filesize)
host, port = ("172.168.1.2", 5566)
print("host : ",host)
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    socket.connect((host, port))
    print("Client connecté")
    dataSend = json.dumps(data_addTitle).encode("utf8")
    socket.sendall(dataSend)
except ConnectionRefusedError:
    print("Connexion au serveur échoué !")
finally:
    socket.close()
