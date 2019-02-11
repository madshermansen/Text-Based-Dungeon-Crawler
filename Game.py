
# Name: Mads
# Date: 05/01/19
# Description: Epic Dungeon adventure with determining if you will escape or not.

import random
import time

#---------------------------------------------------------------#

# Introduction

def DisplayIntroduction():
    print("You wake up in a cold cold dungeon, and before you appear a dark siluette in the figure of a young boy or a woman, as your vision")
    print("slowly appears. You try talking to the figure but it doesnt respond or look your way.")
    print("Then you pass out...")
    print()
    print("You wake up with a message carved in the wall.")
    print()
    print("YOU HAVE MESSED WITH DPU.")
    print("A PUNISHMENT WILL BE BROUGHT")
    print("UPON YOU, UNLESS YOU ESCAPE")
    print("THIS DUNGEON")

#---------------------------------------------------------------#

# Choosing Path

def choosepath():
    path = ""
    while path != "1" and path != "2": # Checking for the input
        path = input("Which path will you take? 1 or 2?: ")

    return path

#---------------------------------------------------------------#



#---------------------------------------------------------------#

HP = 20
NegativeHP = 0
GoblinHP = 6
ChildGoblinHP = 4

def LoseHP():

    print("Save Text = You have lost some HP")
    print("You have lost " + str(NegativeHP) + (" HP"))

DrinkPotion = ""

# Play again function


#playagain = "yes"
#while playagain == "yes" or playagain == "y":
#    DisplayIntroduction()
#    choice = choosepath()
#    checkpath(choice)
#    playagain = input("Do you want to play again? type yes or y to continue playing: ")



Threats=(["Ill beat you silly!", "You're just a mere mortal! Get out of my sight", "What if i turn you into a toaster!", "I'll beat you in chess!", "You are a rump-faced ape!", "Im not insulting you, im describing you", "You are'nt invited to my birthday party anymore!", "Go sit on a pinecone", "Who's this clown", ])
Attacks=(["Slice", "Stab", "Pummel", "Riposte" ])
MeleeAttacks=(["Punch", "Kick", "Headbutt", "Throw rock" ])
GoblinAttacks=(["hits", "throws a rock at", "spits on", "jumps on your head and smacks" ])
NumbersCode=(["1", "2"])

##############################################################

                     # Run Game #

##############################################################

#If want specific place change to 0 and change      if Gamerule_PlayGame == 1:      to      if Gamerule_PlayGame == 0:
                     
Gamerule_PlayGame = 1             

##############################################################

#Start Game

