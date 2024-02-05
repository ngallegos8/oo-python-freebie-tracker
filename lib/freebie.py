
class Freebie:
    
    all = []

    def __init__(self, item_name, value):
        self.item_name = item_name
        self.value = value
        Freebie.all.append(self)

    @classmethod
    def company(self):
        pass

    @classmethod
    def dev(self):
        pass

    @classmethod
    def print_details(self):
        pass

