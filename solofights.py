# coding: utf8

import random
from datetime import datetime
import APILeekwars as API
import getpass
import os

os.makedirs("{}/logs".format(os.getcwd()), exist_ok=True)

api = API.APILeekwars()
farmer_name = input('Login: ')
password = getpass.getpass(prompt='Password: ')
r = api.farmer.login_token(farmer_name, password)
if r["success"]:
    token = r["token"]
    farmer = r["farmer"]
    login = farmer["name"]
    victories = farmer["victories"]
    draws = farmer["draws"]
    defeats = farmer["defeats"]
    ratio = farmer["ratio"]
    nbfights = farmer["fights"]
    money = farmer["habs"]
    print("Connexion réussie ! \nNom d'utilisateur : {}    Habs actuels :  {}\n{} Victoires         {} Nuls         {} Défaites \n{} de ratio.".format(login, money, victories, draws, defeats, ratio))
    leeks = sorted(farmer["leeks"].values(), key=lambda l: l['id'])
    print('\n'.join('Poireau {} : {}'.format(i, l['name']) for i, l in enumerate(leeks, 1)))
    if nbfights == 0:
        print("Pas de combats disponibles, réessayez demain.")
    else:
        print("Vous avez {} combats restants.".format(nbfights))
        nbfightsWntd = int(input("Veuillez choisir le nombre de combats que vous souhaitez lancer : "))
        leekchosen = int(input("Veuillez choisir le numéro correspondant au poireau qui doit se battre : "))
        leek = leeks[leekchosen-1]
        print(leek)
        i = 0
        file = open("logs/solofights_{}.txt".format(datetime.now().strftime('%d-%m-%Y_%H:%M:%S')),"w")
        file.write("Poireau choisi pour {} combats : {}\n".format(nbfightsWntd, leek["name"]))
        while i < nbfightsWntd:
            r = api.garden.get_leek_opponents(leek["id"], token)
            if r["success"]:
                print("Adversaires correctement chargés. Choix aléatoire de l'adversaire en cours...")
                random.seed()
                opponent = random.choice(r["opponents"])["id"]
                r = api.garden.start_solo_fight(leek["id"], opponent, token)
                if r["success"]:
                    file.write("https://leekwars.com/fight/{}\n".format(r["fight"]))
                    print("https://leekwars.com/fight/{}".format(r["fight"]))
                    print(datetime.now().strftime('%H-%M-%S'))
                else:
                    print("Erreur lors du lancement du combat")
            else:
                print("Erreur lors de l'affichage des adversaires")
            i += 1
    r = api.farmer.disconnect(token)
else:
    print("Erreur lors de la connexion du fermier. Vérifiez vos identifiants.")
