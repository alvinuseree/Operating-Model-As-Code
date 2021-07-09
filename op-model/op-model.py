import json
import logging
import getpass
import os
import pytest
from openFiles import *
from consoleOperations import *
import argparse

""" 
Description:    Main script that runs modules to create and add content to the existing colibra operating model.
Structure:      
                - Assets: Contains extra documentation to add to the op model
                - Configs: Contains metadata on the connection params
                - Test: Tests run
                - Op-Model: Contains all py files
Tests:
                - Check if file structure is correct (see above)
                - Check if all files used have valid Json (validJson)
                - Test Connection to the Cloud (testConnection)
Other Modules:
                - Restoring Environment to clean set (restoreEnvironment)

"""
#Logging Setup:
root = logging.getLogger()
logging.basicConfig(format='%(asctime)s.%(msecs)03d %(levelname)s file: [%(module)s] %(message)s', datefmt='%Y-%m-%d,%H:%M:%S', level=logging.INFO)
root.setLevel(logging.DEBUG)

#Set Argparse instance:
parser = argparse.ArgumentParser(description='Operating Model as Code is a mechanism at which we can refresh and update the Kubrick Collibra Operating Model used for Data Management Cohorts in an automated and governed manner.')
parser.add_argument('-o', '--gethelp', nargs='?', const='arg_was_not_given', help='used to get help on how to use this')
args = parser.parse_args()

if args.gethelp is None:
    #Tests to confirm path files exist & Valid Json:
    logging.info("Confirming Directory is not Corrupted ...")
    pytest.main([
        "tests/correctStructure.py", 
        "tests/validJson.py"
    ])

    #Read files:
    instanceInfo = openInstance()
    userInfo = openUsers()

    #Grab credentials from the user:
    logging.info(' Please ensure that your credentials exist in the clean backup')
    baseUserName = input('Enter Username for the Data Intelligence Cloud: ')
    basePassword = getpass.getpass('Enter Password for the Data Intelligence Cloud: ')

    consoleUserName = input('\nEnter Username for the Console: ')
    consolePassword = getpass.getpass('Enter Password for the Console: ')

    #Test Connection to the Cloud:
    logging.info(' Testing Connectivity ...')

    #Arguments:
    baseArg = "--baseUrl=" + instanceInfo['base']
    consoleArg = "--consoleUrl=" + instanceInfo['console']
    iUserArg = "--iUser=" + baseUserName
    iPassArg = "--iPass=" + basePassword
    cUserArg = "--cUser=" + consoleUserName
    cPassArg = "--cPass=" + consolePassword

    connectionTest = pytest.main([
        "-x", 
        "--tb=line", 
        "tests/testConnection.py", 
        baseArg, consoleArg, iUserArg, iPassArg, cUserArg, cPassArg
    ])       
    #-x and tb-line ensures end after 1 fail and only show results
    print(connectionTest)

    #Test Connection to the Cloud:
    restoreEnvironment(instanceInfo['console'], consoleUserName, consolePassword, instanceInfo['backup-id'], instanceInfo['environment-id'])

else:
    print(
        """
        Thank you for using this application.
        You can find the repo for this app here: https://stackoverflow.com/questions/15754208/how-to-make-argument-optional-in-python-argparse"""
    )