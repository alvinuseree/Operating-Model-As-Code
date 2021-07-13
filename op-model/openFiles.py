import json
import logging
import sys

def openInstance():
    #Open instance configurations json file:
    with open("config/instance.json") as jsonFile:
        #Check Valid Json:
        jsonObject = json.load(jsonFile)
        jsonFile.close()        

    #Run check to see if the schema is correct:

    #Config Variables:
    baseUrl = jsonObject['application']['url']
    consoleUrl = jsonObject['console']['url']
    backupToRestore = jsonObject['console']['backup-id']
    envId = jsonObject['console']['environment-id']

    return {"base": baseUrl, "console": consoleUrl, "backup-id": backupToRestore, "environment-id": envId}

def openUsers():
    with open("config/users.json") as jsonFile:
        #Check Valid Json:
        jsonObject = json.load(jsonFile)
        jsonFile.close()
        
        return jsonObject