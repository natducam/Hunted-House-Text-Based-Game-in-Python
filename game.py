from assets import player,hunted_house

def run():
    me = player()
    setting = hunted_house()
    print(f".......................................................\nHUNTED HOUSE\nActions: {me.actions}\n.......................................................\n")
    while True:
        print(f"Inventory: {me.inventory}\nHealth Points: {me.hp}\nLocation: {me.position}.")
        action = input("> ")

run()