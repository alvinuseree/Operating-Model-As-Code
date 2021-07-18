import logging                              #Logging library
import pytest                               #Runs tests on application on run 

def totalArguements(allArguements):
    logging.info("Checking only 1 argument passed")
    if len(allArguements) != 3:
        logging.info(len(allArguements))
        logging.error("To run this application you need to pass one of 3 arguments: -g getHelp, -p partialSync or -f fullSync")
        return 0
    logging.info("1 Argument passed")
    return 1   

def executeTestStrategy(baseUserName, basePassword, consoleUserName, consolePassword, instanceInfo, userInfo):
    logging.info("Executing Test Strategy")
    #Arguments:
    baseArg = "--baseUrl=" + instanceInfo['application']['url']
    consoleArg = "--consoleUrl=" + instanceInfo['console']['url']
    iUserArg = "--iUser=" + baseUserName
    iPassArg = "--iPass=" + basePassword
    cUserArg = "--cUser=" + consoleUserName
    cPassArg = "--cPass=" + consolePassword

    userInfoArg = "--userInfo=" + str(userInfo)
    instanceArg = "--instanceInfo=" + str(instanceInfo)

    #Execute all tests:
    assert pytest.main([
        "-x", 
        "--tb=line", 
        "tests/checkObjectUnique.py", 
        "tests/correctStructure.py", 
        "tests/validJson.py", 
        "tests/testConnection.py", 
        baseArg, consoleArg, iUserArg, iPassArg, cUserArg, cPassArg, userInfoArg, instanceArg
    ]).value == 0          
