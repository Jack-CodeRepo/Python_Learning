#!/usr/bin/env python
# coding: utf-8
# ==================================================================================================



# ==================================================================================================
#   IMPORT
# ==================================================================================================

import json



# ==================================================================================================
#   VARIABLES GLOBALES
# ==================================================================================================
save_file="test.json"

player = "jacques"
new_player = "Bob".lower()

with open(save_file) as f:
    data = json.load(f)



# ==================================================================================================
#   FONCTIONS
# ==================================================================================================

def write_json():
    with open(save_file, "w") as f:
        json.dump(data, f, indent=4)



def check_player(player):
    if player in data["players"]:
        score = data["players"][player]
        return "{} is {}".format(player, score)
    else:
        return f"Player {player} not found"



def change_score(player, score):
    if player in data["players"]:
        data["players"][player] = score

    write_json()



def add_player(player):
    pName = player.lower()
    if pName not in data["players"]:
        score = "10"
        temp = data["players"]
        added_data = {player: score}
        
        temp.update(added_data)

        write_json()

    else:
        print("Player already exists")



def delete_player(player):
    pName = player.lower()
    if pName in data["players"]:
        del data["players"][pName]

        write_json()



# ==================================================================================================
#   SCRIPT
# ==================================================================================================

print(check_player(player))
change_score(player, "10")
print(check_player(player))

print()

print(check_player(new_player))
add_player(new_player)
print(check_player(new_player))


print()
delete_player(new_player)
print(check_player(new_player))