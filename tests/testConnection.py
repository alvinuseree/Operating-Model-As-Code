import requests
import json
import pytest
import sys
import logging                              #Logging library

def test_check_instance_up(baseUrl):
    """Used to check if the instance is running"""
    try:
        instance = requests.get(baseUrl)
        assert instance.status_code == 200
    except:
        logging.error("Instance: " + baseUrl + " is not up")
        pytest.fail("Instance: " + baseUrl + " is not up ...")

def test_check_console_up(consoleUrl):
    """Used to check if the console is running"""
    try:
        console = requests.get(consoleUrl)
        assert console.status_code == 200
    except:
        logging.error("Console at: " + consoleUrl + " is not up ...")
        pytest.fail("Console at: " + consoleUrl + " is not up ...")  

def test_instance_credentials(baseUrl, iUser, iPass):
    postSession = {
        "username": iUser,
        "password": iPass
    }
    try:
        instance = requests.post(baseUrl + "rest/2.0/auth/sessions", json = postSession)
        assert instance.status_code == 200
    except:
        logging.error("Incorrect Application Credentials to " + baseUrl) 
        pytest.fail("Incorrect Application Credentials") 

def test_console_credentials(consoleUrl, cUser, cPass):
    try:
        instance = requests.get(consoleUrl + "rest/environment", auth = (cUser, cPass))
        assert instance.status_code == 200   
    except:
        logging.error("Incorrect Console Credentials to " + consoleUrl)  
        pytest.fail("Incorrect Console Credentials") 
