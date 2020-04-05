#Petit programme calculant les premières et dernières adresses de chaque plage d'un réseau

from Plage import Plage
from Network import  Network
import json
network = Network()
start = network.get_start()
data = {}
data[network.get_name()] = []
data[network.get_name()].append(network.send_to_json())
t = int(input("Combien de plages voulez-vous ?"))
plages_dict = dict()
plages_list = []


for i in range(t):
    if i == 0:
        c = input("Entrez un nom pour la 1ère plage : ").lower()
        plages_dict[c] = int(input("Combien d'adresses voulez-vous dans cette plage : "))
        plages_list.append(Plage(c, plages_dict[c],start))
        data[plages_list[i].get_name()] = []
        data[plages_list[i].get_name()].append(plages_list[i].send_to_json())

    else:
        c = input("Entrez un nom pour la {}ème plage : ".format(i+1)).lower()
        plages_dict[c] = int(input("Combien d'adresses voulez-vous dans cette plage : ".format(i+1)))
        start = plages_list[i-1].get_end()
        start[2], start[3] = start[2]+1, 0
        plages_list.append(Plage(c,plages_dict[c],start))
        data[plages_list[i].get_name()] = []
        data[plages_list[i].get_name()].append(plages_list[i].send_to_json())

print(data)
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile, indent=4)

