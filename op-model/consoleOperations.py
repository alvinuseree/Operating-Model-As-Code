import requests
import time
import logging

def restoreEnvironment(consoleUrl, userName, password, backupId, environmentId):
    jsonBody = {
        "dgcRestoreOptions": [
        "CONFIGURATION"
    ],
    "backupId": backupId
    }
    logging.info(' Restoring Cloud Backup (This could take a while) ...')
    jsonResponse = requests.post(consoleUrl + "rest/restore/" + environmentId, json = jsonBody, auth = (userName, password))

    while(True):
        pollDGC = requests.get(consoleUrl + "rest/environment", auth = (userName, password))
        if pollDGC.json()[0]['status'] == "RUNNING":
            logging.info(' Finished Restoring Backup')
            break
        time.sleep(30) # Wait for 30 seconds until next call
