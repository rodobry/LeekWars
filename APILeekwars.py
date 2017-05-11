import requests

class APIAi:
    """docstring for APIAi"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/ai"

    def change_folder(self, ai_id, folder_id, token):
        url = self.url + "/change-folder/"
        return self.session.post(url, data={"ai_id" : ai_id, "folder_id" : folder_id, "token" : token}).json()

    def delete(self, ai_id, token):
        url = self.url + "/delete/"
        return self.session.post(url, data={"ai_id" : ai_id, "token" : token}).json()

    def get(self, ai_id, token):
        url = self.url + "/get/" + str(ai_id) + "/" + token
        return self.session.get(url).json()

    def get_farmer_ais(self, token):
        url = self.url + "/get-farmer-ais/" + token
        return self.session.get(url).json()

    def new(self, folder_id, v2, token):
        url = self.url + "/new/"
        return self.session.post(url, data={"folder_id" : folder_id, "v2" : v2, "token" : token}).json()

    def rename(self, ai_id, new_name, token):
        url = self.url + "/rename/"
        return self.session.post(url, data={"ai_id" : ai_id, "new_name" : new_name, "token" : token}).json()

    def save(self, ai_id, code, token):
        url = self.url + "/save/"
        return self.session.post(url, data={"ai_id" : ai_id, "code" : code, "token" : token}).json()

    def test(self, ai_id, leek_id, bots, type, token):
        url = self.url + "/test/"
        return self.session.post(url, data={"ai_id" : ai_id, "leek_id" : leek_id, "bots" : bots, "type" : type, "token" : token}).json()

    def test_new(self, data, token):
        url = self.url + "/test-new/"
        return self.session.post(url, data={"data" : data, "token" : token}).json()

class APIAiFolder:
    """docstring for APIAiFolder"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/ai-folder"

    def change_folder(self, folder_id, dest_folder_id, token):
        url = self.url + "/change-folder/"
        return self.session.post(url, data={"folder_id" : folder_id, "dest_folder_id" : dest_folder_id, "token" : token}).json()

    def delete(self, folder_id, token):
        url = self.url + "/delete/"
        return self.session.post(url, data={"folder_id" : folder_id, "token" : token}).json()

    def new(self, folder_id, token):
        url = self.url + "/new/"
        return self.session.post(url, data={"folder_id" : folder_id, "token" : token}).json()

    def rename(self, folder_id, new_name, token):
        url = self.url + "/rename/"
        return self.session.post(url, data={"folder_id" : folder_id, "new_name" : new_name, "token" : token}).json()

class APIChangelog:
    """docstring for APIChangelog"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/changelog"

    def get(self, language):
        url = self.url + "/get/" + language
        return self.session.get(url).json()

    def get_last(self, language):
        url = self.url + "/get-last/" + language
        return self.session.get(url).json()

class APIChip:
    """docstring for APIChip"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/chip"

    def get_all(self):
        url = self.url + "/get-all"
        return self.session.get(url).json()

    def get_templates(self):
        url = self.url + "/get-templates"
        return self.session.get(url).json()

class APIConstant:
    """docstring for APIConstant"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/constant"

    def get_all(self):
        url = self.url + "/get-all"
        return self.session.get(url).json()

class APICountry:
    """docstring for APICountry"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/country"

    def get_all(self):
        url = self.url + "/get-all"
        return self.session.get(url).json()

