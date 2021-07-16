import requests
import logging
import json

def createAsset(baseUrl, userName, password, assetName, assetType, domainId, attributes, relations):
    """
    If attributes are passed, they are to be passed in the current format:
    [{
        "typeId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "value": "example"
    }]
    If no attributes are no be passed then pass an empty array
    """
    endpoint = "rest/2.0/assets"
    assetBody = {
        "name": assetName,
        "displayName": assetName,
        "domainId": domainId,
        "typeId": assetType
        }

    newAsset = requests.post(baseUrl + endpoint, json = assetBody, auth=(userName, password))
    logging.info(' Asset' + assetName + ' created completed with Code:' + str(newAsset.status_code))
    newAssetId = newAsset.json()['id']

    if len(attributes) != 0:
        for i in range(len(attributes)):
            attributes[i]['assetId'] = newAssetId
            addAttributes = requests.post(baseUrl + "rest/2.0/attributes/bulk", json = attributes, auth=(userName, password))
            logging.info(' Attribute' + str(attributes) + ' created completed with Code:' + str(addAttributes.status_code)) 
    return newAsset.json()

def createDomain(baseUrl, userName, password, domainName, domainType, communityId, description):
    endpoint = "rest/2.0/domains"
    domainBody = {
        "name": domainName,
        "communityId": communityId,
        "typeId": domainType,
        "description": description
        }

    newDomain = requests.post(baseUrl + endpoint, json = domainBody, auth=(userName, password))
    logging.info(' Domain: ' + domainName + ' created completed with Code:' + str(newDomain.status_code))      
    return newDomain.json()

def createCommunity(baseUrl, userName, password, parentCommunity, communityName, description):
    endpoint = "rest/2.0/communities"
    communityBody = {}

    #If the community is not a top level community:
    if parentCommunity == "none":
        communityBody = {
            "name": communityName,
            "description": description
            }

    else:
        communityBody = {
            "parentId": parentCommunity,
            "name": communityName,
            "description": description
            }
    newCommunity = requests.post(baseUrl + endpoint, json = communityBody, auth=(userName, password))
    logging.info(' Community: ' + communityName + ' created completed with Code:' + str(newCommunity.status_code))
    return newCommunity.json()