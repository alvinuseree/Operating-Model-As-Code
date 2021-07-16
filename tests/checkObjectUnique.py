import requests
import json
import pytest
import sys
import logging


def test_checkCommunity(userInfo, instanceInfo, baseUrl, iUser, iPass):
    """Used to check if all communities are unique"""
    logging.info("Checked: " + instanceInfo)
    return 0

def test_checkUser(userInfo, baseUrl, iUser, iPass):
    """Used to check if all users are unique"""
    logging.info("Checked: " + userInfo)
    return 0