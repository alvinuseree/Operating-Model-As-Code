import json                                 #Used to parse Json config files
import logging                              #Logging library
import getpass                              #Hides password when grabbed from user
import os                                   #
import pytest                               #Runs tests on application on run 
import argparse                             #Grabs arguements on run
import sys                                  #sys(exit) used to stop flow under certain conditions

#Custom python files:
from openFiles import *                     #Opens all config and asset files
from consoleOperations import *             #Allows us to run our operations on the Collibra Console
from createObject import *                  #Creates Collibra Objects (Assets, Users, Domains etc)


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

parser.add_argument('-g', '--getHelp', help='used to get help on how to use this')
parser.add_argument('-p', '--partialSync', help='used to indicate if the user wants to refresh the instance')
parser.add_argument('-f', '--fullSync', help='used to a full sychronisation of the op model')

args = parser.parse_args()

#Test to confirm: Only 1 arg has been passed:
if len(sys.argv) != 3:
    logging.info(len(sys.argv))
    logging.error("To run this application you need to pass one of 3 arguments: -g getHelp, -p partialSync or -f fullSync")
    sys.exit()

#If the getHelp arg is not passed then we run some basic tests on the some of the configurations
if args.getHelp is None:

    #Tests to confirm path files exist & Valid Json:
    logging.info("Confirming Directory is not Corrupted ...")
    assert pytest.main([
        "tests/correctStructure.py", 
        "tests/validJson.py"
    ]) == 0

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

    #Test Connection to the Cloud:
    logging.info(' Testing Connectivity ...')

    #Arguments:
    baseArg = "--baseUrl=" + instanceInfo['application']['url']
    consoleArg = "--consoleUrl=" + instanceInfo['console']['url']
    iUserArg = "--iUser=" + baseUserName
    iPassArg = "--iPass=" + basePassword
    cUserArg = "--cUser=" + consoleUserName
    cPassArg = "--cPass=" + consolePassword

    #Testing Credentials the user has provided
    assert pytest.main([
        "-x", 
        "--tb=line", 
        "tests/testConnection.py", 
        baseArg, consoleArg, iUserArg, iPassArg, cUserArg, cPassArg
    ]).value == 0       
    #-x and tb-line ensures end after 1 fail and only show results

    userInfoArg = "--userInfo=" + str(userInfo)
    instanceArg = "--instanceInfo=" + str(instanceInfo)

    #Test to see if all required Objects are Unique
    assert pytest.main([
        "-x", 
        "--tb=line", 
        "tests/checkObjectUnique.py", 
        baseArg, iUserArg, iPassArg, userInfoArg, instanceArg
    ]).value == 0      

    #Full Sync entails a restoration of the environment before creating the op model
    if args.fullSync is not None:
        restoreEnvironment(instanceInfo['console']['url'], consoleUserName, consolePassword, instanceInfo['console']['backup-id'], instanceInfo['console']['environment-id'])

    #Create Op-Model:
    #Naming Convention - [First Name Last Name - Object]

    #Add parent communities: Collibra Documentation, Consultant Communities, Configurations
    communityIds = []

    #Add container Community for all the op-model content
    containerCommunity = createCommunity(
        instanceInfo['application']['url'],
        baseUserName,
        basePassword,
        "none",
        "Container",
        "Temporary Container Community"
    )['id']

    for tpCommunity in instanceInfo['top-level']:
        communityIds.append(createCommunity(
            instanceInfo['application']['url'],
            baseUserName,
            basePassword,
            containerCommunity,
            tpCommunity['name'],
            tpCommunity['description']
        )['id'])
      
    # In Configurations Community, create a domain called [Profiles]:
    profileDomain = createDomain(
        instanceInfo['application']['url'],
        baseUserName,
        basePassword,
        "Profiles",
        userInfo['domain-uuid'],
        communityIds[1],
        "Consultant Profiles"
    )['id']

    # In Collibra Documentation create Articles and Certifications Domain
    articlesDomain = createDomain(
        instanceInfo['application']['url'],
        baseUserName,
        basePassword,
        "Articles",
        articleInfo['domain-uuid'],
        communityIds[0],
        "List of Articles"
    )['id']

    certsDomain = createDomain(
        instanceInfo['application']['url'],
        baseUserName,
        basePassword,
        "Certifications",
        certInfo['domain-uuid'],
        communityIds[0],
        "Certs"
    )['id']     

    # For every User in file:
    for consultant in userInfo['users']: 
        # Create a user with the permissions set in the file
        newUser = createUser(
            instanceInfo['application']['url'],
            baseUserName,
            basePassword,
            consultant['first-name'],
            consultant['last-name'],
            consultant['first-name'] + '.' + consultant['last-name'],
            consultant['user-type'],
            consultant['email']
        )['id']

        # Add Profile Asset to Profiles Domain - [First Name Last Name]
        createAsset(
            instanceInfo['application']['url'],
            baseUserName,
            basePassword,
            consultant['first-name'] + ' ' + consultant['last-name'],
            exerciseInfo['uuid'],
            profileDomain,
            [{
                "typeId": "00000000-0000-0000-0000-000000000202",
                "value": "This consultant is has permissions for: " + consultant['user-type']
            }],
            []
        )

        # Add Community in Consultant Communities -  [First Name Last Name Community]
        consultantCommunity = createCommunity(
            instanceInfo['application']['url'],
            baseUserName,
            basePassword,
            communityIds[2],
            consultant['first-name'] + ' ' + consultant['last-name'],
            consultant['first-name'] + ' ' + consultant['last-name'] + "'s personal community"
        )['id']

        #Give Profile Permissions on Consultant Community:
        createResponsibility(
            instanceInfo['application']['url'],
            baseUserName,
            basePassword,
            newUser,
            instanceInfo['permissions']['owner'],
            consultantCommunity,
            "Community"
        )

        # Add domains: [First Name Last Name - Exercises] in First Name Last Name Community
        consultantExerciseDomain = createDomain(
            instanceInfo['application']['url'],
            baseUserName,
            basePassword,
            consultant['first-name'] + ' ' + consultant['last-name'] + ' Exercises',
            exerciseInfo['domain-uuid'],
            consultantCommunity,
            "You'll find all your exercises here"
        )['id']

        # For every Exercise in file:
        for exercises in exerciseInfo['exercises']:
            # Add Exercise to First Name Last Name - Exercises called [Exercise Name]            
            createAsset(
                instanceInfo['application']['url'],
                baseUserName,
                basePassword,
                exercises['name'],
                exerciseInfo['uuid'],
                consultantExerciseDomain,
                [{
                    "typeId": "00000000-0000-0000-0000-000000000202",
                    "value": exercises['description']
                },{
                    "typeId": "00000000-0000-0000-0000-000000003115",
                    "value": exercises['instructions']
                },],
                []
            )['id']            
    # 4: For every Article in file:
        # Add article to Articles Domain - [Article Name]

    # For every Certification in file:
    for certification in certInfo['certifications']:
        # Add Certification to Cert Domain - [Cert Name]
        createAsset(
            instanceInfo['application']['url'],
            baseUserName,
            basePassword,
            certification['name'],
            certInfo['uuid'],
            certsDomain,
            [{
                "typeId": "00000000-0000-0000-0000-000000000202",
                "value": certification['description']
            }],
            []
        )['id']          

#User goes down this path if they pass no arguements
else:
    print(
        """
        Thank you for using this application.
        You can find the repo for this app here: https://gitlab.com/Alvin.Useree/operating-model-as-code/"""
    )