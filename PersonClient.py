import requests

import yaml


def getPersons():
    return yaml.safe_load(requests.get('http://localhost:5000/person').text)
