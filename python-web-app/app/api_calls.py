import hashlib, requests
from time import time
from flask import current_app as app
import json

PETFINDER_KEY = "?key=f7fd4a079087d6983fb59b20d691dac2"
WOLFRAMALPHA_APPID = "?appid=WGV8HX-VQG59UU468"

def get_adoptables_list():
    """
    This function get all the adoptable cats on petfinder, from their API.
    """
    api_base = "http://api.petfinder.com/pet.find" + PETFINDER_KEY
    api_tail = "&animal=cat&location=78705&count=1000&format=json"
    r = requests.get(api_base + api_tail)
    return r.json()

def get_breeds_list():
    """
    This function get all the breeds of cats on petfinder, from their API.
    """
    api_base = "http://api.petfinder.com/breeds.list" + PETFINDER_KEY
    api_tail = "&animal=cat&format=json"
    r = requests.get(api_base + api_tail)
    return r.json()

def get_organizations_list():
    """
    This function get all the organizations that shelter adoptable cats, from petfinder's API.
    """
    api_base = "http://api.petfinder.com/shelter.find" + PETFINDER_KEY
    api_tail = "&location=78705&format=json"
    r = requests.get(api_base + api_tail)
    return r.json()

def get_single_adoptable(adoptable_id):
    """
    This function gets a single adoptable cat's information, from petfinder's API.
    """
    api_base = "http://api.petfinder.com/pet.get" + PETFINDER_KEY
    api_tail = "&id=" + str(adoptable_id) + "&format=json"
    r = requests.get(api_base + api_tail)
    return r.json()

def get_single_breed(breed_name):
    """
    This function gets all the information we need on a breed, from Wolfram Alpha's API.
    The breed's name needs to have '%20' in place of its spaces.
    """
    # add '%20' as spaces for the name.
    api_base = "http://api.wolframalpha.com/v2/query" + WOLFRAMALPHA_APPID
    api_tail = "&input=" + breed_name + "(cat%20breed)&format=plaintext"
    r = requests.get(api_base + api_tail)
    return (api_base + api_tail)
