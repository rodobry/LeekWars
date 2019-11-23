import APILeekwars as API
import getpass

api = API.APILeekwars()
farmer_name = input('Login: ')
password = getpass.getpass(prompt='Password: ')
r = api.farmer.login_token(farmer_name, password)
if r and 'token' in r:
    farmer = r["farmer"]
    token = r["token"]
    r = api.garden.get(token)
    if r and 'garden' in r:
        compositions = sorted(r["garden"]["my_compositions"], key=lambda l: l['id'])
        for i in compositions:
            r = api.team.register_tournament(i["id"], token)
            if r and [] == r:
                print("{} a bien été inscrit au tournoi d'équipe.".format(i["name"]))
            else:
                print("{} {} pour le tournoi d'équipe".format(i["name"], r["error"]))
    r = api.farmer.register_tournament(token)
    if r and [] == r:
        print("{} a bien été inscrit au tournoi d'éleveur.".format(farmer["name"]))
    else:
        print("{} {} pour le tournoi d'éleveur".format(farmer["name"], r["error"]))
    leeks = sorted(farmer["leeks"].values(), key=lambda l: l['id'])
    for i in leeks:
        r = api.leek.register_tournament(i["id"], token)
        if r and [] == r:
            print("{} a bien été inscrit au tournoi solo.".format(i["name"]))
        else:
            print("{} {} pour le tournoi solo".format(i["name"], r["error"]))
    r = api.farmer.disconnect(token)
else:
    print("Erreur lors de la connexion du fermier. Vérifiez vos identifiants.")
