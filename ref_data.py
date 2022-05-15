import requests
import json

API_KEY = "d6975e3679e8c77e35b03a1ca10ba62c"
TOKEN = "6b3bd87a96bb21ee4d12e502a65307f96ab28920bca06e7bf891c864ad5930f3"
CURL_BASE = "https://api.trello.com/1/"
BOARD_ID = "62759b62341d150f74c03413"
LIST_IDS = {}

def get_list_ids(board_id):
    my_dict = {}
    my_url = CURL_BASE + "/boards/" + board_id + "/lists"

    jsonObj = {"key":API_KEY, "token":TOKEN,"id":BOARD_ID}
    lists = requests.request("GET", my_url, json = jsonObj)
    lists_info = json.loads(lists.text)
    
    for list in lists_info:
        my_dict[list['name']] = list['id']

    return my_dict

LIST_IDS = get_list_ids(BOARD_ID)

TEAM_LOGINS = {
    "Baxter" : "Baxter Gonzalez",
    "Sam" : "Sam Whitlock",
    "Kyle" : "Kyle Harris",
    "Alan" : "Alan Rendon",
    "Andrew" : "Andrew Bierbower",
    "Aprameya" : "aprameya sudharsan",
    "Carol" : "Carol Geng",
    "Jude" : "Jude Riojas",
    "Kayla" : "Kayla Spencer",
    "Wanjiru" : "Wanjiru Randolph"
}