class APIFarmer:
    """docstring for APIFarmer"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/farmer"

    def activate(self, farmer_id, code):
        url = self.url + "/activate/"
        return self.session.post(url, data={"farmer_id" : farmer_id, "code" : code}).json()

    def change_country(self, country_code, token):
        url = self.url + "/change-country/"
        return self.session.post(url, data={"country_code" : country_code, "token" : token}).json()

    def change_password(self, password, new_password, token):
        url = self.url + "/change-password/"
        return self.session.post(url, data={"password" : password, "new_password" : new_password, "token" : token}).json()

    def disconnect(self, token):
        url = self.url + "/disconnect/"
        return self.session.post(url, data={"token" : token}).json()

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
        return self.session.post(url, data={"login" : login, "password" : password}).json()

    def register(self, login, password, email, leek_name, godfather):
        url = self.url + "/register/"
        return self.session.post(url, data={"login" : login, "password" : password, "email" : email, "leek_name" : leek_name, "godfather" : godfather}).json()

    def register_tournament(self, token):
        url = self.url + "/register-tournament/"
        return self.session.post(url, data={"token" : token}).json()

    def set_avatar(self, avatar, token):
        url = self.url + "/set-avatar/"
        return self.session.post(url, data={"avatar" : avatar, "token" : token}).json()

    def set_github(self, github, token):
        url = self.url + "/set-github/"
        return self.session.post(url, data={"github" : github, "token" : token}).json()

    def set_in_garden(self, in_garden, token):
        url = self.url + "/set-in-garden/"
        return self.session.post(url, data={"in_garden" : in_garden, "token" : token}).json()

    def set_website(self, website, token):
        url = self.url + "/set-website/"
        return self.session.post(url, data={"website" : website, "token" : token}).json()

    def unregister(self, password, delete_forum_messages, token):
        url = self.url + "/unregister/"
        return self.session.post(url, data={"password" : password, "delete_forum_messages" : delete_forum_messages, "token" : token}).json()

    def unregister_tournament(self, token):
        url = self.url + "/unregister-tournament/"
        return self.session.post(url, data={"token" : token}).json()

    def update(self, token):
        url = self.url + "/update/"
        return self.session.post(url, data={"token" : token}).json()

class APIFight:
    """docstring for APIFight"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/fight"

    def comment(self, fight_id, comment, token):
        url = self.url + "/comment/"
        return self.session.post(url, data={"fight_id" : fight_id, "comment" : comment, "token" : token}).json()

    def get(self, fight_id):
        url = self.url + "/get/" + str(fight_id)
        return self.session.get(url).json()

    def get_logs(self, fight_id, token):
        url = self.url + "/get-logs/" + str(fight_id) + "/" + token
        return self.session.get(url).json()

class APIFunction:
    """docstring for APIFunction"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/function"

    def get_all(self):
        url = self.url + "/get-all"
        return self.session.get(url).json()

    def get_categories(self):
        url = self.url + "/get-categories"
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
        return self.session.post(url, data={"target_id" : target_id, "token" : token}).json()

    def start_farmer_fight(self, target_id, token):
        url = self.url + "/start-farmer-fight/"
        return self.session.post(url, data={"target_id" : target_id, "token" : token}).json()

    def start_solo_challenge(self, leek_id, target_id, token):
        url = self.url + "/start-solo-challenge/"
        return self.session.post(url, data={"leek_id" : leek_id, "target_id" : target_id, "token" : token}).json()

    def start_solo_fight(self, leek_id, target_id, token):
        url = self.url + "/start-solo-fight/"
        return self.session.post(url, data={"leek_id" : leek_id, "target_id" : target_id, "token" : token}).json()

    def start_team_fight(self, composition_id, target_id, token):
        url = self.url + "/start-team-fight/"
        return self.session.post(url, data={"composition_id" : composition_id, "target_id" : target_id, "token" : token}).json()

class APIHat:
    """docstring for APIHat"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/hat"

    def get_all(self):
        url = self.url + "/get-all"
        return self.session.get(url).json()

    def get_templates(self):
        url = self.url + "/get-templates"
        return self.session.get(url).json()

