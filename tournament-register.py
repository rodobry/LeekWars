import APILeekwars as API
import getpass

api = API.APILeekwars()
farmer_name = input('Login: ')
password = getpass.getpass(prompt='Password: ')
r = api.farmer.login_token(farmer_name, password)