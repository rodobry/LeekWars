import requests

class APIAI:
    """docstring for watson"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/ai"

    def change_folder(self, ai_id, folder_id, token):
        url = self.url + "/change-folder/"
        return self.session.post(url, data = {"ai_id" : ai_id, "folder_id" : folder_id, "token" : token}).json()

    def delete(self, ai_id, token):
        url = self.url + "/delete/"
        return self.session.post(url, data = {"ai_id" : ai_id, "token" : token}).json()

    def get(self, ai_id, token):
        url = self.url + "/get/" + ai_id + "/" + token
        return self.session.get(url).json()

    def get_farmer_ais(self, token):
        url = self.url + "/get-farmer-ais/" + token
        return self.session.get(url).json()

    def new(self, folder_id, v2, token):
        url = self.url + "/new/"
        return self.session.post(url, data = {"folder_id" : folder_id, "v2": v2, "token" : token}).json()

    def rename(self, ai_id, new_name, token):
        url = self.url + "/rename/"
        return self.session.post(url, data = {"ai_id" : ai_id, "new_name": new_name, "token" : token}).json()

    def save(self, ai_id, code, token):
        url = self.url + "/save/"
        return self.session.post(url, data = {"ai_id" : ai_id, "code": code, "token" : token}).json()

    def test(self, ai_id, leek_id, bots, type, token):
        url = self.url + "/test/"
        return self.session.post(url, data = {"ai_id" : ai_id, "leek_id": leek_id, "bots": bots, "type": type, "token" : token}).json()

    def test_new(self, data, token):
        """example@https://gist.github.com/5pilow/72294ce31f856c730e1ffb17528d7c31"""
        url = self.url + "/test-new/"
        return self.session.post(url, data = {"data" : data, "token" : token}).json()

class APIFarmer:
    """docstring for wat"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/farmer"

    def activate(self, farmer_id, code):
        url = self.url + "/activate/"
        return self.session.post(url, data = {"farmer_id" : farmer_id, "code" : code}).json()

    def change_country(self, country_code, token):
        url = self.url + "/change-country/"
        return self.session.post(url, data = {"country_code" : country_code, "token" : token}).json()

    def change_password(self, password, new_password, token):
        url = self.url + "/change-password/"
        return self.session.post(url, data = {"password" : password, "new_password" : new_password, "token" : token}).json()

    def disconnect(self, token):
        url = self.url + "/disconnect/"
        return self.session.post(url, data = {"token" : token}).json()

    def get(self, farmer_id):
        url = self.url + "/get/" + str(farmer_id)
        return self.session.get(url).json()

    def get_connected(self):
        url = self.url + "/get-connected"
        return self.session.get(url).json()

    def get_from_token(self, token):
        url = self.url + "/get-from-token/" + token
        return self.session.get(url).json()

    def login_token(self, login, password):
        url = self.url + "/login-token/"
        return self.session.post(url, data = {"login" : login,
                                            "password" : password}).json()

    def register(self, login, password, email, leek_name, godfather):
        url = self.url + "/register/"
        return self.session.post(url, data = {"login" : login,
                                            "password" : password,
                                            "email" : email,
                                            "leek_name" : leek_name,
                                            "godfather" : godfather}).json()

    def regiter_tournament(self, token):
        url = self.url + "/register-tournament/"
        return self.session.post(url, data = {"token" : token}).json()

    def set_avatar(self, avatar, token):
        url = self.url + "/set-avatar/"
        return self.session.post(url, data = {"token" : token}, files = {"avatar" : avatar}).json()

    def set_github(self, github, token):
        url = self.url + "/set-github/"
        return self.session.post(url, data = {"github" : github, "token" : token}).json()

    def set_in_garden(self, in_garden, token):
        url = self.url + "/set-in-garden/"
        return self.session.post(url, data = {"in_garden" : in_garden, "token" : token}).json()

    def set_wesbite(self, website, token):
        url = self.url + "/set-website/"
        return self.session.post(url, data = {"website" : website, "token" : token}).json()

    def unregister(self, password, delete_forum_messages, token):
        url = self.url + "/unregister/"
        return self.session.post(url, data = {"password" : password, "delete_forum_messages" : delete_forum_messages, "token" : token}).json()

    def unregister_tournament(self, token):
        url = self.url + "/unregister-tournament/"
        return self.session.post(url, data = {"token" : token}).json()

    def update(self, token):
        url = self.url + "/update/"
        return self.session.post(url, data = {"token" : token}).json()

class APIFight:
    """docstring for APIFight"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/fight"

    def comment(self, fight_id, comment, token):
        url = self.url + "/comment/"
        return self.session.post(url, data = {"fight_id" : fight_id, "comment" : comment, "token" : token}).json()

    def get(self, fight_id):
        url = self.url + "/get/" + str(fight_id)
        return self.session.get(url).json()

    def get_logs(self, fight_id, token):
        url = self.url + "/get-logs/" + str(fight_id) + "/" + token
        return self.session.get(url).json()

