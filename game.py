from assets import player,hunted_house

def display_state(me,setting):
    print(f"Location: {me.position}.\nConnected Locations:{setting.get_connected_locations(me.position)}\nInventory: {me.inventory}\nHealth Points: {me.hp}\n")
    return

def run():
    me = player()
    setting = hunted_house()
    print(f".......................................................\nHUNTED HOUSE\nActions: {list(me.actions.keys())}\n.......................................................\n")
    display_state(me,setting)
    while True:
        action = input("> ").upper().split(" ")
        print()
        if action[0] == "HELP":
            for key, value in me.actions.items():
                print(f"{key}: {value}")
            print()
        if action[0] == "STATE":
            display_state(me,setting)
        if action[0] == "USE":
            outcome = setting.use(me.position,action[1],me.inventory)
            if outcome == "GAME OVER":
                print(f".......................................................\nGAME OVER\n.......................................................\n")
                break
            elif outcome == "LIGHTSABER":
                me.take("LIGHTSABER")
        if action[0] == "TAKE":
            outcome = setting.take(me.position,action[1],me.inventory)
            if outcome == True:
                me.take(action[1])


run()