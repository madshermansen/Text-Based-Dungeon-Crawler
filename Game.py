# Name: Mads
# Date: 05/01/19
# Description: Epic Dungeon adventure with determining if you will escape or not.

import random
import time


# ---------------------------------------------------------------#

# Introduction

def DisplayIntroduction():
    print("You wake up in a cold cold dungeon, and before you appear a dark siluette in the figure of a young boy or a woman")
    print("as your vision slowly appears. You try talking to the figure but it doesnt respond or look your way.")
    time.sleep(3)
    print("Then you pass out...")
    print()
    time.sleep(3)
    print("You wake up with a message carved in the wall.")
    print()
    print("YOU HAVE MESSED WITH DPU.")
    time.sleep(0.5)
    print("A PUNISHMENT WILL BE BROUGHT")
    time.sleep(0.5)
    print("UPON YOU, UNLESS YOU ESCAPE")
    time.sleep(0.5)
    print("THIS DUNGEON")
    time.sleep(3)


# ---------------------------------------------------------------#

# Choosing Path

def choosepath():
    path = ""
    while path != "1" and path != "2":  # Checking for the input
        path = input("Which path will you take? 1 or 2?: ")

    return path


# ---------------------------------------------------------------#

def StartMaze():
    print("Room " + str(Count + 1))
    print()
    print("1: Left")
    print("2: Forward")
    print("3: Right")
    print("4: Down")
    print()
    Path = input("Which door do you want to go through?: ")
    print()
    if Path == AnswerKey:
        print("You walk through the door")
        return (Count + 1)
    else:
        print("You walk in the wrong door. and head back to the start of the maze")
        return (0)


# ---------------------------------------------------------------#

HP = 20
NegativeHP = 0
GoblinHP = 6
ChildGoblinHP = 4


def LoseHP():
    print("Save Text = You have lost some HP")
    print("You have lost " + str(NegativeHP) + (" HP"))


DrinkPotion = ""

# Play again function


# playagain = "yes"
# while playagain == "yes" or playagain == "y":
#    DisplayIntroduction()
#    choice = choosepath()
#    checkpath(choice)
#    playagain = input("Do you want to play again? type yes or y to continue playing: ")


Threats = (
    ["Ill beat you silly!", "You're just a mere mortal! Get out of my sight", "What if i turn you into a toaster!",
     "I'll beat you in chess!", "You are a rump-faced ape!", "Im not insulting you, im describing you",
     "You are'nt invited to my birthday party anymore!", "Go sit on a pinecone", "Who's this clown", ])
DragonAttacks = (["Spits a ball of fire at", "Swipes its claws at", "Blows fire at", "Flies up and drops down on"])
Attacks = (["Slice", "Stab", "Pummel", "Riposte"])
MeleeAttacks = (["Punch", "Kick", "Headbutt", "Throw rock"])
RNGBeastAttacks = (["Punch", "Swings at", "Headbutts", "Stomps on"])
GoblinAttacks = (["hits", "throws a rock at", "spits on", "jumps on your head and smacks"])
NumbersCode = (["1", "2", "3", "4", "5", "6", "7", "8", "9"])
NormalWeaponList = ["Bow", "Shiv", "Iron Sword"]
NormalWeaponDamage = [[10, 30],[6, 19],[12, 32]]
NormalWeaponAttacks = [["Shoot","Throw arrow"],["Stab","Slice","Ninjutsu kunai attack"],["Slice","Stab","Pummel","Riposte"]]

##############################################################

# Run Game #

##############################################################

# If want specific place change to 0 and change      if Gamerule_PlayGame == 1:      to      if Gamerule_PlayGame == 0:

YouWin = ("""__  ______  __  __   _       _______   ____
\ \/ / __ \/ / / /  | |     / /  _/ | / / /
 \  / / / / / / /   | | /| / // //  |/ / / 
 / / /_/ / /_/ /    | |/ |/ // // /|  /_/  
/_/\____/\____/     |__/|__/___/_/ |_(_)   
                                           """)
YouLose = ("""__  ______  __  __   __    ____  _____ ________
\ \/ / __ \/ / / /  / /   / __ \/ ___// ____/ /
 \  / / / / / / /  / /   / / / /\__ \/ __/ / / 
 / / /_/ / /_/ /  / /___/ /_/ /___/ / /___/_/  
/_/\____/\____/  /_____/\____//____/_____(_)   
                                               """)

Gamerule_PlayGame = 1

##############################################################
# Start Game

