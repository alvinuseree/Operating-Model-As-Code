from createObject import *

def generateOpmodel(baseUserName, basePassword, instanceInfo, userInfo, articleInfo, certInfo, exerciseInfo):
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
        "List of useful Articles"
    )['id']

    certsDomain = createDomain(
        instanceInfo['application']['url'],
        baseUserName,
        basePassword,
        "Certifications",
        certInfo['domain-uuid'],
        communityIds[0],
        "List of available certifications"
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
            userInfo['uuid'],
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