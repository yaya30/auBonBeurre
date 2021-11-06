import random as rd
import time
import json
def generateAuto(x):
    automate = {
    'numAutomate' : x+1,
    'cuveTemp' : round(rd.uniform(2.5,4),1),
    'outsideTemp' : round(rd.uniform(8,14),1),
    'weightCuveMilk' : round(rd.uniform(8,14),1),
    'weightFinalProduct' : rd.randint(3512,4607),
    'ph' : round(rd.uniform(6.8,7.2),1),
    'kp' : rd.randint(35,47),
    'naCl' : round(rd.uniform(1,1.7),1),
    'bactSalmo' : rd.randint(17,37),
    'bactEcoli' : rd.randint(35,49),
    'bactListeria' : rd.randint(28,54)
    }
    return automate
def auto() : 
    gen=(generateAuto(x) for x in range(10))
    return {'data':list(gen)} , time.time()






