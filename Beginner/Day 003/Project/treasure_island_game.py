print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
prompt_1 = input('''
The storm rages on, waves crashing against your ship. The crew waits anxiously for your command.: 
    Type "Anchor" or "Sails": ''').lower()

if prompt_1 == "sails":
    print('''
    You hoist the sails, and the ship surges forward, slicing through the storm. The island’s silhouette looms ahead.''')
    prompt_2 = input('''
You step onto the island. The air is thick with humidity, and strange sounds echo from the jungle. Two paths stretch before you.
    Type "Beach" or "Jungle": ''').lower()
    if prompt_2 == "jungle":
        print('''
    Twisting vines and thick foliage scratch at your arms, but you uncover markings pointing toward something valuable.''')
        prompt_3 = input('''
You stumble upon a dark cave hidden behind a waterfall. Inside, two tunnels lead in opposite directions.
    Type "Left" or "Right": ''').lower()
        if prompt_3 == "left":
            print('''
    The tunnel narrows, and you squeeze through. At the end, a treasure chest gleams in the faint light.''')
            prompt_4 = input('''
The chest is locked, and three keys lie before you: one rusty, one silver, and one golden. Your hand hovers over them.
    Type "Rusty" or "Silver" or "Golden": ''').lower()
            if prompt_4 == "golden":
                print('''
    The lock clicks open. Inside, gold coins and sparkling jewels spill out, a reward beyond your wildest dreams.
    Congratulations!
        ''')
            elif prompt_4 == "silver":
                print('''
    Game Over:
    The key fits perfectly, but opening the chest triggers a trap. Darts fly, and the air fills with poison.
                ''')
            else:
                print('''
    Game Over:
    The chest groans as the key turns. Suddenly, it explodes, and the treasure vanishes into smoke.
                ''')
        else:
            print('''
    Game Over:
    You follow the tunnel, but the air grows colder. A hidden pit swallows you before you can react.''')
    else:
        print('''
    Game Over:
    The soft sand feels safe, but the tide rises quickly. Before you can escape, the sea pulls you under.''')
else:
    print('''
    Game Over:
    The ship holds steady, but the storm grows fiercer. A massive wave capsizes the ship, pulling it to the depths.''')