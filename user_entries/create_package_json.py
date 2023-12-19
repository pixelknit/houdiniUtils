import json
import sys
import os

with open("user_data.json","r") as file:
    user_data = json.load(file)

user_machine = os.getlogin()
json_dict = {}

with open("packages/company_vars.json","w") as env_file:
    for user in user_data:
        if user_machine in user_data[user].values():
            print("User found, setting env variables")
            print(user_data[user])
            json_dict["env"] = [{"USER_ID":str(user_data[user]["id"])}]
            json.dump(json_dict, env_file, indent=4)
