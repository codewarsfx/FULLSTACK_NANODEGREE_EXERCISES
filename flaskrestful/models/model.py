
recipes_list = []

def get_id():
    if recipes_list:
        last_item = recipes_list[-1]
    else:
        return 1
    return last_item.id + 1
    


class Recipe():
    def __init__(self,name,description):
        self.id = get_id()
        self.name = name
        self.description = description
        self.isPublished = False
    
    def data(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "isPublished": self.isPublished
        }

