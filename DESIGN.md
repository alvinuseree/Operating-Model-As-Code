## Operating Model as Code
#REST-APIS 


| Navigation Table |
| ----------- |
|[Background](#Background)|
|[Governance](#Governance)|
|[Backup-Restore](#Backup-Restore)|
|[Metamodel](#Metamodel)|


#### Background:
When a new Data Management cohort starts their Collibra training, the instance needs to be refreshed.

This is done via a backup restore. However, this is a fresh instance and the consultants are asked to build personal communities for themselves as they learn more about Collibra.

To bring a more personalised experienced to the training and establish more familiarity with Collibra, we are suggesting:
* Creating personalised communities for each consultant

and embedding:
* All the exercises
* Training material
* Project briefs
* Consultant submissions
* Assessments
 
in Collibra.

In addition to a personalised experience, we need a means of adding additional information to the training operating model as the platform continues to evolve. 

If we did this via a backup restore, this would need us to

* First restore to the clean version
* Add the new content
* Take a backup

For EACH change - this is not particularly scalable.

#### Problem Statement:
A personalised experience for each consultant cannot be acheived using a Backup Restore.

A more automated approach towards the spinning up of an operating model for each cohort is required.

In addition to this, a scalable approach whereby we scan content  from a repository we regularly add to is required to cater to scalability.

#### Governance:
Re: [[21-06-2021 Martin]], we can add a certain level of governance over changes that get made to the collateral.

E.g:

* Changes can be added as branches of the code base
* Committed to Default branch via Pull Request
* Add checks on the Request

You would also get a complete audit trail of changes over time.

#### Backup-Restore:
A backup-restore is still required so we have a starting point to build on.

A Python module that triggers the restoration then polls the console API to confirm once the restore is finished is required.

#### Metamodel:
##### Users:
A file containing all the users to be added is required. We'll align usernames to principal names in Azure (firstlastname@kubrickgroup.com)

**Global Roles:**
Upon creation, each user will need to be given the relevant roles to complete their Tasks during the training.

* **Consultant:**
A consultant by default will not have the ability to edit the metamodel.

* **Trainer:**
All trainers will be added to sysAdmin User Group.

##### Communities:
**Consultant Communities:**
* Top level communities are needed that will be named after the consultants

**Documentation Communities:**
* Another Top level community will be needed to house articles and other content we want to advertise on the instance

**Configurations:**
* This is a community that will house all metadata pertaining to configuration of the operating model 

##### Resource Roles:
Each user will be assigned as Owner of their respective community to allow them to update content in said community.

Each consultant will also be owner of a Profile Asset which will allow consultants to track their progress as well as holding a configurations JSON body which will indicate what exercises, project etc belong to each consultant.
##### Domains:
**Exercises:**
* A domain to house exercises is required
* Only the consultant should be able to edit content here
* An instance of an exercise domain is needed in each consultant's community

**Profiles Domain**
* Domain to house User Profiles
* Only sysAdmins and workflows should be able to edit these
* Only 1 Profile Domain should exist in the configurations community
##### Assets & Asset Types:
**Exercise:**
**Project:**
**Profile:**
**Articles:**
**Certification Paths:**

#### Workflows:


#### Configurations:

#####




