import requests
import json
import pytest

def test_check_instance_up(baseUrl):
    """Used to check if the instance is running"""
    try:
        instance = requests.get(baseUrl)
        assert instance.status_code == 200
    except:
        pytest.fail("Instance: " + baseUrl + " is not up ...")

def test_check_console_up(consoleUrl):
    """Used to check if the console is running"""
    try:
        console = requests.get(consoleUrl)
        assert console.status_code == 200
    except:
        pytest.fail("Console at: " + consoleUrl + " is not up ...")  

def test_instance_credentials(baseUrl, iUser, iPass):
    postSession = {
        "username": iUser,
        "password": iPass
    }  

    instance = requests.post(baseUrl + "rest/2.0/auth/sessions", json = postSession)
    assert instance.status_code == 200

def test_console_credentials(consoleUrl, cUser, cPass):
    instance = requests.get(consoleUrl + "rest/environment", auth = (cUser, cPass))
    assert instance.status_code == 200    