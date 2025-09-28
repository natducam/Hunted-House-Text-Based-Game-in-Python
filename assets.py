
class player:
    def __init__(self):
        self.inventory = ["TEDDY"]
        self.hp = 5
        self.position = "MY BEDROOM"
        self.actions = ["USE","TAKE"]
    
    def move(self,new_location):
        self.position = new_location
        return
    
    def pick_up(self,thing):
        self.inventory.append(thing)
        return
    
    def use_thing(self,thing):
        if thing in self.inventory:
            self.inventory.remove(thing)
            return True
        return False
    
    def hurt(self,amount):
        self.hp =- amount
        if self.hp <= 0:
            return True #Dead
    
    def heal(self,amount):
        self.hp =+ amount
        if self.hp >= 5:
            self.hp = 5 #Max HP is 5
        return

    
class hunted_house:
    def __init__(self):
        self.room_connections = {
            "MY BEDROOM":["HALLWAY"],
            "HALLWAY":["MY BEDROOM","MOM'S BEDROOM", "BATHROOM","LIVING ROOM"],
            "BATHROOM":["HALLWAY"],
            "LIVING ROOM":["HALLWAY","KITCHEN"],
            "KITCHEN":["LIVING ROOM","BASEMENT"],
            "BASEMENT":["KITCHEN"]
        }

        self.interactable_setpieces = {
            "MY BEDROOM":["LAMP","CLOSET","BED","DOOR"]
        }

        self.interactable_things = {
            "MY BEDROOM":[""]
        }
    
    def validate_movement(self,current_location,new_location):
        for room, connections_list in self.room_connections.items():
            if room == current_location:
                for connection in connections_list:
                    if connection == new_location:
                        return True
                return False
        return False
    
    def eliminate_thing(self,current_location,thing_to_eliminate):
        for room, things_list in self.interactable_things.items():
            if room == current_location:
                for thing in things_list:
                    if thing == thing_to_eliminate:
                        return True
                return False
        return False