class APIFunction():
    """docstring for APIFunction"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/function"

    def get_all(self):
        url = self.url + "/get-all/"
        return self.session.get(url).json()

    def get_categories(self):
        url = self.url + "/get-categories/"
        return self.session.get(url).json()

class APIGarden:
    """docstring for APIGarden"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/garden"

    def get(self, token):
        url = self.url + "/get/" + token
        return self.session.get(url).json()

    def get_composition_opponents(self, composition, token):
        url = self.url + "/get-composition-opponents/" + str(composition) + "/" + token
        return self.session.get(url).json()

    def get_farmer_challenge(self, target, token):
        url = self.url + "/get-farmer-challenge/" + str(target) + "/" + token
        return self.session.get(url).json()

    def get_farmer_opponents(self, token):
        url = self.url + "/get-farmer-opponents/" + token
        return self.session.get(url).json()

    def get_leek_opponents(self, leek_id, token):
        url = self.url + "/get-leek-opponents/" + str(leek_id) + "/" + token
        return self.session.get(url).json()

    def get_solo_challenge(self, leek_id, token):
        url = self.url + "/get-solo-challenge/" + str(leek_id) + "/" + token
        return self.session.get(url).json()

    def start_farmer_challenge(self, target_id, token):
        url = self.url + "/start-farmer-challenge/"
        return self.session.post(url, data = {"target_id" : target_id, "token" : token}).json()

    def start_farmer_fight(self, target_id, token):
        url = self.url + "/start-farmer-fight/"
        return self.session.post(url, data = {"target_id" : target_id, "token" : token}).json()

    def start_solo_challenge(self, leek_id, target_id, token):
        url = self.url + "/start-solo-challenge/"
        return self.session.post(url, data = {"leek_id" : leek_id, "target_id" : target_id, "token" : token}).json()

    def start_solo_fight(self, leek_id, target_id, token):
        url = self.url + "/start-solo-fight/"
        return self.session.post(url, data = {"leek_id" : leek_id, "target_id" : target_id, "token" : token}).json()

    def start_team_fight(self, composition_id, target_id, token):
        url = self.url + "/start-team-fight/"
        return self.session.post(url, data = {"composition_id" : composition_id, "target_id" : target_id, "token" : token}).json()

class APILeek:
    """docstring for APILeek"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/leek"

    def get_registers(self, leek_id, token):
        url = self.url + "/get-registers/" + str(leek_id) + "/" + token
        return self.session.get(url).json()

    def set_register(self, leek_id, key, value, token):
        url = self.url + "/set-register/"
        return self.session.post(url, data = {"leek_id" : leek_id, "key" : key, "value" : value, "token" : token}).json()

class APINotification:
    """docstring for APILeek"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/notification"

    def get_latest(self, count, token):
        url = self.url + "/get-latest/" + str(count) + "/" + token
        return self.session.get(url).json()

    def read_all(self, token):
        url = self.url + "/read-all/"
        return self.session.post(url, data = {"token" : token}).json()

class APIService:
    """docstring for APIService"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/service"

    def get_all(self, token):
        url = self.url + "/get-all/" + token
        return self.session.get(url).json()


class APILeekwars():
    """docstring for APILeekwars"""
    def __init__(self):
        self.session = requests.Session()
        self.ai = APIAI(self.session)
        self.farmer = APIFarmer(self.session)
        self.fight = APIFight(self.session)
        self.function = APIFunction(self.session)
        self.garden = APIGarden(self.session)
        self.leek = APILeek(self.session)
        self.notification = APINotification(self.session)
        self.service = APIService(self.session)