class APILang:
    """docstring for APILang"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/lang"

    def get(self, file, lang):
        url = self.url + "/get/" + file + "/" + lang
        return self.session.get(url).json()

class APILeek:
    """docstring for APILeek"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/leek"

    def add_chip(self, leek_id, chip_id, token):
        url = self.url + "/add-chip/"
        return self.session.post(url, data={"leek_id" : leek_id, "chip_id" : chip_id, "token" : token}).json()

    def add_weapon(self, leek_id, weapon_id, token):
        url = self.url + "/add-weapon/"
        return self.session.post(url, data={"leek_id" : leek_id, "weapon_id" : weapon_id, "token" : token}).json()

    def create(self, name, token):
        url = self.url + "/create/"
        return self.session.post(url, data={"name" : name, "token" : token}).json()

    def delete_register(self, leek_id, key, token):
        url = self.url + "/delete-register/"
        return self.session.post(url, data={"leek_id" : leek_id, "key" : key, "token" : token}).json()

    def get(self, leek_id):
        url = self.url + "/get/" + str(leek_id)
        return self.session.get(url).json()

    def get_count(self):
        url = self.url + "/get-count"
        return self.session.get(url).json()

    def get_image(self, leek, scale):
        url = self.url + "/get-image/" + str(leek) + "/" + str(scale)
        return self.session.get(url).json()

    def get_level_popup(self, leek_id, token):
        url = self.url + "/get-level-popup/" + str(leek_id) + "/" + token
        return self.session.get(url).json()

    def get_next_price(self, token):
        url = self.url + "/get-next-price/" + token
        return self.session.get(url).json()

    def get_private(self, leek_id, token):
        url = self.url + "/get-private/" + str(leek_id) + "/" + token
        return self.session.get(url).json()

    def get_registers(self, leek_id, token):
        url = self.url + "/get-registers/" + str(leek_id) + "/" + token
        return self.session.get(url).json()

    def register_tournament(self, leek_id, token):
        url = self.url + "/register-tournament/"
        return self.session.post(url, data={"leek_id" : leek_id, "token" : token}).json()

    def remove_ai(self, leek_id, token):
        url = self.url + "/remove-ai/"
        return self.session.post(url, data={"leek_id" : leek_id, "token" : token}).json()

    def remove_chip(self, chip_id, token):
        url = self.url + "/remove-chip/"
        return self.session.post(url, data={"chip_id" : chip_id, "token" : token}).json()

    def remove_hat(self, leek_id, token):
        url = self.url + "/remove-hat/"
        return self.session.post(url, data={"leek_id" : leek_id, "token" : token}).json()

    def remove_weapon(self, weapon_id, token):
        url = self.url + "/remove-weapon/"
        return self.session.post(url, data={"weapon_id" : weapon_id, "token" : token}).json()

    def rename_crystals(self, leek_id, new_name, token):
        url = self.url + "/rename-crystals/"
        return self.session.post(url, data={"leek_id" : leek_id, "new_name" : new_name, "token" : token}).json()

    def rename_habs(self, leek_id, new_name, token):
        url = self.url + "/rename-habs/"
        return self.session.post(url, data={"leek_id" : leek_id, "new_name" : new_name, "token" : token}).json()

    def set_ai(self, leek_id, ai_id, token):
        url = self.url + "/set-ai/"
        return self.session.post(url, data={"leek_id" : leek_id, "ai_id" : ai_id, "token" : token}).json()

    def set_hat(self, leek_id, hat_id, token):
        url = self.url + "/set-hat/"
        return self.session.post(url, data={"leek_id" : leek_id, "hat_id" : hat_id, "token" : token}).json()

    def set_in_garden(self, leek_id, in_garden, token):
        url = self.url + "/set-in-garden/"
        return self.session.post(url, data={"leek_id" : leek_id, "in_garden" : in_garden, "token" : token}).json()

    def set_popup_level_seen(self, leek_id, token):
        url = self.url + "/set-popup-level-seen/"
        return self.session.post(url, data={"leek_id" : leek_id, "token" : token}).json()

    def set_register(self, leek_id, key, value, token):
        url = self.url + "/set-register/"
        return self.session.post(url, data={"leek_id" : leek_id, "key" : key, "value" : value, "token" : token}).json()

    def spend_capital(self, leek, characteristics, token):
        url = self.url + "/spend-capital/"
        return self.session.post(url, data={"leek" : leek, "characteristics" : characteristics, "token" : token}).json()

    def unregister_tournament(self, leek_id, token):
        url = self.url + "/unregister-tournament/"
        return self.session.post(url, data={"leek_id" : leek_id, "token" : token}).json()

    def use_potion(self, leek_id, potion_id, token):
        url = self.url + "/use-potion/"
        return self.session.post(url, data={"leek_id" : leek_id, "potion_id" : potion_id, "token" : token}).json()

