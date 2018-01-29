# Lists of functions to manage accounts

import os.path
import json

class AccountsManager:
    accounts = []
    def add(self, name, password):
        self.load()
        for account in self.accounts:
            if account['login'] == name:
                account['pw'] = password
                self.save()
                return 2
        self.accounts.append(dict([("login", name),("pw", password)]))
        self.save()
        return 1
    def getAll(self):
        self.load()
        return self.accounts
    def load(self):
        if os.path.exists('cfg/config.json') and os.path.getsize('cfg/config.json') > 0:
            with open('cfg/config.json') as json_data_file:
                self.accounts = json.load(json_data_file)
        else:
            os.makedirs("{}/cfg".format(os.getcwd()), exist_ok=True)
            self.accounts = []
    def save(self):
        with open('cfg/config.json', 'w') as outfile:
            json.dump(self.accounts, outfile)
