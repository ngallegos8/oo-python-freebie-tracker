from .freebie import Freebie

class Company:

    all = []

    def __init__(self, name, founding_year):
        self.name = name
        self.founding_year = founding_year 
        Company.all.append(self)

    @classmethod
    def devs(self):
        pass

    @classmethod
    def freebies(self):
        pass

    @classmethod
    def give_freebie(self, dev, item_name, value):
        pass