class APILeekWars:
    """docstring for APILeekWars"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/leek-wars"

    def version(self):
        url = self.url + "/version"
        return self.session.get(url).json()

class APIMarket:
    """docstring for APIMarket"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/market"

    def buy_crystals(self, item_id, token):
        url = self.url + "/buy-crystals/"
        return self.session.post(url, data={"item_id" : item_id, "token" : token}).json()

    def buy_habs(self, item_id, token):
        url = self.url + "/buy-habs/"
        return self.session.post(url, data={"item_id" : item_id, "token" : token}).json()

    def get_item_templates(self, token):
        url = self.url + "/get-item-templates/" + token
        return self.session.get(url).json()

    def sell_habs(self, item_id, token):
        url = self.url + "/sell-habs/"
        return self.session.post(url, data={"item_id" : item_id, "token" : token}).json()

class APIMessage:
    """docstring for APIMessage"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/message"

    def create_conversation(self, farmer_id, message, token):
        url = self.url + "/create-conversation/"
        return self.session.post(url, data={"farmer_id" : farmer_id, "message" : message, "token" : token}).json()

    def get_latest_conversations(self, count, token):
        url = self.url + "/get-latest-conversations/" + str(count) + "/" + token
        return self.session.get(url).json()

    def get_messages(self, conversation_id, count, page, token):
        url = self.url + "/get-messages/" + str(conversation_id) + "/" + str(count) + "/" + str(page) + "/" + token
        return self.session.get(url).json()

    def quit_conversation(self, conversation_id, token):
        url = self.url + "/quit-conversation/"
        return self.session.post(url, data={"conversation_id" : conversation_id, "token" : token}).json()

    def send_message(self, conversation_id, message, token):
        url = self.url + "/send-message/"
        return self.session.post(url, data={"conversation_id" : conversation_id, "message" : message, "token" : token}).json()

class APINotification:
    """docstring for APINotification"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/notification"

    def get_latest(self, count, token):
        url = self.url + "/get-latest/" + str(count) + "/" + token
        return self.session.get(url).json()

    def read_all(self, token):
        url = self.url + "/read-all/"
        return self.session.post(url, data={"token" : token}).json()

class APIPotion:
    """docstring for APIPotion"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/potion"

    def get_all(self):
        url = self.url + "/get-all"
        return self.session.get(url).json()

class APIRanking:
    """docstring for APIRanking"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/ranking"

    def fun(self, token):
        url = self.url + "/fun/" + token
        return self.session.get(url).json()

    def get(self, category, order, page):
        url = self.url + "/get/" + category + "/" + order + "/" + str(page)
        return self.session.get(url).json()

    def get_farmer_rank(self, farmer_id, order):
        url = self.url + "/get-farmer-rank/" + str(farmer_id) + "/" + order
        return self.session.get(url).json()

    def get_home_ranking(self):
        url = self.url + "/get-home-ranking"
        return self.session.get(url).json()

    def get_leek_rank(self, leek_id, order):
        url = self.url + "/get-leek-rank/" + str(leek_id) + "/" + order
        return self.session.get(url).json()

    def get_team_rank(self, team_id, order):
        url = self.url + "/get-team-rank/" + str(team_id) + "/" + order
        return self.session.get(url).json()

    def search(self, query, search_leeks, search_farmers, search_teams):
        url = self.url + "/search/"
        return self.session.post(url, data={"query" : query, "search_leeks" : search_leeks, "search_farmers" : search_farmers, "search_teams" : search_teams}).json()

class APIService:
    """docstring for APIService"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/service"

    def get_all(self, token):
        url = self.url + "/get-all/" + token
        return self.session.get(url).json()

class APISummon:
    """docstring for APISummon"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/summon"

    def get_templates(self):
        url = self.url + "/get-templates"
        return self.session.get(url).json()

