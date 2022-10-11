from constants import CAT_API_KEY, CAT_API_URL, MEOW_API_URL
import requests

class Cat():
    # fetch img, fact, add as object properties
    def __init__(self):
        self.img = Cat.__get_img()
        self.fact = Cat.__get_fact()
    
    # set up class function to fetch img
    def __get_img():
        img = requests.get(CAT_API_URL, headers={'x-api-key': CAT_API_KEY})
        return img.json()[0]['url']

    # class function to fetch fact
    def __get_fact():
        fact = requests.get(MEOW_API_URL)
        return fact.json()['data'][0]