if Gamerule_PlayGame == 1:
    playagain = "yes"
    while playagain == "yes" or playagain == "y":
        #functions
        HP = 20
        NegativeHP = random.randint(1, 2)
        GoblinHP = 6
        ChildGoblinHP = 4
        KeyA = 0
        KeyB = 0
        RandomPotionRNG = 0
        ChestRandomKey = 0
        KeyBDoor = 0
        MazeDoor = "0"
        MazeFinish = 0
        #Gamerule Functions
        Gamerule_PlayGame = 0
        Gamerule_StartIntro1 = 0
        Gamerule_Dungeon = 0
        Gamerule_KeyADoor = 0
        Gamerule_KeyFinder = 0
        Gamerule_Start_MazeDoor = 0
        Gamerule_Start_MazeDoor2 = 1
        Gamerule_CorridorDamage = 0
        Gamerule_CorridorDamage2 = 0
        Gamerule_OutsideDoor1 = 0
        Gamerule_Trapdoor = 0
        Gamerule_Stealth = 0
        Gamerule_FallBackSpawn = 0
        Gamerule_MagicDoor = 0
        Gamerule_RNGEnding = 0
        Gamerule_TeleportCube = 0 
        #Start Game
        if Gamerule_PlayGame == 1:
            print()
            print("1: You stand up, you see that the wall is old and has a large crack running through it.")
            print("2: You also see that the door is slightly ajar and could be pushed open")
            print()
            choice = choosepath()
            if choice == "1":
                print("You try pulling open the crack but nothing happens")
                print("You decide to run at the wall breaking it open but getting hurt")
                print()
                HP = (HP - NegativeHP)
                print ("You now have " + str(HP) + "HP")
                print()
                print("There is a hollow room on the other side of the wall")
                WallBreak = random.randint(1, 2)
                if WallBreak == 1:
                    print("There is a statue that casts a blessing on you")
                    print("As you walk out of the room you start to feel more refreshed")
                    print("HP +1")
                    HP = HP + 1
                    Gamerule_StartIntro1 = 1
                else:
                    print("There is a door that leads to stairs going furthur down the dungeon")
                    Enter = input("Do you want to go furthur down? y or n: ")
                    if Enter == "n":
                         print("You walk back not having achieved anything")
                         Gamerule_StartIntro1 = 1
                    elif Enter == "y":
                        Gamerule_Dungeon = 1
                    else:
                        Gamerule_StartIntro1 = 1

                    #Player decides to go back into main room
                    
            if Gamerule_StartIntro1 == 1:
                print()
                print("You walk back from the hollow room not having done anything")

                #Player chooses to go into the dungeon

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
                    while MeleeAttack != "Punch" and MeleeAttack != "Kick" and MeleeAttack != "Throw rock" and MeleeAttack != "Headbutt":
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


            #Different doors, Key, Maze, Find Key.

        if Gamerule_KeyADoor == 1:
            print("1")
            if KeyA == 1:
                print("You open the door with ease, the key slides in and you walk in.")
                print("There is a long hallway lit with candles, you walk down it not thinking about anything")
                print("1: You see a small corridor that you could fit in if you pushed yourself very hard.")
                print("2: You also see a vent like system that you could easily crawl through but would need to push yourself")
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
                    print("2: And a third room that is locked and needs a key to open")
                    Path = ""
                    while Path != "1" and Path != "2":
                        Path = input("Which door do you want to open? 1 or 2: ")
                    print()
                    if Path == "1":
                        Gamerule_KeyADoor = 1
                    if Path == "2":
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
                if Path == "1":
                    Gamerule_Start_MazeDoor = 1
                    
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

        if Gamerule_Start_MazeDoor2 == 1:
            while MazeDoor != "1" and MazeDoor != "2" and MazeDoor != "3":
                print("Room 1")
                print()
                print("1: Left")
                print("2: Forward")
                print("3: Right")
                MazeDoor = input("Which door do you want to go through: ")
                print()
            if MazeDoor == "1":
                print("You walk into the next room")
                print()
                if Gamerule_Start_MazeDoor2 == 1:
                    while MazeDoor != "1" and MazeDoor != "2" and MazeDoor != "3":
                        print("Room 2")
                        print()
                        print("1: Left")
                        print("2: Forward")
                        print("3: Right")
                        MazeDoor = input("Which door do you want to go through: ")
                        print()
                    if MazeDoor == "1":
                        print("You walk into the next room")
                        print()
                    else:
                        print("You walk back to the start of the maze")
                        print()
            else:
                print("You walk back to the start of the maze")
                print()
            
                        
                    
                    
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
                print("You wake up to large banging, there are gaurds at the door. The door opens and they see you sleeping on the floor")
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

        #VENT WALKWAY
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
                
                            #RUN PAST GUARD ENDING (RNG)
                
            if Path == "1":
                print()
                print("You crawl past to the road that you need to cross, you see a rock and a tree you can hide behind")
                Path = ""
                while Path != "Rock" and Path != "rock" and Path != "Tree" and Path != "tree":
                    Path = input("Do you run to the rock or the tree?: ")
                if Path == "Rock" or Path == "rock":
                    RockHide = random.randint(1,5)
                    if RockHide == 1 :
                        print("You manage to cross the road and hide behind the rocks until the gaurds pass")
                    else:
                        print("The guards spot you as you're running and catch you, they pin you to the ground and bring you back to the cell.")
                        print()
                        Gamerule_StartIntro1 = 1
                if Path == "Tree" or Path == "tree":
                    TreeHide = random.randint(1,5)
                    if TreeHide == 5 or TreeHide == 4:
                        print("You manage to cross the road and hide behind the tree until the gaurds pass")
                        print()
                    else:
                        print("The guards spot you as you're running and catch you, they pin you to the ground and bring you back to the cell.")
                        print()
                        Gamerule_StartIntro1 = 1
                        
                        #Stealth Escape
                        
                if Path == "2":
                    Gamerule_Stealth = 1
                
                #Hide in bushes get caught
                
            if Path == "3":
                print()
                print("You hide in nearby bushes but the one of the gaurds stops walking and looks around")
                print("He sees you hiding in the bush and pins you down, than he brings you back to the cell")
                print()
                Gamerule_StartIntro1 = 1

                                #STEALTH ENDING
                        
        if Gamerule_Stealth == 1:
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
                    Lever1 = input("Pull lever 1? 1 or 0: ")
                    Lever2 = input("Pull lever 2? 1 or 0: ")
                    Lever3 = input("Pull lever 3? 1 or 0: ")
                    Lever4 = input("Pull lever 4? 1 or 0: ")
                    Lever5 = input("Pull lever 5? 1 or 0: ")
                    print()
                    if not(Lever1 != "1" or Lever2 != "0" or Lever3 != "1" or Lever4 != "1" or Lever5 != "0"):
                        print("WRONG TRY AGAIN")
                print("Ok fini")
                #Hide in bushes get caught


        if Gamerule_FallBackSpawn == 1:
            print("You walk down the corridor seeing lit lights not paying attention to where you are going.")
            print("You see the corridor open up to the outside world and run towards it as fast as you can")
            print("As you arent paying attention to the ground you fall into a hole back into the dungeon where you started")
            NegativeHP = random.randint(3, 7)
            print()
            print("You have lost some HP")
            print("You have lost " + str(NegativeHP) + (" HP falling down the hole"))
            HP = (HP - NegativeHP)
            print("You now have " + str(HP) + " HP")
            Gamerule_StartIntro1 = 1
            