if Gamerule_PlayGame == 1:
    playagain = "yes"
    while playagain == "yes" or playagain == "y" or playagain == "Y" or playagain == "Yes" :
        # Variables
        Dice1 = 0
        Dice2 = 0
        DragonHP = 50000
        Count = 0
        HP = 20
        NegativeHP = random.randint(1, 2)
        GoblinHP = 6
        ChildGoblinHP = 4
        FutureKey = 0
        KeyA = 0
        KeyB = 0
        RandomPotionRNG = 0
        ChestRandomKey = 0
        KeyBDoor = 0
        MazeDoor = "0"
        MazeFinish = 0
        AnswerKey = "0"
        Dice = 0
        RNGBeastHP = 200
        PreDragonHP = 100
        RandomDragonDamage = 0
        Lever1 = 10
        Lever2 = 10
        Lever3 = 10
        Lever4 = 10
        Lever5 = 10
        Weapon = "Placeholder weapon"
        # Gamerule Functions
        Gamerule_PreDragonFight = 0
        Gamerule_DragonFight = 0
        Gamerule_PlayGame = 1
        Gamerule_StartIntro1 = 0
        Gamerule_Dungeon = 0
        Gamerule_KeyADoor = 0
        Gamerule_KeyFinder = 0
        Gamerule_Start_MazeDoor = 0
        Gamerule_Start_MazeDoor2 = 0
        Gamerule_CorridorDamage = 0
        Gamerule_CorridorDamage2 = 0
        Gamerule_OutsideDoor1 = 0
        Gamerule_Trapdoor = 0
        Gamerule_Stealth = 0
        Gamerule_FallBackSpawn = 0
        Gamerule_MagicDoor = 0
        Gamerule_RNGEnding = 0
        Gamerule_RNGEnding2 = 0
        Gamerule_TeleportCube = 0
        Gamerule_TeleportOrb = 0
        Gamerule_HallwayEscape = 0
        Gamerule_HallwayEscape2 = 0
        Gamerule_DPUEnding = 0
        Gamerule_Trapped = 0

        # Start Game

        if Gamerule_PlayGame == 1 or Gamerule_StartIntro1 == 1:
            DisplayIntroduction()
            print()
            print("1: You stand up, you see that the wall is old and has a large crack running through it.")
            print("2: You also see that the door is slightly ajar and could be pushed open")
            print()
            time.sleep(5)
            choice = choosepath()
            if choice == "1":
                print("You try pulling open the crack but nothing happens")
                print("You decide to run at the wall breaking it open but getting hurt")
                print()
                time.sleep(3)
                HP = (HP - NegativeHP)
                print ("You now have " + str(HP) + "HP")
                print()
                print("There is a hollow room on the other side of the wall")
                WallBreak = random.randint(1, 2)
                time.sleep(3)
                if WallBreak == 1:
                    print("There is a statue that casts a blessing on you")
                    print("As you walk out of the room you start to feel more refreshed")
                    print("HP +1")
                    HP = HP + 1
                    print("You walk back and decide to go the other way")
                    choice = "2"
                else:
                    print("There is a door that leads to stairs going furthur down the dungeon")
                    Enter = input("Do you want to go furthur down? y or n: ")
                    if Enter == "n":
                        print("You walk back and decide to go the other way")
                        choice = "2"
                    elif Enter == "y":
                        Gamerule_Dungeon = 1
                    else:
                        choice = "2"
                        print("You walk back and decide to go the other way")

                    # Player decides to go back into main room
            if choice == "2":
                print("You push the door open and slowly walk out, you see five different rooms and a small door")
                print("1: A small room with a slanted door.")
                print("2: A basic prison cell")
                print("3: A basic prison cell")
                print("4: A basic prison cell")
                print("5: A more luxiorius room with paintings on the wall")
                print("6: A small door leading somewhere unknown")
                Path = ""
                while Path != "1" and Path != "2" and Path != "3" and Path != "4" and Path != "5" and Path != "6":
                    Path = input("Which path do you want to take?: ")
                if Path == "1":
                    Weapon = NormalWeaponList[0]
                    Attacks = NormalWeaponAttacks[0]
                    Damage = NormalWeaponDamage[0]
                    print("You find a bow and pick it up")
                    print("You also see arrows on the ground and pick them up as well")
                    print("You walk out of the room and see a gaurd, you run to the other side of the hallway")
                    Gamerule_HallwayEscape = 1
                if Path == "2":
                    WallBreak = random.randint(1, 2)
                    if WallBreak == 1:
                        print("You don't find anything and walk back out")
                        print("You walk out of the room and see a gaurd, you run to the other side of the hallway")
                        Gamerule_HallwayEscape = 1
                    if WallBreak == 2:
                        print("You see a door leading to a room and decide to walk in")
                        print("You walk out of the room and see a gaurd, you run to the other side of the hallway")
                        Gamerule_Start_MazeDoor2 = 1
                        print("You open the door and you are at the start of a maze")
                if Path == "3":
                    print("You search the room and find a shiv hidden in the corner")
                    print("You pick it up and put it into your pocket")
                    Weapon = NormalWeaponList[1]
                    Attacks = NormalWeaponAttacks[1]
                    Damage = NormalWeaponDamage[1]
                    print("You walk out of the room and see a gaurd, you run to the other side of the hallway")
                    Gamerule_HallwayEscape = 1
                if Path == "4":
                    print("You look around the room and don't find anything")
                    print("You walk out of the room and see a gaurd, you run to the other side of the hallway")
                    Gamerule_HallwayEscape = 1
                if Path == "5":
                    Attacks = NormalWeaponAttacks[2]
                    Weapon = NormalWeaponList[2]
                    Damage = NormalWeaponDamage[2]
                    print("You find a Iron sword hung on the wall along with a potion")
                    WallBreak = ""
                    while WallBreak != "yes" and WallBreak != "Yes" and WallBreak != "no" and WallBreak != "No" and WallBreak != "y" and WallBreak != "Y" and WallBreak != "n" and WallBreak != "N":
                        WallBreak = input("Do you want to drink the potion?: ")
                    if WallBreak == "yes" or WallBreak == "Y" or WallBreak == "Yes" or WallBreak == "yes":
                        print("You drink the potion and feel bad")
                        HP = HP - 3
                        print("You lost 3 HP Drinking the potion, you now have " + str(HP))
                        print("You walk out of the room and see a gaurd, you run to the other side of the hallway")
                        Gamerule_HallwayEscape = 1
                    else:
                        print("You pick up the sword and leave")
                        print("You walk out of the room and see a gaurd, you run to the other side of the hallway")
                        Gamerule_HallwayEscape = 1
                if Path == "6":
                    print("You find a strange looking device and pick it up")
                    FutureKey = 1
                    print("You walk out of the room and see a gaurd, you run to the other side of the hallway")
                    Gamerule_HallwayEscape = 1

            if Gamerule_HallwayEscape == 1:
                print("You walk into a big white room, you see a ")
                print("1: White door with no handle")
                print("2: A old wooden door with cracks in it leading to a hallway")
                Path = ""
                while Path != "1" and Path != "2":
                    Path = input("Which path do you want to take?: ")
                if Path == "1":
                    if FutureKey == 1:
                        print("You walk into the room and see a white box")
                        print("You walk close to the box and the strange artifact starts moving")
                        print("The artifact flies out of your pocket and sticks to the box")
                        print("The box slowly disappears and you see a strange looking device")
                        print("The device has some letters bellow it")
                        print()
                        print("DPU")
                        print()
                        Path = ""
                        while Path != "Y" and Path != "y" and Path != "n" and Path != "N":
                            Path = input("Do you want to touch the device? (Y/N): ")
                        if Path == "y" or Path == "Y":
                            print("You touch the device and the screen starts flashing")
                            Gamerule_DPUEnding = 1
                        if Path == "N" or Path == "n":
                            Gamerule_HallwayEscape2 = 1
                            print("You decide to walk out of the room and take the wooden door")
                    if FutureKey == 0:
                        print("You walk into the room and see a white box")
                        print("You walk closer and nothing happens")
                        print("You decide to walk out of the room and take the wooden door")
                        Gamerule_HallwayEscape2 = 1
                elif Path == "2":
                    Gamerule_HallwayEscape2 = 1
                    print("You open the door and walk along the hallway to another door and open it")

            if Gamerule_DPUEnding == 1:
                print("It flashes three images")
                print("")
                time.sleep(0.1)
                print("DIGITAL")
                time.sleep(0.1)
                print("PROCESSING")
                time.sleep(0.1)
                print("UNIT")
                print("")
                time.sleep(0.5)
                print("The room starts disappearing slowly along with the rest of the dungeon")
                print("You are standing in a empty area with nothing")
                print("You float in the air and stand still")
                print("Slowly a man with a black cloak walks up to you")
                time.sleep(1)
                print("")
                print("based")
                print("")
                time.sleep(2)
                print(YouWin)

            if Gamerule_HallwayEscape2 == 1:
                print("You come into another hallway where you see two dice on a table")
                print("You see a note and read it")
                print("")
                print("Different roles will treat you well")
                print("Some might send you to hell")
                print("A four is a treat good as day")
                print("A seven might send you away")
                print("An eleven might also give you a gift")
                print("But a perfect double six will help you continue your quest")
                while Dice1 + Dice2 != 12:
                    print("")
                    Path = ""
                    while Path != "y" and Path != "Y":
                        Path = input("Roll dice?(Saying no wont do anything)y/Y: ")
                    print("You roll the dice")
                    Dice1 = random.randint(1,6)
                    Dice2 = random.randint(1,6)
                    print("You land a " + str(Dice1) + " and a " + str(Dice2))
                    print("")
                    if Dice1 + Dice2 == 4:
                        print()
                        print("You feel a divine spirit give you power")
                        print("Your HP has gone up by 5")
                        print("")
                        HP = HP + 5
                        print("You now have " + HP + " HP")
                        print("")
                    if Dice1 + Dice2 == 7:
                        print("A Goblin appears and starts attacking you")
                        GoblinHP = 30
                        while GoblinHP > 0 and HP > 0:
                            print()
                            print("The goblin says " + random.choice(Threats))
                            RandomGoblinDamage = random.randint(3, 5)
                            print("The goblin " + random.choice(GoblinAttacks) + " you for " + str(RandomGoblinDamage) + " HP")
                            HP = HP - RandomGoblinDamage
                            print()
                            print("You now have " + str(HP) + " HP")
                            print()
                            print(Attacks)
                            print()
                            Attack = ""
                            while not(Attack in Attacks):
                                Attack = input("What attack do you want to use?")
                            print("You " + Attack + " the enemy")
                            print("You use your " + Weapon + " and deal " + str(random.randint(Damage[0],Damage[1])) + " damage")
                            GoblinHP = GoblinHP - random.randint(Damage[0], Damage[1])
                            print("")
                            print("The goblin now has " + str(GoblinHP) + " HP left")
                            print("")
                    if Dice1 + Dice2 == 10:
                        print()
                        print("You feel a divine spirit give you power")
                        print("Your HP has gone up by 5")
                        print("")
                        HP = HP + 5
                        print("You now have " + HP + " HP")
                        print("")
                print("You roll a twelve and a door opens")
                print("You expect a fight...")
                print("Nothing ever comes and you stay in the room")
                print("Then you hear a loud roar")
                print("")
                print("I am the goblin king! And you do not belong here!")
                GoblinHP = 50
                while GoblinHP > 0 and HP > 0:
                    print()
                    print("The goblin says " + random.choice(Threats))
                    RandomGoblinDamage = random.randint(4, 6)
                    print("The goblin " + random.choice(GoblinAttacks) + " you for " + str(RandomGoblinDamage) + " HP")
                    HP = HP - RandomGoblinDamage
                    print()
                    print("You now have " + str(HP) + " HP")
                    print()
                    print(Attacks)
                    print()
                    Attack = ""
                    while not (Attack in Attacks):
                        Attack = input("What attack do you want to use?")
                    print("You " + Attack + " the enemy")
                    print(
                        "You use your " + Weapon + " and deal " + str(random.randint(Damage[0], Damage[1])) + " damage")
                    GoblinHP = GoblinHP - random.randint(Damage[0], Damage[1])
                    print("")
                    print("The goblin now has " + str(GoblinHP) + " HP left")
                    print("")
                # Player chooses to go into the dungeon

            if Gamerule_Dungeon == 1:
                print()
                print("You walk down the staircase not knowing what you will find")
                print("You walk down the stairs slowly to get ready for what you will find.")
                print("You come into a big empty room...")
                print("Then the door closes behind you.")
                print()
                print("A small goblin appears and screams at you.")
                print()
                print("MY NAME IS GABRIEL AND YOU SHALL NOT PASS - in a very squeaky and weak voice")

                while GoblinHP > 0:
                    print()
                    print("The goblin says " + random.choice(Threats))
                    RandomGoblinDamage = random.randint(1, 2)
                    print("The goblin " + random.choice(GoblinAttacks) + " you for " + str(RandomGoblinDamage) + " HP")
                    HP = HP - RandomGoblinDamage
                    print()
                    print("You now have " + str(HP) + " HP")
                    print()
                    print(MeleeAttacks)
                    print()
                    MeleeAttack = ""
                    while not(MeleeAttack in MeleeAttacks):
                        MeleeAttack = input("What attack do you want to do?: ")
                    RandomDamage = random.randint(2, 3)
                    print("You used " + str(MeleeAttack) + " and did " + str(RandomDamage) + " to the goblin")
                    GoblinHP = GoblinHP - RandomDamage
                    print("The goblin now has " + str(GoblinHP) + " HP left")
                    print()
                print()
                print("The goblin has died and dropped a rusty sword, as you pick it up another goblin jumps out")
                print("MY NAME IS NAKSUNN AND I WILL AVENGE DADDY GABRIEL")
                print()
                while ChildGoblinHP > 0:
                    print()
                    print("The goblin says " + random.choice(Threats))
                    RandomGoblinDamage = 1
                    print("The goblin " + random.choice(GoblinAttacks) + " you for " + str(RandomGoblinDamage) + " HP")
                    HP = HP - RandomGoblinDamage
                    print()
                    print("You now have " + str(HP) + " HP")
                    print()
                    print(Attacks)
                    print()
                    Attack = ""
                    while Attack != "Slice" and Attack != "Pummel" and Attack != "Stab" and Attack != "Riposte":
                        Attack = input("What attack do you want to do?: ")
                    RandomDamage = random.randint(2, 3)
                    print("You used " + str(Attack) + " and did " + str(RandomDamage) + " to the goblin")
                    ChildGoblinHP = ChildGoblinHP - RandomDamage
                    print("The goblin now has " + str(ChildGoblinHP) + " HP left")
                    print()
                DrinkPotion = ""
                while DrinkPotion != "y" and DrinkPotion != "n":
                    DrinkPotion = input("Do you want to drink the potion?(30% to poison you) y or n?: ")
                RandomPotionRNG = random.randint(1, 10)
                if RandomPotionRNG == 1 or RandomPotionRNG == 2 or RandomPotionRNG == 3:
                    HP = HP - 2
                    print("You drank something icky and took some damage")
                else:
                    HP = HP + 5
                    print("The potion healed you for 5 HP")
                print("You now have " + str(HP) + " HP")
                print()
                print("You see three doors")
                print("1: One Giant door with a lever to open it")
                print("2: Another door that is open and has a chest in it")
                print("3: And a third room that is locked and needs a key to open")
                print()
                Path = ""
                while Path != "1" and Path != "2" and Path != "3":
                    Path = input("Which door do you want to open? 1, 2 or 3: ")
                    print()
                if Path == "3":
                    Gamerule_KeyADoor = 1
                if Path == "2":
                    Gamerule_KeyFinder = 1
                if Path == "1":
                    Gamerule_Start_MazeDoor = 1

            # Different doors, Key, Maze, Find Key.

        if Gamerule_KeyFinder == 1:
            print("You walk into the room where the door closes behind you")
            print("You walk next to the chest hesitating to open it")
            ChestRandomKey = random.randint(1, 4)
            if ChestRandomKey == 1:
                print()
                print("You open the chest after waiting a while and find a key")
                print("You look at the key and wonder what to do with it")
                KeyB = 1
            else:
                print()
                print("You open the chest after waiting a while and find a key")
                print("You look at the key and wonder what to do with it")
                KeyA = 1
            print("You turn to your left and see a door that needs a key to open")
            KeyBDoor = 0
            while KeyBDoor != "Yes" and KeyBDoor != "No" and KeyBDoor != "yes" and KeyBDoor != "no":
                KeyBDoor = input("Do you try opening the door?: ")
            if KeyBDoor == "Yes" or KeyBDoor == "yes":
                if KeyB == 1:
                    print("The key slides in and you open the door with ease and you walk in")
                    Gamerule_MagicDoor = 1
                else:
                    print("You try putting the key in but it doesnt fit")
                    print("You decide to walk back")
                    print()
                    print("1: You see one Giant door with a lever to open it")
                    Path = ""
                    while Path != "1":
                        Path = input("Which door do you want to open? 1: ")
                    print()
                    if Path == "1":
                        Gamerule_Start_MazeDoor = 1

            if KeyBDoor == "No" or KeyBDoor == "no":
                print("You decide to walk back")
                print()
                print("1: You see one Giant door with a lever to open it")
                print("2: And a third room that is locked and needs a key to open")
                Path = ""
                while Path != "1" and Path != "2":
                    Path = input("Which door do you want to open? 1 or 2: ")
                print()
                if Path == "2":
                    Gamerule_KeyADoor = 1
                if Path == "1":
                    Gamerule_Start_MazeDoor = 1

        if Gamerule_KeyADoor == 1:
            print("1")
            if KeyA == 1:
                print("You open the door with ease, the key slides in and you walk in.")
                print("There is a long hallway lit with candles, you walk down it not thinking about anything")
                print("1: You see a small corridor that you could fit in if you pushed yourself very hard.")
                print(
                    "2: You also see a vent like system that you could easily crawl through but would need to push yourself")
                print()
                Path = ""
                while Path != "1" and Path != "2":
                    Path = input("Where do you want to go? 1 or 2: ")
                if Path == "1":
                    print()
                    Gamerule_CorridorDamage = 1
                if Path == "2":
                    print()
                    Gamerule_OutsideDoor1 = 1


            elif KeyA == 0:
                Path = ""
                print("It seems you do not have a key so you cannot open the door.")
                while Path != "1" and Path != "2":
                    Path = input("Which door do you want to open? 1, or 2: ")
                if Path == "2":
                    Gamerule_KeyFinder = 1
                    Gamerule_KeyADoor = 0
                if Path == "3":
                    Gamerule_Start_MazeDoor = 1
                    Gamerule_KeyADoor = 0

        if Gamerule_MagicDoor == 1:
            print()
            print("You walk into a room where a mystical power fills your body.")
            print("1: You see a blue vortex that holds immense power and you can enter")
            print("2: There is also a door leading into a dark alley")
            print("3: You could also walk back and save yourself from any harm")
            Path = 0
            while Path != "1" and Path != "2" and Path != "3":
                Path = input("Where do you want to go?: ")
            if Path == "1":
                print()
                Gamerule_TeleportCube = 1
            if Path == "2":
                print()
                Gamerule_CorridorDamage = 1
            if Path == "3":
                print()
                print("You decide to walk back")
                print()
                print("1: You see one Giant door with a lever to open it")
                print("2: And a third room that is locked and needs a key to open")
                Path = ""
                while Path != "1" and Path != "2":
                    Path = input("Which door do you want to open? 1 or 2: ")
                print()
                if Path == "2":
                    Gamerule_KeyADoor = 1
                elif Path == "1":
                    Gamerule_Start_MazeDoor = 1
        if Gamerule_TeleportCube == 1:
            print("You touch the vortex and feel worse")
            print("You start feeling powerful and suddenly you black out")
            print("You wake up and see different things")
            print("1: You see a gate that you can slide open with a pulley system")
            print("2: You see a door that is made from shiny black metals")
            while Path != "1" and Path != "2":
                Path = input("Which path do you want to take")
            if Path == "1":
                print("You pull on the rope slowly opening the door")
            if Path == "2":
                print("You open the door slowly and walk inside, The door slams shut when you walk in")
                Gamerule_DragonFight = 1

        if Gamerule_Start_MazeDoor == 1:
            print()
            print("You see two doors and a dead end.")
            print("1: The door is small and looks very old")
            print("2: The door is giant and has a lever to open it. It is atleast 2 times bigger than you")
            Path = ""
            while Path != "1" and Path != "2":
                Path = input("Which door do you want to open? 1 or 2: ")
                print()
                if Path == "1":
                    Gamerule_RNGEnding = 1
                if Path == "2":
                    Gamerule_Start_MazeDoor2 = 1
                    print("You pull the lever causing the door to slowly open.")
                    print("In front of you there are three doors")
                    print("On the wall there is some writing")
                    print()
                    print("THE ESCAPE YOU SEEK WILL BE FOUND")
                    print("SOME OF THE DOORS YOU PICK WILL GET")
                    print("YOU HONE SAFE AND SOUND")
                    print()

        if Gamerule_RNGEnding == 1:
            print()
            print("There is a seven sided dice in the room. Do you roll it?")
            while Dice != "yes" and Dice != "y" and Dice != "no" and Dice != "n":
                Dice = input("Roll the dice, y or n?: ")
            if Dice == "yes" or Dice == "y":
                Dice = random.randint(1, 7)
                if Dice == 7:
                    print()
                    print("You roll a 7, a hidden door reveals itself and you walk in")
                    Gamerule_RNGEnding2 = 1
                else:
                    Gamerule_Start_MazeDoor2 = 1
                    print()
                    print("Your rolled a " + str(Dice) + ". Nothing happened.")
                    print("You decide to walk back to the door with a lever")
                    print()
                    print("You pull the lever causing the door to slowly open.")
                    print("In front of you there are three doors")
                    print("On the wall there is some writing")
                    print()
                    print("THE ESCAPE YOU SEEK WILL BE FOUND")
                    print("SOME OF THE DOORS YOU PICK WILL GET")
                    print("YOU HONE SAFE AND SOUND")
                    print()

            if Dice == "no" or Dice == "n":
                Gamerule_Start_MazeDoor2 = 1
                print("You walk back into the corridor and pull the leaver causing the door to slowly open")
                print("In front of you there are three doors")
                print("On the wall there is some writing")
                print()
                print("THE ESCAPE YOU SEEK WILL BE FOUND")
                print("SOME OF THE DOORS YOU PICK WILL GET")
                print("YOU HONE SAFE AND SOUND")
                print()

        if Gamerule_RNGEnding2 == 1:
            print("You walk into the hidden room where you see 3 weapons on the floor")
            print("1: A sword that is nicely cut around the edges")
            print("2: An axe that glows of power")
            print("3: A Spear with a shining blue tip")
            Path = ""
            while Path != "1" and Path != "2" and Path != "3":
                Path = input("Which weapon do you pick up?: ")
            if Path == "1":
                Weapon = "Sword"
                Attacks = (["Slice", "Stab", "Pummel", "Riposte"])
            elif Path == "2":
                Weapon = "Axe"
                Attacks = (["Bash", "Slice", "Swing", "Bludgeon"])
            elif Path == "3":
                Weapon = "Flail mace"
                Attacks = (["Swing", "Spin", "Whip"])
            print("You pick up the " + Weapon + " and feel")
            print("a soaring power running through your body")
            print("You see a door and you walk in.")
            print()
            while RNGBeastHP > 0:
                print()
                print("The beast says " + random.choice(Threats))
                RandomGoblinDamage = random.randint(2, 8)
                print("The beast " + random.choice(RNGBeastAttacks) + " you for " + str(RandomGoblinDamage) + " HP")
                HP = HP - RandomGoblinDamage
                print()
                print("You now have " + str(HP) + " HP")
                print()
                print(Attacks)
                print()
                MeleeAttack = ""
                while not (MeleeAttack in Attacks):
                    MeleeAttack = input("What attack do you want to use: ")
                RandomDamage = random.randint(48, 93)
                print("You used " + MeleeAttack + " and did " + str(RandomDamage))
                RNGBeastHP = RNGBeastHP - RandomDamage
                print("The beast now has " + str(RNGBeastHP) + " HP left")
                print()
            print("You defeat the beast and some placeholder text comes up")

        if Gamerule_Start_MazeDoor2 == 1:
            Count = 0
            while Count != 13:
                path = "0"
                if Count == 0:
                    AnswerKey = "1"
                    Count = StartMaze()
                elif Count == 1:
                    AnswerKey = "2"
                    Count = StartMaze()
                elif Count == 2:
                    AnswerKey = "1"
                    Count = StartMaze()
                elif Count == 3:
                    AnswerKey = "2"
                    Count = StartMaze()
                elif Count == 4:
                    AnswerKey = "3"
                    Count = StartMaze()
                elif Count == 5:
                    AnswerKey = "3"
                    Count = StartMaze()
                elif Count == 6:
                    AnswerKey = "4"
                    Count = StartMaze()
                elif Count == 7:
                    AnswerKey = "3"
                    Count = StartMaze()
                elif Count == 8:
                    AnswerKey = "2"
                    Count = StartMaze()
                elif Count == 9:
                    AnswerKey = "2"
                    Count = StartMaze()
                elif Count == 10:
                    AnswerKey = "2"
                    Count = StartMaze()
                elif Count == 11:
                    AnswerKey = "1"
                    Count = StartMaze()
                elif Count == 12:
                    AnswerKey = "2"
                    Count = StartMaze()
            print("You walk through the door and the maze is over.")
            print("1: You see a gate that you can slide open with a pulley system")
            print("2: You see a door that is made from shiny black metals")
            Path = ""
            while Path != "1" and Path != "2":
                Path = input("Which path do you want to take")
            if Path == "1":
                print("You pull on the rope slowly opening the door")
                Gamerule_Trapped = 1
            if Path == "2":
                print("You open the door slowly and walk inside, The door slams shut when you walk in")
                Gamerule_PreDragonFight = 1

        if Gamerule_Trapped == 1:
            print("You pull on the rope and walk into the room")
            print("The gate crashes down on you and you cant find anything to do")
            print("You die in the room like the scum you are")

        if Gamerule_PreDragonFight == 1:
            print("When walking into the room you see a spear with a green tip on the end")
            print("You pick it up and as you do a beast comes out from the wall")
            Weapon = "Spear"
            Attacks = (["Thrust", "Throw", "Swing", "Stab"])
            while PreDragonHP > 0 and HP > 0:
                print()
                print(Attacks)
                print()
                MeleeAttack = ""
                while not (MeleeAttack in Attacks):
                    MeleeAttack = input("What attack do you want to use: ")
                RandomDamage = random.randint(15, 60)
                print("You used " + MeleeAttack + " and did " + str(RandomDamage))
                PreDragonHP = PreDragonHP - RandomDamage
                print("The beast now has " + str(PreDragonHP) + " HP left")
                print()
                print()
                print("The beast says " + random.choice(Threats))
                RandomGoblinDamage = random.randint(2, 5)
                print("The beast " + random.choice(RNGBeastAttacks) + " you for " + str(RandomGoblinDamage) + " HP")
                HP = HP - RandomGoblinDamage
                print()
                print("You now have " + str(HP) + " HP")
            if PreDragonHP <= 0 and HP > 0:
                print()
                print("You pick up and drink a potion healing you to full HP")
                HP = 20
                print()
                print("You defeat the beast and a door opens, you walk into the room and hear a giant cracking sound.")
                print("A giant dragon breaks through the roof, You feel immense power in the room")
                Gamerule_DragonFight = 1
            elif HP <= 0:
                print("You died")

        if Gamerule_DragonFight == 1:
            print("The dragon blasts you with fire, you try running away but it is blocking the exit")
            print("It shoots a fireball at you breaking open a wall which you run through")
            print("You see shiny green armor with a note beside it")
            print()
            print("Experiment 46 - Dragon Armor and utility")
            print("Armor specially designed for fighting dragons")
            print("Highly resistant to fire and scale protection")
            print("HP Boost potion")
            print("Dragon and Fire resistance potion")
            print()
            print("You pick up and put on the armor. You look for an escape but there is none")
            print("After picking up the armor you decide to drink the potions")
            print("Your heart starts beating faster and feel a surge of blood flow through your body")
            print()
            HP = 100
            print("Your current (boosted) HP is " + str(HP))
            print()
            print("You have to fight the dragon or die...")
            Path = ""
            while Path != "yes" and Path != "Yes" and Path != "y" and Path != "Y" and Path != "no" and Path != "No" and Path != "n" and Path != "N":
                Path = input("Do you want to fight?: ")
                if Path == "Yes" or Path == "yes" or Path == "y" or Path == "Y":
                    print("You run out into the opening ready to fight the dragon")
                    while DragonHP > 0 and HP > 0:
                        print("")
                        print(Attacks)
                        print("")
                        MeleeAttack = ""
                        while not(MeleeAttack in Attacks):
                            MeleeAttack = input("What attack do you want to use: ")
                            RandomDamage = random.randint(7000, 21000)
                        DragonHP = DragonHP - RandomDamage
                        print("You used " + MeleeAttack + "and did " + str(RandomDamage) + " damage")
                        print("The dragon now has " + str(DragonHP) + "HP")
                        if DragonHP > 0 and HP > 0:
                            RandomDragonDamage = random.randint(13, 30)
                            print("The dragon " + random.choice(DragonAttacks) + " you for " + str(RandomDragonDamage) + " HP")
                            HP = HP - RandomDragonDamage
                        print("You now have " + str(HP) + " HP")
                    if DragonHP <= 0:
                        print("You won! Good job!")
                    elif HP <= 0:
                        print("You lost! Too bad")



                elif Path == "no" or Path == "No" or Path == "N" or Path == "n":
                    print("You decide to live out your life in the cave with no food or water")
                    print("After a few days you die with no one around you...")

        if Gamerule_CorridorDamage == 1:
            NegativeHP = random.randint(2, 5)
            print()
            print("You have lost some HP")
            print("You have lost " + str(NegativeHP) + (" HP crawling through the walls"))
            HP = (HP - NegativeHP)
            print("You now have " + str(HP) + " HP")
            print()
            print("You walk through the corridor turning multiple times until you come to a door")
            print("You try opening the door with they key you have but it doesnt fit")
            print("You decide to stay and sit down for a while and relax...")
            time.sleep(5)
            print("After resting a while you think it might be time to leave even though you want to stay...")
            print("1: You think of staying there and sleeping to restore some of your energy")
            print("2: You need to get going again to find out where you need to go")
            Path = ""
            while Path != "1" and Path != "2" and Path != "3":
                Path = input("What do you want to do? 1 or 2: ")
            if Path == 1:
                print("You decide to sleep in the corridor. You try finding a space to sleep on the floor")
                print("Finally you fall asleep")
                time.sleep(5)
                print(
                    "You wake up to large banging, there are gaurds at the door. The door opens and they see you sleeping on the floor")
                print("The gaurds bring you back to the cell")
                Gamerule_StartIntro1 = 1
            if Path == 2:
                print("You walk back through the crack taking some more damage and go through the vent like system")
                print()
                print("You have lost some HP")
                print("You have lost " + str(NegativeHP) + (" HP crawling through the walls"))
                HP = (HP - NegativeHP)
                print("You now have " + str(HP) + " HP")
                print()
                Gamerule_OutsideDoor1 = 1

        # VENT WALKWAY
        if Gamerule_OutsideDoor1 == 1:
            print("You crawl inside the hole and you see a long path, the path leads to a dim light")
            print("You see two ways you can go")
            print("1: You see lots of light comming through holes in a trapdoor")
            print("2: You also see the vent like system lead to a bigger room where you see candle lights")
            print()
            Path = ""
            while Path != "1" and Path != "2":
                Path = input("Which path do you want to take? 1 or 2: ")
            if Path == "1":
                Gamerule_Trapdoor = 1
            elif Path == "2":
                Gamerule_FallBackSpawn = 1

        if Gamerule_Trapdoor == 1:
            print("You crawl through the trapdoor revealing the outside of the dungeon.")
            print("You walk out happy to be free from the place then you spot some prison gaurds heading back")
            print("1: You think of trying to sneak past them so they wont see you.")
            print("2: You go back into the dungeon to hide and go another path")
            print("3: You try hiding from the gaurds in some bushes nearby")
            Path = ""
            while Path != "1" and Path != "2" and Path != "3":
                Path = input("What do you want to do? 1, 2 or 3: ")

                # RUN PAST GUARD ENDING (RNG)
            if Path == "1":
                print()
                print(
                    "You crawl past to the road that you need to cross, you see a rock and a tree you can hide behind")
                Path = ""
                while Path != "Rock" and Path != "rock" and Path != "Tree" and Path != "tree":
                    Path = input("Do you run to the rock or the tree?: ")
                if Path == "Rock" or Path == "rock":
                    RockHide = random.randint(1, 5)
                    if RockHide == 1:
                        print("You manage to cross the road and hide behind the rocks until the gaurds pass")
                    else:
                        print(
                            "The guards spot you as you're running and catch you, they pin you to the ground and bring you back to the cell.")
                        print()
                        Gamerule_StartIntro1 = 1

                if Path == "Tree" or Path == "tree":
                    TreeHide = random.randint(1, 5)
                    if TreeHide == 5 or TreeHide == 4:
                        print("You manage to cross the road and hide behind the tree until the gaurds pass")
                        print()
                    else:
                        print(
                            "The guards spot you as you're running and catch you, they pin you to the ground and bring you back to the cell.")
                        print()
                        Gamerule_StartIntro1 = 1

                        # Stealth Escape

            elif Path == "2":
                    Gamerule_Stealth = 1

                # Hide in bushes get caught

            elif Path == "3":
                print()
                print("You hide in nearby bushes but the one of the gaurds stops walking and looks around")
                print("He sees you hiding in the bush and pins you down, than he brings you back to the cell")
                print()
                Gamerule_StartIntro1 = 1

                # STEALTH ENDING

        if Gamerule_Stealth == 1:
            Path = "2"
            if Path == "2":
                print()
                print("You go back into the dungeon where you see a pathway, you walk and see 5 levers")
                print("In the wall there is some writing written on the wall")
                print()
                print("THIS PUZZEL MUST BE SOLVED BY THE BEST")
                print("TO SOLVE IT YOU MUST COMPLETE A TEST")
                print()
                print("You think to yourself what levers you need to pull")
                RandomLever1 = random.choice(NumbersCode)
                RandomLever2 = random.choice(NumbersCode)
                RandomLever3 = random.choice(NumbersCode)
                RandomLever4 = random.choice(NumbersCode)
                RandomLever5 = random.choice(NumbersCode)
                while Lever1 != RandomLever1 or Lever2 != RandomLever2 or Lever3 != RandomLever3 or Lever4 != RandomLever4 or Lever5 != RandomLever5:
                    print()
                    Lever1 = input("Input a number between 1 and 9: ")
                    Lever2 = input("Input a number between 1 and 9: ")
                    Lever3 = input("Input a number between 1 and 9: ")
                    Lever4 = input("Input a number between 1 and 9: ")
                    Lever5 = input("Input a number between 1 and 9: ")
                    print()
                    if Lever1 == RandomLever1:
                        print("Number 1 was correct")
                    if Lever2 == RandomLever2:
                        print("Number 2 was correct")
                    if Lever3 == RandomLever3:
                        print("Number 3 was correct")
                    if Lever4 == RandomLever4:
                        print("Number 4 was correct")
                    if Lever5 == RandomLever5:
                        print("Number 5 was correct")
                print("Ok fini")
                # Hide in bushes get caught

        if Gamerule_FallBackSpawn == 1:
            print("You walk down the corridor seeing lit lights not paying attention to where you are going.")
            print("You see the corridor open up to the outside world and run towards it as fast as you can")
            print(
                "As you arent paying attention to the ground you fall into a hole back into the dungeon where you started")
            NegativeHP = random.randint(3, 7)
            print()
            print("You have lost some HP")
            print("You have lost " + str(NegativeHP) + (" HP falling down the hole"))
            HP = (HP - NegativeHP)
            print("You now have " + str(HP) + " HP")
            Gamerule_StartIntro1 = 1
        playagain = ""
        playagain = input("Do you want to play again?(Y/M): ")
