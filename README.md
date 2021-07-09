# Operating Model As Code 
<img 
    src="https://img.shields.io/badge/Python-3.9.0-blue.svg" style="padding-bottom: 5px; float: left; margin-right: 5px">

<img 
    src="https://img.shields.io/badge/Beta-0.1-red.svg" style="padding-bottom: 5px;">

Operating Model as Code is a mechanism at which we can refresh and update the Kubrick **Collibra** Operating Model used for Data Management Cohorts in an automated and governed manner.

## Installation:
The Application comes with an associated requirements.txt file.

```cmd
pip install requirements.txt
```

## Executing:
### Help:
Run the following instruction for help:
```cmd
python op-model/op-model.py -g getHelp
```
### Full-Sync:
Run the following instruction to run a full synchronisation of the operating model:
```cmd
python op-model/op-model.py -f fullSync
```
### Partial-Sync:
Run the following instruction to not run a restore of the database and instead add content to your existing operating model:
```cmd
python op-model/op-model.py -p partialSync
```

## Tests:
On execution, the Application runs a series of tests before executing logic. These tests include:

* Test Folder Structure Correct and not Corrupted
* Test whether the Data Intelligence Cloud is running
* Test Credential to the Data Intelligence Cloud before and after restoration
* Test Credentials to the Console
* Confirm all config files contain valid JSON

## Files:


## To Do:

