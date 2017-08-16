class ShopList(object):
    def __init__(self, items = None):
        self.items = []
    
    def add_item(self, items):
        self.items.append(items)
        return self.items

    def remove_item(self, items):
        if len(self.items) >= 0:
            self.items.remove(items)
            return self.items
        else:
            return 'You cant Remove Nothing'