import requests
import json
from ref_data import *

def find_cards_on_boards(list):
    my_cards = {}
    url = CURL_BASE + "/lists/" + LIST_IDS[list] + "/cards"
    
    #request all cards on a board
    jsonObj = {"key":API_KEY, "token":TOKEN, "id":LIST_IDS[list]}
    cards = requests.request("GET", url, json = jsonObj)
    cards_info = json.loads(cards.text)

    #requests id and all labels on each card. stores it in a dict of arrays
    for card in cards_info:
        #stores the id of the card...
        card_data = []
        card_data.append(card['desc'])

        #stores all labels on a card
        labels = card['labels']
        for label in labels:
            card_data.append(label['name'])
        my_cards[card['name']] = card_data

    print(my_cards)
    return my_cards
