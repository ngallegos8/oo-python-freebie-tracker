from .freebie import Freebie

class Dev:
    
    all = []

    def __init__(self, name):
        self.name = name

    @classmethod
    def companies(self):
        pass

    @classmethod
    def freebies(self):
        pass

    @classmethod
    def recieved_one(self, item_name):
        pass

    @classmethod
    def give_away(self, dev, freebie):
        pass