class APITeam:
    """docstring for APITeam"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/team"

    def accept_candidacy(self, candidacy_id, token):
        url = self.url + "/accept-candidacy/"
        return self.session.post(url, data={"candidacy_id" : candidacy_id, "token" : token}).json()

    def ban(self, farmer_id, token):
        url = self.url + "/ban/"
        return self.session.post(url, data={"farmer_id" : farmer_id, "token" : token}).json()

    def cancel_candidacy(self, token):
        url = self.url + "/cancel-candidacy/"
        return self.session.post(url, data={"token" : token}).json()

    def cancel_candidacy_for_team(self, team_id, token):
        url = self.url + "/cancel-candidacy-for-team/"
        return self.session.post(url, data={"team_id" : team_id, "token" : token}).json()

    def change_description(self, description, token):
        url = self.url + "/change-description/"
        return self.session.post(url, data={"description" : description, "token" : token}).json()

    def change_member_grade(self, member_id, new_grade, token):
        url = self.url + "/change-member-grade/"
        return self.session.post(url, data={"member_id" : member_id, "new_grade" : new_grade, "token" : token}).json()

    def change_owner(self, new_owner, password, token):
        url = self.url + "/change-owner/"
        return self.session.post(url, data={"new_owner" : new_owner, "password" : password, "token" : token}).json()

    def create(self, team_name, token):
        url = self.url + "/create/"
        return self.session.post(url, data={"team_name" : team_name, "token" : token}).json()

    def create_composition(self, composition_name, token):
        url = self.url + "/create-composition/"
        return self.session.post(url, data={"composition_name" : composition_name, "token" : token}).json()

    def delete_composition(self, composition_id, token):
        url = self.url + "/delete-composition/"
        return self.session.post(url, data={"composition_id" : composition_id, "token" : token}).json()

    def dissolve(self, token):
        url = self.url + "/dissolve/"
        return self.session.post(url, data={"token" : token}).json()

    def get(self, team_id):
        url = self.url + "/get/" + str(team_id)
        return self.session.get(url).json()

    def get_connected(self, team_id, token):
        url = self.url + "/get-connected/" + str(team_id) + "/" + token
        return self.session.get(url).json()

    def get_private(self, team_id, token):
        url = self.url + "/get-private/" + str(team_id) + "/" + token
        return self.session.get(url).json()

    def move_leek(self, leek_id, to, token):
        url = self.url + "/move-leek/"
        return self.session.post(url, data={"leek_id" : leek_id, "to" : to, "token" : token}).json()

    def quit(self, token):
        url = self.url + "/quit/"
        return self.session.post(url, data={"token" : token}).json()

    def register_tournament(self, composition_id, token):
        url = self.url + "/register-tournament/"
        return self.session.post(url, data={"composition_id" : composition_id, "token" : token}).json()

    def reject_candidacy(self, candidacy_id, token):
        url = self.url + "/reject-candidacy/"
        return self.session.post(url, data={"candidacy_id" : candidacy_id, "token" : token}).json()

    def send_candidacy(self, team_id, token):
        url = self.url + "/send-candidacy/"
        return self.session.post(url, data={"team_id" : team_id, "token" : token}).json()

    def set_emblem(self, team_id, emblem, token):
        url = self.url + "/set-emblem/"
        return self.session.post(url, data={"team_id" : team_id, "emblem" : emblem, "token" : token}).json()

    def set_opened(self, opened, token):
        url = self.url + "/set-opened/"
        return self.session.post(url, data={"opened" : opened, "token" : token}).json()

    def unregister_tournament(self, composition_id, token):
        url = self.url + "/unregister-tournament/"
        return self.session.post(url, data={"composition_id" : composition_id, "token" : token}).json()

class APITestLeek:
    """docstring for APITestLeek"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/test-leek"

    def delete(self, id, token):
        url = self.url + "/delete/"
        return self.session.post(url, data={"id" : id, "token" : token}).json()

    def get_all(self, token):
        url = self.url + "/get-all/" + token
        return self.session.get(url).json()

    def new(self, name, token):
        url = self.url + "/new/"
        return self.session.post(url, data={"name" : name, "token" : token}).json()

    def update(self, id, data, token):
        url = self.url + "/update/"
        return self.session.post(url, data={"id" : id, "data" : data, "token" : token}).json()

