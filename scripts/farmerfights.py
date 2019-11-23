# coding: utf8

import random
from datetime import datetime
import APILeekwars as API
import getpass
import os

os.makedirs("{}/logs/farmerfights".format(os.getcwd()), exist_ok=True)

api = API.APILeekwars()
farmer_name = input('Login: ')
password = getpass.getpass(prompt='Password: ')
r = api.farmer.login_token(farmer_name, password)
if r and 'token' in r:
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
    if nbfights == 0:
        print("Pas de combats disponibles, réessayez demain.")
    else:
        print("Vous avez {} combats restants.".format(nbfights))
        nbfightsWntd = int(input("Veuillez choisir le nombre de combats que vous souhaitez lancer : "))
        i = 0
        file = open("logs/farmerfights_{}.txt".format(datetime.now().strftime('%d-%m-%Y_%H:%M:%S')),"w")
        file.write("L'éleveur {} a été choisi pour {} combats : {}\n".format(farmer, nbfightsWntd))
        while i < nbfightsWntd:
            r = api.garden.get_farmer_opponents(token)
            if r and 'opponents' in r:
                print("Eleveurs correctement chargés. Choix aléatoire de l'éleveur en cours...")
                random.seed()
                opponent = random.choice(r["opponents"])["id"]
                r = api.garden.start_farmer_fight(opponent, token)
                if r and 'fight' in r:
                    file.write("https://leekwars.com/fight/{}\n".format(r["fight"]))
                    print("https://leekwars.com/fight/{}".format(r["fight"]))
                    print(datetime.now().strftime('%H-%M-%S'))
                else:
                    print("Erreur lors du lancement du combat")
            else:
                print("Erreur lors de l'affichage des éleveurs")
            i += 1
    r = api.farmer.disconnect(token)
else:
    print("Erreur lors de la connexion de l'éleveur. Vérifiez vos identifiants.")
