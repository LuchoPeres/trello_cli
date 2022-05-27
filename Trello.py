import requests

class Trello():
    __module__ = 'trello'
    
    def __init__(self, apikey, token=None,id_board=None):
        self._apikey = apikey
        self._token = token
        self._id_board = id_board

    def raise_or_json(self, resp):
        resp.raise_for_status()
        return resp.json()
    #use the board id to return the board
    def get_board(self):
        resp = requests.get(f"https://trello.com/1/boards/{self._id_board}", params={"key": self._apikey, "token": self._token},data=None)
        return self.raise_or_json(resp)
    #returns all the lists on the board    
    def get_lists(self):
        resp = requests.get(f"https://trello.com/1/boards/{self._id_board}/lists", params={"key": self._apikey, "token": self._token},data=None)
        return self.raise_or_json(resp)
    #return all cards asociated with the list
    def get_cards(self,id_list):
        resp = requests.get(f"https://trello.com/1/lists/{id_list}/cards", params={"key": self._apikey, "token": self._token},data=None)
        return self.raise_or_json(resp)
    #delete the card of the given id
    def delete_card(self, id_card):
        resp = requests.delete(f"https://trello.com/1/cards/{id_card}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)
    #create new card in the provided list
    def new_card(self,id_list,name, desc=None):
        resp = requests.post(f"https://trello.com/1/lists/{id_list}/cards", params={"key": self._apikey, "token": self._token}, data={"name": name, "idList": id_list, "desc": desc,"idBoard":self._id_board})
        return self.raise_or_json(resp)
    #move card from list a to b
    #def move_card(self, id_list1,id_list2):
    #    return self.raise_or_json(resp)
    
    