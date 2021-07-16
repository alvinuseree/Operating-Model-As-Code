from pathlib import Path
import logging
import sys
import json
import pytest
import os

def test_checkAllFiles_valid():
    #Only contain 2 sub folders with json files:
    directories = ['assets', 'config']
    for folder in directories:
        Files = os.listdir(path='./' + folder)
        for file in Files:
            with open(folder + "/" + file) as jsonFile:
                if os.path.getsize(folder + "/" + file) > 0:
                    logging.info("Checked: " + file)
                    try:
                        jsonObject = json.load(jsonFile)
                        jsonFile.close()
                    except ValueError as e:
                        pytest.fail(file + " has invalid Json ...")