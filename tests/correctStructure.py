from pathlib import Path
import logging
import sys
import pytest
import os

def test_structure():
    foldersNeeded = set(['assets', 'config', 'tests'])
    allFiles = set(os.listdir(path='./'))
    logging.info("Confirming Directory is not Corrupted ...")
    
    if foldersNeeded.issubset(allFiles) == False:
        pytest.fail("Structure is corrupted, please download application again")
