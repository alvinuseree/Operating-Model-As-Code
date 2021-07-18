import json                                 #Used to parse Json config files
import logging                              #Logging library
import getpass                              #Hides password when grabbed from user
import os                                   #
import argparse                             #Grabs arguements on run
import sys                                  #sys(exit) used to stop flow under certain conditions

#Custom python files:
from openFiles import *                     #Opens all config and asset files
from consoleOperations import *             #Allows us to run our operations on the Collibra Console
from testExecutions import *
from generateOperatingModel import *


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

#Set Argparse instance:
parser = argparse.ArgumentParser(description='Operating Model as Code is a mechanism at which we can refresh and update the Kubrick Collibra Operating Model used for Data Management Cohorts in an automated and governed manner.')

parser.add_argument('-g', '--getHelp', help='used to get help on how to use this')
parser.add_argument('-p', '--partialSync', help='used to indicate if the user wants to refresh the instance')
parser.add_argument('-f', '--fullSync', help='used to a full sychronisation of the op model')

args = parser.parse_args()

#Test to confirm: Only 1 arg has been passed:
if totalArguements(sys.argv) != 1:
    sys.exit()

#If the getHelp arg is not passed then we run some basic tests on the some of the configurations
if args.getHelp is None:

    #Read files:
    instanceInfo = openInstance()
    userInfo = openUsers()

    articleInfo = openArticles()
    certInfo = openCerts()
    exerciseInfo = openExercises()

    #Grab credentials from the user:
    logging.info(' Please ensure that your credentials exist in the clean backup')
    baseUserName = input('Enter Username for the Data Intelligence Cloud: ')
    basePassword = getpass.getpass('Enter Password for the Data Intelligence Cloud: ')

    consoleUserName = input('\nEnter Username for the Console: ')
    consolePassword = getpass.getpass('Enter Password for the Console: ')

    #Run all tests on the this Application:
    executeTestStrategy(baseUserName, basePassword, consoleUserName, consolePassword, instanceInfo, userInfo)
 
    #Full Sync entails a restoration of the environment before creating the op model
    if args.fullSync is not None:
        restoreEnvironment(instanceInfo['console']['url'], consoleUserName, consolePassword, instanceInfo['console']['backup-id'], instanceInfo['console']['environment-id'])

    #Generate the complete Operating Model
    generateOpmodel(baseUserName, basePassword, instanceInfo, userInfo, articleInfo, certInfo, exerciseInfo)          

#User goes down this path if they pass no arguements
else:
    print(
        """
        Thank you for using this application.
        You can find the repo for this app here: https://gitlab.com/Alvin.Useree/operating-model-as-code/"""
    )