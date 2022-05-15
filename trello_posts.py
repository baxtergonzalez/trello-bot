import requests
import json
from ref_data import *

class Card:
    url = CURL_BASE + "cards"

    def __init__(self, name, description, board):
        self.name = name
        self.description = description
        self.list_id = LIST_IDS[board]
        self.checklist_ids = {}
        self.labels = {}
    #create new card
    def build_card(self):
        jsonObj = {"key":API_KEY,"token":TOKEN,"idList":self.list_id, "name":self.name, "desc":self.description}
        
        #create a new card and store the id as attribute in this card object
        new_card = requests.post(Card.url, json = jsonObj)
        new_card_info = json.loads(new_card.text)
        self.card_id = new_card_info["id"]
        print(f"My id is: {self.card_id}")
    def add_checklist(self, list_name, items):
        jsonObj = {"key":API_KEY,"token":TOKEN,"idCard":self.card_id, "name":list_name}
        
        #create a new cecklist and store the id as an attribute in the card object
        new_list = requests.post(CURL_BASE + "checklists", json = jsonObj)
        new_list_info = json.loads(new_list.text)
        self.checklist_ids[list_name] = new_list_info['id']
        print(f"List: {list_name} created\n")

        #add the items to the previously created checklist
        checklist_url = CURL_BASE + "checklists/" + self.checklist_ids[list_name] + "/checkItems"
        for item in items:
            jsonObj = {"key":API_KEY, "token":TOKEN,"id":self.checklist_ids[list_name], "name":item, "checked":False}
            new_item = requests.post(checklist_url, json = jsonObj)
            print(f"Item: {item} created...\n")