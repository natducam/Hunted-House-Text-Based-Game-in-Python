
class player:
    def __init__(self):
        self.inventory = []
        self.hp = 5
        self.position = "BEDROOM"
        self.actions = {"HELP":"display list of commands",
                        "STATE":"display current character state",
                        "USE ~item~":"use the item (example: USE CLOSET)",
                        "TAKE ~item~":"put item in inventory (example: TAKE APPLE)"}
    
    def move(self,new_location):
        self.position = new_location
        return
    
    def take(self,thing):
        self.inventory.append(thing)
        return
    
    def consume(self,thing):
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

        self.apple_counter = 0

        # Defines the rooms that can be assesed from the starting location
        self.room_connections = {
            "BEDROOM":["HALLWAY"],
            "HALLWAY":["BEDROOM","MOM'S ROOM", "BATHROOM","LIVING ROOM"],
            "BATHROOM":["HALLWAY"],
            "LIVING ROOM":["HALLWAY","KITCHEN"],
            "KITCHEN":["LIVING ROOM","BASEMENT"]
        }

        self.room_descriptions = {
            "BEDROOM":"'My new bedroom is smaller than my old bedroom. I have a lamp and a new bed.\nI hear noises coming from my closet, mom doesn't believe me.'",
            "HALLWAY":"",
            "BATHROOM":"",
            "LIVING ROOM":"",
            "KITCHEN":"",
            "BASEMENT":""
        }

        # Defines the things that USE interacts with
        self.usable_things = {
            "BEDROOM":{"LAMP":["'It doesn't work...\nMaybe the power is out...'"],
                       "CLOSET":["~The monster wraps around you and pulls you into the darkness.\nNo one comes to save you.~",
                                "~TEDDY protects you.\nThe monster can't touch you.\nYou get LIGHTSABER~"],
                        "BED":["'I'm scared...\nI can't sleep...'"],}
        }

        # Defines the things that TAKE interacts with
        self.takeable_things = {
            "BEDROOM":{"TEDDY":["~A pink teddy bear.\nIt's missing an eye.~"]}
        }

    def get_connected_locations(self,current_location):
        for room, connections_list in self.room_connections.items():
            if room == current_location:
                return connections_list
        return False
    
    def display_description(self,current_location):
        for room, description in self.room_descriptions:
            if room == current_location:
                print(f"{description}\n")
    
    def validate_movement(self,current_location,new_location,inventory):
        for room, connections_list in self.room_connections.items():
            if room == current_location:
                for connection in connections_list:
                    if connection == "MOM'S ROOM":
                        print("'I'm not allowed to go in there...'")
                        return False
                    if connection == "BASEMENT":
                        if "KEY" in inventory:
                            return True
                        else:
                            print("'I don't have the key...'")
                            return False
                    if connection == new_location:
                        return True
                return False
        return False
    
    def use(self,current_position, usable_thing, inventory):
        for room,dictionary in self.usable_things.items():
            if room == current_position:
                for thing, description in dictionary.items():
                    if thing == usable_thing:
                        if thing == "CLOSET":
                            if "TEDDY" in inventory:
                                print(f"{description[1]}\n")
                                return "LIGHTSABER"
                            else:
                                print(f"{description[0]}\n")
                                return "GAME OVER"
                        else:
                            print(f"{description[0]}\n")
                        return 
                print(f"Can't USE {usable_thing}.\n")
                return
        print(f"Can't USE {usable_thing}.\n")
        return 
    
    def take(self,current_position,takeable_thing,inventory):
        if takeable_thing in inventory:
            print(f"{takeable_thing} is already in your inventory.\n")
            return False
        if takeable_thing == "APPLE":
            if self.apple_counter == 0:
                print(f"..........what?\n")
                self.apple_counter += 1
            elif self.apple_counter == 1:
                print(f"Ooohh... like from.... HELP...\nhaha... clever...\n")
                self.apple_counter += 1
            elif self.apple_counter == 2:
                print(f"Yeah, I get it.\nYou can actually play the game now.\n")
                self.apple_counter += 1
            elif self.apple_counter == 3:
                print(f"...\n")
                self.apple_counter += 1
            elif self.apple_counter == 4:
                print(f"Here, go have an apple.")
                return "GAME OVER"
            return False
        for room,dictionary in self.takeable_things.items():
            if room == current_position:
                for thing, description in dictionary.items():
                    if thing == takeable_thing:
                        print(f"{description[0]}\n")
                        return True
                print(f"Can't TAKE {takeable_thing}.\n")
                return False
        print(f"Can't TAKE {takeable_thing}.\n")
        return False   