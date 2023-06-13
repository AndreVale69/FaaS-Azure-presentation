import logging

import azure.functions as func
import json
from random import randint
# from pathlib import Path

# calcola-somma function
def main(req: func.HttpRequest) -> func.HttpResponse:
        logging.info('Python HTTP trigger function processed a request.')
        users = {"1754462800": {"name": "John", "surname": "Doe", "email": "john.doe@email.com"}, "4659781230": {"name": "Mario", "surname": "Rossi", "email": "mario.rossi@email.com"}, "7845120036": {"name": "Mattia", "surname": "Di Nardo", "email": "mattia.di.nardo@email.com"}, "9956223017": {"name": "Angela", "surname": "Donadoni", "email": "angela.donadoni@email.com"}, "3328182950": {"name": "Maria", "surname": "Lorena", "email": "maria.lorena@email.com"}}

        # GET method
        if req.method == "GET":
                # read users file
                # with open(str(Path.cwd()) + "\\ServerPOST\\users.json", "r") as file:
                #         parsed = json.load(file)
                #         users = json.dumps(parsed, indent=4)
                
                # HTTP Response
                return func.HttpResponse(
                        f"This HTTP triggered function executed successfully.\nThe users are: {json.dumps(users, indent=4)}",
                        status_code=200
                )
        
        # POST method
        if req.method == "POST":
                # if there are params
                if len(req.params) >= 3:
                        # take data
                        id = randint(1000000000, 9999999999)
                        name = req.params.get("name")
                        surname = req.params.get("surname")
                        email = req.params.get("email")
                        
                        # read users file
                        # with open(str(Path.cwd()) + "\\ServerPOST\\users.json", "r") as file:
                        #         users = json.load(file)

                        # append new user
                        # users[str(id)] = {
                        #                 "name": name,
                        #                 "surname": surname,
                        #                 "email": email
                        # }
                        
                        user = {id: {
                                "name": name,
                                "surname": surname,
                                "email": email
                        }}

                        # insert new format file
                        # with open(str(Path.cwd()) + "\\ServerPOST\\users.json", "w") as file:
                        #         json.dump(users, file)
                        
                        # HTTP Response
                        return func.HttpResponse(
                                f"This HTTP triggered function executed successfully.\nThe user has been added!\nDetails:{json.dumps(user, indent=4)}",
                                status_code=200
                        )
                # otherwise, check body
                else:
                        # take body
                        req_body = req.get_json()
                        
                        # gen id
                        id = randint(1000000000, 9999999999)

                        # read file
                        # with open(str(Path.cwd()) + "\\ServerPOST\\users.json", "r") as file:
                        #         users = json.load(file)
                        
                        # append new user
                        user = {
                                id: 
                                {
                                        "name": req_body["name"],
                                        "surname": req_body["surname"],
                                        "email": req_body["email"]
                                }
                        }

                        # insert new format file
                        # with open(str(Path.cwd()) + "\\ServerPOST\\users.json", "w") as file:
                        #         json.dump(users, file)
                        
                        # HTTP Response
                        return func.HttpResponse(
                                f"This HTTP triggered function executed successfully.\nThe user has been added!\nDetails:{json.dumps(user, indent=4)}",
                                status_code=200
                        )
        
        # DELETE method
        if req.method == "DELETE":
                # read users file
                # with open(str(Path.cwd()) + "\\ServerPOST\\users.json", "r") as file:
                #         users = json.load(file)

                # take id from params
                id_user = req.params.get("id")
                
                # deepcopy
                users_pre_delete = users.copy()

                # delete user
                users.pop(id_user)
                
                # insert new format file
                # with open(str(Path.cwd()) + "\\ServerPOST\\users.json", "w") as file:
                #         json.dump(users, file)
                
                # HTTP Response
                return func.HttpResponse(
                        f"This HTTP triggered function executed successfully.\nThe user has been deleted!\nUsers pre-delete:{json.dumps(users_pre_delete, indent=4)}\nUsers after-delete:{json.dumps(users, indent=4)}",
                        status_code=200
                )