#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title           :menu.py
#description     :This program displays an interactive menu
#version         :1.0
#usage           :python menu.py
#python_version  :3.6.1  
#=======================================================================
 
# Import the modules needed to run the script.
import sys, os
import random
from datetime import datetime
import APILeekwars as API
import getpass
import os
 

# Main definition - constants
menu_actions  = {}  
global token
global farmer
global nbfights
global login
global victories
global draws
global defeats
global ratio
global money 
# =======================
#     MENUS FUNCTIONS
# =======================
 
# Main menu
def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=====================================================================")
    print("                        INFORMATIONS COMPTE                          ")
    print("=====================================================================")
    print("\nNom d'utilisateur : {}    Habs actuels :  {}\n\n{} Victoires         {} Nuls         {} Défaites \nRatio : {} ".format(login, money, victories, draws, defeats, ratio))
    print("Veuillez choisir le menu que vous souhaitez utiliser :")
    print ("\n1. Combats Solo")
    print ("2. Combats d'Eleveurs")
    print ("3. Combats d'Equipe")
    print ("4. Inscription tournois")
    print ("\n0. Quitter")
    choice = input(" >>  ")
    exec_menu(choice)
    return
 
# Execute menu
def exec_menu(choice):
    os.system('cls' if os.name == 'nt' else 'clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print ("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return
 
# Menu 1
def menu1():
    print("=====================================================================")
    print("                        INFORMATIONS COMPTE                          ")
    print("=====================================================================")
    print("\nNom d'utilisateur : {}    Habs actuels :  {}\n\n{} Victoires         {} Nuls         {} Défaites \nRatio : {} \n".format(login, money, victories, draws, defeats, ratio))
    print("=====================================================================")
    print("                           COMBATS SOLO                              ")
    print("=====================================================================\n")
    leeks = sorted(farmer["leeks"].values(), key=lambda l: l['id'])
    print('\n'.join('Poireau {} : {}'.format(i, l['name']) for i, l in enumerate(leeks, 1)))
    if nbfights == 0:
        print("\nPas de combats disponibles, réessayez demain.")
    else:
        print("Vous avez {} combats restants.".format(nbfights))
        nbfightsWntd = int(input("Veuillez choisir le nombre de combats que vous souhaitez lancer : "))
        leekchosen = int(input("Veuillez choisir le numéro correspondant au poireau qui doit se battre : "))
        leek = leeks[leekchosen-1]
        i = 0
        file = open("logs/solofights/solofights_{}.txt".format(datetime.now().strftime('%d-%m-%Y_%H-%M-%S')),"w")
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
                else:
                    print("Erreur lors du lancement du combat")
            else:
                print("Erreur lors de l'affichage des adversaires")
            i += 1
    print ("\n9. Retour")
    print ("0. Quitter")
    choice = input(" >>  ")
    exec_menu(choice)
    return
 
# Menu 2
def menu2():
    print("=====================================================================")
    print("                        INFORMATIONS COMPTE                          ")
    print("=====================================================================")
    print("\nNom d'utilisateur : {}    Habs actuels :  {}\n\n{} Victoires         {} Nuls         {} Défaites \nRatio : {} \n".format(login, money, victories, draws, defeats, ratio))
    print("=====================================================================")
    print("                         COMBATS ELEVEURS                            ")
    print("=====================================================================\n")
    if nbfights == 0:
        print("Pas de combats disponibles, réessayez demain.")
    else:
        print("Vous avez {} combats restants.".format(nbfights))
        nbfightsWntd = int(input("Veuillez choisir le nombre de combats que vous souhaitez lancer : "))
        i = 0
        file = open("logs/farmerfights/farmerfights_{}.txt".format(datetime.now().strftime('%d-%m-%Y_%H-%M-%S')),"w")
        file.write("L'éleveur {} a été choisi pour {} combats.\n".format(login, nbfightsWntd))
        while i < nbfightsWntd:
            r = api.garden.get_farmer_opponents(token)
            if r["success"]:
                print("Eleveurs correctement chargés. Choix aléatoire de l'éleveur en cours...")
                random.seed()
                opponent = random.choice(r["opponents"])["id"]
                r = api.garden.start_farmer_fight(opponent, token)
                if r["success"]:
                    file.write("https://leekwars.com/fight/{}\n".format(r["fight"]))
                    print("https://leekwars.com/fight/{}".format(r["fight"]))
                else:
                    print("Erreur lors du lancement du combat")
            else:
                print("Erreur lors de l'affichage des éleveurs")
            i += 1
    print ("\n9. Retour")
    print ("0. Quitter")
    choice = input(" >>  ")
    exec_menu(choice)
    return

def menu4():
    print("=====================================================================")
    print("                        INFORMATIONS COMPTE                          ")
    print("=====================================================================")
    print("\nNom d'utilisateur : {}    Habs actuels :  {}\n\n{} Victoires         {} Nuls         {} Défaites \nRatio : {} \n".format(login, money, victories, draws, defeats, ratio))
    print("=====================================================================")
    print("                       INSCRIPTION TOURNOIS                          ")
    print("=====================================================================\n")
    r = api.garden.get(token)
    if r["success"]:
        compositions = sorted(r["garden"]["my_compositions"], key=lambda l: l['id'])
        for i in compositions:
            r = api.team.register_tournament(i["id"], token)
            if r["success"]:
                print("{} a bien été inscrit au tournoi d'équipe.".format(i["name"]))
            else:
                print("{} {} pour le tournoi d'équipe".format(i["name"], r["error"]))
    r = api.farmer.register_tournament(token)
    if r["success"]:
        print("{} a bien été inscrit au tournoi d'éleveur.".format(farmer["name"]))
    else :
        print("{} {} pour le tournoi d'éleveur".format(farmer["name"], r["error"]))
    leeks = sorted(farmer["leeks"].values(), key=lambda l: l['id'])
    for i in leeks:
        r = api.leek.register_tournament(i["id"], token)
        if r["success"]:
            print("{} a bien été inscrit au tournoi solo.".format(i["name"]))
        else :
            print("{} {} pour le tournoi solo".format(i["name"], r["error"]))
    print ("\n9. Retour")
    print ("0. Quitter")
    choice = input(" >>  ")
    exec_menu(choice)
    return

def menu3():
    print("=====================================================================")
    print("                        INFORMATIONS COMPTE                          ")
    print("=====================================================================")
    print("\nNom d'utilisateur : {}    Habs actuels :  {}\n\n{} Victoires         {} Nuls         {} Défaites \nRatio : {} \n".format(login, money, victories, draws, defeats, ratio))
    print("=====================================================================")
    print("                         COMBATS D'EQUIPE                            ")
    print("=====================================================================\n")
    r = api.garden.get(token)
    if r["success"]:
        compositions = sorted(r["garden"]["my_compositions"], key=lambda l: l['id'])
        nbteamfightsTotal = sum(item['fights'] for item in compositions)
        print('\n'.join('Composition {} : {}'.format(i, l['name']) for i, l in enumerate(compositions, 1)))
        if nbteamfightsTotal == 0:
            print("\nPas de combats disponibles, réessayez demain.")
        else:
            compchosen = int(input("Veuillez choisir le numéro correspondant au poireau qui doit se battre : "))
            comp = compositions[compchosen-1]
            nbfightsWntd = int(input("Veuillez choisir le nombre de combats que vous souhaitez lancer : "))
            i = 0
            file = open("logs/teamfights/teamfights_{}.txt".format(datetime.now().strftime('%d-%m-%Y_%H-%M-%S')),"w")
            file.write("La composition {} a été choisie pour {} combats.\n".format(comp["name"], nbfightsWntd))
            while i < nbfightsWntd:
                r = api.garden.get_composition_opponents(comp["id"], token)
                if r["success"]:
                    print("Compositions correctement chargées. Choix aléatoire de la composition en cours...")
                    random.seed()
                    opponent = random.choice(r["opponents"])["id"]
                    r = api.garden.start_team_fight(comp["id"], opponent, token)
                    if r["success"]:
                        file.write("https://leekwars.com/fight/{}\n".format(r["fight"]))
                    else:
                        print("Erreur lors du lancement du combat")
                else:
                    print("Erreur lors de l'affichage des éleveurs")
                i += 1
    print ("9. Retour")
    print ("0. Quitter")
    choice = input(" >>  ")
    exec_menu(choice)
    return
 
# Back to main menu
def back():
    menu_actions['main_menu']()
 
# Exit program
def exit():
    sys.exit()
 
# =======================
#    MENUS DEFINITIONS
# =======================
def maj(token, farmer, login, victories, draws, defeats, ratio, nbfights, money):
    r = api.farmer.get_from_token(token)
    if r["success"]:
        farmer = r["farmer"]
        login = farmer["name"]
        victories = farmer["victories"]
        draws = farmer["draws"]
        defeats = farmer["defeats"]
        ratio = farmer["ratio"]
        nbfights = farmer["fights"]
        money = farmer["habs"]
        return
    else:
        print("MAJ Des informations impossible")
    return
# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': menu2,
    '3': menu3,
    '4': menu4,
    '9': back,
    '0': exit,
}
 
# =======================
#      MAIN PROGRAM
# =======================
 
# Main Program
if __name__ == "__main__":
    os.makedirs("{}/logs/solofights".format(os.getcwd()), exist_ok=True)
    os.makedirs("{}/logs/farmerfights".format(os.getcwd()), exist_ok=True)
    os.makedirs("{}/logs/teamfights".format(os.getcwd()), exist_ok=True)
    api = API.APILeekwars()
    farmer_name = input('Identifiant: ')
    password = getpass.getpass(prompt='Mot de passe: ')
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
        print("Connexion réussie !")
        # launch main menu
        main_menu()
    else:
        print("Erreur lors de la connexion de l'éleveur. Vérifiez vos identifiants.")