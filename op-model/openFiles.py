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

    return jsonObject

def openUsers():
    with open("config/users.json") as jsonFile:
        #Check Valid Json:
        jsonObject = json.load(jsonFile)
        jsonFile.close()
        
        return jsonObject

def openArticles():
    with open("assets/articles.json") as jsonFile:
        #Check Valid Json:
        jsonObject = json.load(jsonFile)
        jsonFile.close()
        
        return jsonObject   

def openCerts():
    with open("assets/certifications.json") as jsonFile:
        #Check Valid Json:
        jsonObject = json.load(jsonFile)
        jsonFile.close()
        
        return jsonObject   

def openExercises():
    with open("assets/exercises.json") as jsonFile:
        #Check Valid Json:
        jsonObject = json.load(jsonFile)
        jsonFile.close()
        
        return jsonObject  