class APITestMap:
    """docstring for APITestMap"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/test-map"

    def delete(self, id, token):
        url = self.url + "/delete/"
        return self.session.post(url, data={"id" : id, "token" : token}).json()

    def get_all(self, token):
        url = self.url + "/get-all/" + token
        return self.session.get(url).json()

    def new(self, name, token):
        url = self.url + "/new/"
        return self.session.post(url, data={"name" : name, "token" : token}).json()

    def update(self, id, data, token):
        url = self.url + "/update/"
        return self.session.post(url, data={"id" : id, "data" : data, "token" : token}).json()

class APITestScenario:
    """docstring for APITestScenario"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/test-scenario"

    def delete(self, id, token):
        url = self.url + "/delete/"
        return self.session.post(url, data={"id" : id, "token" : token}).json()

    def get_all(self, token):
        url = self.url + "/get-all/" + token
        return self.session.get(url).json()

    def new(self, name, token):
        url = self.url + "/new/"
        return self.session.post(url, data={"name" : name, "token" : token}).json()

    def update(self, id, data, token):
        url = self.url + "/update/"
        return self.session.post(url, data={"id" : id, "data" : data, "token" : token}).json()

class APIToken:
    """docstring for APIToken"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/token"

    def check(self, token):
        url = self.url + "/check/"
        return self.session.post(url, data={"token" : token}).json()

class APITournament:
    """docstring for APITournament"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/tournament"

    def comment(self, tournament_id, comment, token):
        url = self.url + "/comment/"
        return self.session.post(url, data={"tournament_id" : tournament_id, "comment" : comment, "token" : token}).json()

    def get(self, tournament_id, token):
        url = self.url + "/get/" + str(tournament_id) + "/" + token
        return self.session.get(url).json()

class APITrophy:
    """docstring for APITrophy"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/trophy"

    def get_admin(self, lang, token, supertoken):
        url = self.url + "/get-admin/" + lang + "/" + token + "/" + supertoken
        return self.session.get(url).json()

    def get_all(self):
        url = self.url + "/get-all"
        return self.session.get(url).json()

    def get_categories(self):
        url = self.url + "/get-categories"
        return self.session.get(url).json()

    def get_farmer_trophies(self, farmer_id, lang, token):
        url = self.url + "/get-farmer-trophies/" + str(farmer_id) + "/" + lang + "/" + token
        return self.session.get(url).json()

    def unlock(self, trophy_id, token):
        url = self.url + "/unlock/"
        return self.session.post(url, data={"trophy_id" : trophy_id, "token" : token}).json()

class APIWeapon:
    """docstring for APIWeapon"""
    def __init__(self, session):
        self.session = session
        self.url = "https://leekwars.com/api/weapon"

    def get_all(self):
        url = self.url + "/get-all"
        return self.session.get(url).json()

    def get_templates(self):
        url = self.url + "/get-templates"
        return self.session.get(url).json()


class APILeekwars():
    """docstring for APILeekwars"""
    def __init__(self):
        self.session = requests.Session()
        self.ai = APIAi(self.session)
        self.aiFolder = APIAiFolder(self.session)
        self.changelog = APIChangelog(self.session)
        self.chip = APIChip(self.session)
        self.constant = APIConstant(self.session)
        self.country = APICountry(self.session)
        self.farmer = APIFarmer(self.session)
        self.fight = APIFight(self.session)
        self.function = APIFunction(self.session)
        self.garden = APIGarden(self.session)
        self.hat = APIHat(self.session)
        self.lang = APILang(self.session)
        self.leek = APILeek(self.session)
        self.leekWars = APILeekWars(self.session)
        self.market = APIMarket(self.session)
        self.message = APIMessage(self.session)
        self.notification = APINotification(self.session)
        self.potion = APIPotion(self.session)
        self.ranking = APIRanking(self.session)
        self.service = APIService(self.session)
        self.summon = APISummon(self.session)
        self.team = APITeam(self.session)
        self.testLeek = APITestLeek(self.session)
        self.testMap = APITestMap(self.session)
        self.testScenario = APITestScenario(self.session)
        self.token = APIToken(self.session)
        self.tournament = APITournament(self.session)
        self.trophy = APITrophy(self.session)
        self.weapon = APIWeapon(self.session)
