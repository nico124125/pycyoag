######################### IMPORTING MODULES/PACKAGES ###############################
import random
import time, sys
import os


# add other imports like sound, math, etc. here

# test push
# tes pull


# pauses game until user presses enter


name = input("Enter your name soldier! ")


################## DEFINITIONS OF TEACHER SUPPLIED FUNCTIONS ######################
def chooseOption(numberOfOptions):
    choice = 0
    while choice < 1 or choice > numberOfOptions:
        print('1 to ' + str(numberOfOptions) + '> ', end='')
        choice = input()
        if choice != '1' and choice != '2' and choice != '3' and choice != '4':
            choice = 0
        if choice == '1' or choice == '2' or choice == '3' or choice == '4':
            choice = int(choice)
        print('\n\n')
        return choice


def pause():
    input('Enter to deploy')
    print(f'You are being deployed {name}')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

deploy_intro_ascci1 = r"""
         _  _
        ( `   )_
       (    )    `)
     (_   (_ .  _) _)
                                    _
                                   (  )
    _ .                         ( `  ) . )
  (  _ )_                      (_, _(  ,_)_)
(_  _(_ ,)
                                                       |
         _  _                                        \ _ /
        ( `   )_                                   -= (_) =-
       (    )    `)                                  /   \
     (_   (_ .  _) _)             



                                 -=\`\
                             |\ ____\_\__
                          -=\CAF******** `*)
                              `~~~~~/ /~~`
                                -==/ /
                                  /-/    




                                              (  )
                _, _ .                         ( `  ) . )
               ( (  _ )_                      (_, _(  ,_)_)
             (_(_  _(_ ,)
"""
deploy_intro_ascci2 = r"""
         _  _
        ( `   )_
       (    )    `)
     (_   (_ .  _) _)
                                    _
                                   (  )
    _ .                         ( `  ) . )
  (  _ )_                      (_, _(  ,_)_)
(_  _(_ ,)
                                                       |
         _  _                                        \ _ /
        ( `   )_                                   -= (_) =-
       (    )    `)                                  /   \
     (_   (_ .  _) _)             



                                   -=\`\
                               |\ ____\_\__
                            -=\CAF******* `*)
                                `~~~~~/ /~~`
                                  -==/ /
                                    /-/    




                                              (  )
                _, _ .                         ( `  ) . )
               ( (  _ )_                      (_, _(  ,_)_)
             (_(_  _(_ ,)
"""
deploy_intro_ascci3 = r"""
         _  _
        ( `   )_
       (    )    `)
     (_   (_ .  _) _)
                                    _
                                   (  )
    _ .                         ( `  ) . )
  (  _ )_                      (_, _(  ,_)_)
(_  _(_ ,)
                                                       |
         _  _                                        \ _ /
        ( `   )_                                   -= (_) =-
       (    )    `)                                  /   \
     (_   (_ .  _) _)             



                                     -=\`\
                                 |\ ____\_\__
                              -=\CAF******* `*)
                                  `~~~~~/ /~~`
                                    -==/ /
                                      /-/    




                                              (  )
                _, _ .                         ( `  ) . )
               ( (  _ )_                      (_, _(  ,_)_)
             (_(_  _(_ ,)
"""
deploy_intro_ascci4 = r"""
         _  _
        ( `   )_
       (    )    `)
     (_   (_ .  _) _)
                                    _
                                   (  )
    _ .                         ( `  ) . )
  (  _ )_                      (_, _(  ,_)_)
(_  _(_ ,)
                                                       |
         _  _                                        \ _ /
        ( `   )_                                   -= (_) =-
       (    )    `)                                  /   \
     (_   (_ .  _) _)             



                                       -=\`\
                                   |\ ____\_\__
                                -=\CAF******* `*)
                                  . --~~~~~/ /~~`
                                       -==/ /
                                         /-/    




                                              (  )
                _, _ .                         ( `  ) . )
               ( (  _ )_                      (_, _(  ,_)_)
             (_(_  _(_ ,)
"""
deploy_intro_ascci5 = r"""
         _  _
        ( `   )_
       (    )    `)
     (_   (_ .  _) _)
                                    _
                                   (  )
    _ .                         ( `  ) . )
  (  _ )_                      (_, _(  ,_)_)
(_  _(_ ,)
                                                       |
         _  _                                        \ _ /
        ( `   )_                                   -= (_) =-
       (    )    `)                                  /   \
     (_   (_ .  _) _)             



                                         -=\`\
                                     |\ ____\_\__
                                  -=\CAF******* `*)
                                  .   --~~~~~/ /~~`
                                         -==/ /
                                           /-/    




                                              (  )
                _, _ .                         ( `  ) . )
               ( (  _ )_                      (_, _(  ,_)_)
             (_(_  _(_ ,)
"""
deploy_intro_ascci6 = r"""
         _  _
        ( `   )_
       (    )    `)
     (_   (_ .  _) _)
                                    _
                                   (  )
    _ .                         ( `  ) . )
  (  _ )_                      (_, _(  ,_)_)
(_  _(_ ,)
                                                       |
         _  _                                        \ _ /
        ( `   )_                                   -= (_) =-
       (    )    `)                                  /   \
     (_   (_ .  _) _)             



                                          -=\`\
                                      |\ ____\_\__
                                   -=\CAF******* `*)
                                       --~~~~~/ /~~`
                                   .      -==/ /
                                            /-/    




                                              (  )
                _, _ .                         ( `  ) . )
               ( (  _ )_                      (_, _(  ,_)_)
             (_(_  _(_ ,)
"""
deploy_intro_ascci7 = r"""
         _  _
        ( `   )_
       (    )    `)
     (_   (_ .  _) _)
                                    _
                                   (  )
    _ .                         ( `  ) . )
  (  _ )_                      (_, _(  ,_)_)
(_  _(_ ,)
                                                       |
         _  _                                        \ _ /
        ( `   )_                                   -= (_) =-
       (    )    `)                                  /   \
     (_   (_ .  _) _)             



                                            -=\`\
                                        |\ ____\_\__
                                     -=\CAF******* `*)
                                         --~~~~~/ /~~`
                                            -==/ /
                                    \./       /-/    




                                              (  )
                _, _ .                         ( `  ) . )
               ( (  _ )_                      (_, _(  ,_)_)
             (_(_  _(_ ,)
"""
deploy_intro_ascci8 = r"""
         _  _
        ( `   )_
       (    )    `)
     (_   (_ .  _) _)
                                    _
                                   (  )
    _ .                         ( `  ) . )
  (  _ )_                      (_, _(  ,_)_)
(_  _(_ ,)
                                                       |
         _  _                                        \ _ /
        ( `   )_                                   -= (_) =-
       (    )    `)                                  /   \
     (_   (_ .  _) _)             



                                                -=\`\
                                            |\ ____\_\__
                                         -=\CAF******* `*)
                                       ___   --~~~~~/ /~~`
                                      (   )     -==/ /
                                      \   /       /-/    
                                       \./     



                                              (  )
                _, _ .                         ( `  ) . )
               ( (  _ )_                      (_, _(  ,_)_)
             (_(_  _(_ ,)
"""
deploy_intro_ascci9 = r"""
         _  _
        ( `   )_
       (    )    `)
     (_   (_ .  _) _)
                                    _
                                   (  )
    _ .                         ( `  ) . )
  (  _ )_                      (_, _(  ,_)_)
(_  _(_ ,)
                                                       |
         _  _                                        \ _ /
        ( `   )_                                   -= (_) =-
       (    )    `)                                  /   \
     (_   (_ .  _) _)             



                                                   -=\`\
                                               |\ ____\_\__
                                            -=\CAF******* `*)
                                                --~~~~~/ /~~`
                                                   -==/ /
                                        ___          /-/    
                                       (   )
                                       \   / 
                                        \./

                                              (  )
                _, _ .                         ( `  ) . )
               ( (  _ )_                      (_, _(  ,_)_)
             (_(_  _(_ ,)
"""
deploy_intro_ascci10 = r"""
         _  _
        ( `   )_
       (    )    `)
     (_   (_ .  _) _)
                                    _
                                   (  )
    _ .                         ( `  ) . )
  (  _ )_                      (_, _(  ,_)_)
(_  _(_ ,)
                                                       |
         _  _                                        \ _ /
        ( `   )_                                   -= (_) =-
       (    )    `)                                  /   \
     (_   (_ .  _) _)             









                                        ___       
                                       (   )
                                       \   / 
                                        \./

                                              (  )
                _, _ .                         ( `  ) . )
               ( (  _ )_                      (_, _(  ,_)_)
             (_(_  _(_ ,)
"""


##https://asciiart.cc/view/11081 - plane
###################### DEFINITIONS OF YOUR FUNCTIONS ############################

# INTRODUCTION function
# function to introduce the game and then start it
def game_intro():
    print('\n')
    # introduce story and provide simple instructions...
    pause()
    print("deloying in 5 seconds!")
    time.sleep(3)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    print("you are being deployed!")
    # call start() function to START your actual game/adventure;
    start()


# START function
# start the game by setting up the location/scene/action
def start():
    # time.sleep(0.5)
    # continue story line and proceed to first location/scene/action

    # Then jump to the first scene/location/action;
    # rename the function call AND the function defintion!
    print("skip intro?")
    print('1 Yes')
    print('2 No')
    choice = chooseOption(2)
    print(choice)
    if choice == 1:
        warZone_nointro()
    elif 2 == choice:
        warZone()


########################## LOCATION/SCENE/ACTION Functions #######################

# RENAME location1() function to reflect your actual first location/scene/action
def warZone():
    print(deploy_intro_ascci1)
    time.sleep(0.5)
    print(deploy_intro_ascci2)
    time.sleep(0.5)
    print(deploy_intro_ascci3)
    time.sleep(0.5)
    print(deploy_intro_ascci4)
    time.sleep(0.5)
    print(deploy_intro_ascci5)
    time.sleep(0.5)
    print(deploy_intro_ascci6)
    time.sleep(0.5)
    print(deploy_intro_ascci7)
    time.sleep(0.5)
    print(deploy_intro_ascci8)
    time.sleep(0.5)
    print(deploy_intro_ascci9)
    time.sleep(0.5)
    print(deploy_intro_ascci10)
    time.sleep(0.5)
    print('You are landing!')
    time.sleep(2)
    clear_screen()
    mylist = ["Death", "landing", "landing", "landing", "landing", "landing", "landing"]
    if (random.choice(mylist)) == "Death":
        print(f'{name}s parachute ripped!')
        print("\033[1;31;40m You died! \n")
    else:
        print('You have successfully landed into a treacherous deep jungle in a undisclosed location')
        time.sleep(4)
        print(f'your name is {name}, and you must make it out of this warzone alive')
        time.sleep(2)
        print('you are only equipped with a backpack, a large laser pointer, a radio, and a map')
        time.sleep(4)
        print("as you look around, you realise you have landed in the only open part of the jungle")
        time.sleep(3)
        print("To proceed, you will need to push forward, deeper into the jungle")
        time.sleep(2)
        # Clearing the Screen
        # list players options
        print()
        print('You are now in the warzone, What is your first objective?')
        print('  1 Seek Enemies')
        print('  2 Find Supplies')
        print('  3 leave')
        print('  4 Go towards cave')

        # handle player's selection to jump to other locations/scenes/actions
        choice = chooseOption(4)
        print(choice)
        if choice == 1:
            seekEnemies()
        elif 2 == choice:
            findSupplies()
        elif 3 == choice:
            leave()
        elif 4 == choice:
            amazingChoice()
        else:
            print("That wasn't a option!")

clear_screen()
def warZone_nointro():
    print("To proceed, you will need to push forward, deeper into the jungle")
    # list players options
    print()
    print('You are now in the warzone, What is your first objective?')
    print('  1 Seek Enemies')
    print('  2 Find Supplies')
    print('  3 leave')
    print('  4 Go towards cave')

    # handle player's selection to jump to other locations/scenes/actions
    choice = chooseOption(4)
    print(choice)
    if choice == 1:
        seekEnemies()
    elif 2 == choice:
        findSupplies()
    elif 3 == choice:
        leave()
    elif 4 == choice:
        amazingChoice()
    else:
        print("That wasn't a option!")

clear_screen()
def findSupplies():
    print("You find it best to find supplies")
    mylist = ["Water", "Water", "Water", "Water", "Water", "Bandage", "Bandage", "Bandage", "Bandage", "Bandage"]
    result = random.choice(mylist)
    if (result) == "Water":
        print(f'{name} finds some water, Should be useful...')
        time.sleep(0.5)
        print()
        print('You have now have some water, but still a objective to complete, what will you do?')
        print('  1 Seek Enemies')
        print('  2 Go towards cave')
        choice = chooseOption(2)
        print(choice)
        if choice == 1:
            seekEnemies()
        elif 2 == choice:
            amazingChoice()
        else:
            print("That wasn't a option!")

    elif (result) == "Bandage":

        print(f'{name} finds a bandage, Hopefully wont need it...')
        time.sleep(0.5)
        print()
        print('You have now have a bandage, but still a objective to complete, what will you do?')
        print('  1 Seek Enemies')
        print('  2 Go towards cave')
        choice = chooseOption(2)
        time.sleep(0.5)
        print(choice)
        if choice == 1:
            seekEnemies()
        elif 2 == choice:
            amazingChoice()
        else:
            print("That wasn't a option!")

clear_screen()
# rename function to reflect your actual location/scene/action
def seekEnemies():
    print(f'{name} thinks that the best idea is to find enemy squads and take them out')
    time.sleep(2)
    print(f'{name} ventures deeper into the expansive jungle, eventually spotting a small wood building')
    time.sleep(3)
    print("you notice nearby footsteps, so you ensure to approach silently")
    time.sleep(3)
    print('as you sneak closer, using trees as cover, you spot a enemy squad. What will you do?')
    print('1 Use your supplied weapon')
    print('2 Throw a rock')
    print('3 use your laser')
    choice = chooseOption(3)
    print(choice)
    if choice == 1:
        UseWeapon()
    elif 2 == choice:
        RockThrow()
    elif 3 == choice:
        airStrike1()

    else:
        print("That wasn't a option!.")

clear_screen()
def leave():
    mylist = ["leave", "death"]
    if (random.choice(mylist)) == "leave":
        print(f'although {name} has just landed, they have decided to leave')
    else:
        print(f'{name} was attacked by a tiger trying to flee!')
        # handle player's selection to jump to other locations/scenes/actions

clear_screen()
def UseWeapon():
    print('Of course! You will use your supplied weapon')
    time.sleep(2)
    print('wait a minute, I dont have a supplied weapon.')
    time.sleep(2)
    print("the squad spots you.")
    print(f'{name} died!')

clear_screen()
def RockThrow():
    print(f'{name} finds a rock on the ground, and thinks it is best to throw it at the squad')
    time.sleep(2)
    print(f'{name} throws the rock')
    time.sleep(2)
    mylist = ["Hit", "Miss"]
    if (random.choice(mylist)) == "Miss":
        print(f'{name} missed!')
        print("\033[1;31;40m You died! \n")

    else:
        print(f'{name} hits a squad member with the rock')
        time.sleep(3)
        print(
            f'{name}s throw was powerful enough to knock a the squad member unconscious, but now the squad has spotted you')
        time.sleep(2)
        print('in a panic you dash for cover, trying to think of a different plan')
        time.sleep(3)
        print('You remember that you have a large laser pointer, and a radio that can be used to call in a airstrike')
        airStrike()

clear_screen()
def airStrike():
    print(f'{name} points the beam in the direction of the enemies, and talks into their radio')
    time.sleep(3)
    print('the pilot confirms the airstrike is inbound, so you take cover')
    time.sleep(3)
    print('the plane bursts through the air, and drops its munitions.')
    time.sleep(4)
    print('the planes munitions hits the squad, it explodes with a thunderous explosion that sends a shockwave, moving trees, and scaring birds in the distance')
    levelTwo()

clear_screen()
def airStrike1():
    print(
        f'{name} points the beam in the direction of the enemies, and talks into their radio, intending to use the beam as a marker for a airstrike')
    time.sleep(2)
    mylist = ["Hit", "Miss"]
    if (random.choice(mylist)) == "Miss":
        print('With all the dense forestry, the pilot could not pin-point your exact location')
        time.sleep(3)
        print('you see the jet fly past and drop its bomb, but in the wrong location')
        time.sleep(3)
        print('you try and escape, using trees as cover')
        time.sleep(3)
        print(f'The squad spots {name} and starts firing')
        time.sleep(2)
        print("\033[1;31;40m You died! \n")
    else:
        print("You spot the jet in the distance, it bursts through the sky and releases it's payload")
        time.sleep(2)
        print("Direct hit! the squad is no more!")
        levelTwo()

    # handle player's selection to jump to other locations/scenes/actions

clear_screen()
def amazingChoice():
    print(f'{name} looks into the distance, spotting a small cave')
    time.sleep(3)
    print("you think there might be somthing useful in the cave so you venture into it")
    time.sleep(3)
    print("as you get deeper and deeper you notice that there is strange smoke coming from cracks in the cave")
    time.sleep(3)
    print(f'{name} finds the smoke smells kind of funny. you assure yourself that its fine.')
    time.sleep(2)
    print('yu get t o the enD of thE c aVe aNd fiNd NoTHing')
    print('Well, that was a waste fo teim')
    print('1 CAVE')

    # handle player's selection to jump to other locations/scenes/actions
    choice = chooseOption(000000)
    print(choice)
    if choice == 1:
        amazingChoice1()
    else:
        print("htat wsnt na topion!")

clear_screen()
def amazingChoice1():
    print("what... is......")
    time.sleep(3)
    print('...')
    time.sleep(1)
    print()
    print('wwjaikhguowapoaji')
    time.sleep(3)
    print(' efiandsupl')
    time.sleep(3)
    print(f'{name} Died from gas!')


# rename function to reflect your actual location/scene/action

clear_screen()
# rename function to reflect your actual location/scene/action
def levelTwo():
    print(f' after getting past that first squad you need to get deeper into the jungle')
    time.sleep(3)
    print('you are presented with a new set of options')
    print('1 Find a weapon')
    print('2 Find supplies')
    print('3 Search for more enemies to attack')
    print('4 Try to establish a radio signal to extract')
    print('5 Leave')
    choice = chooseOption(5)
    print(choice)
    if choice == 1:
        findaWeapon()
    elif 2 == choice:
        findsupplies2()
    elif 3 == choice:
        searchforenemies()
    elif 4 == choice:
        radioSignal()
    elif 5 == choice:
        leave()

    else:
        print("That wasn't a option! You instead implode from self conflict")

clear_screen()
# Find A weapon story
def findaWeapon():
    print('You decide that you need to be able to protect yourself with a weapon')
    time.sleep(3)
    print('you explore further until you find a old overgrown factory that seems a abandoned')
    print('you spot a degrading sign that says armoury. How will you get in?')
    time.sleep(3)
    print('1 Back door')
    print('2 Front door')
    print('3 Roof hatch')
    print('4 dig..')
    choice = chooseOption(4)
    print(choice)
    if choice == 1:
        backDoor()
    elif 2 == choice:
        frontDoor()
    elif 3 == choice:
        skyLight()
    elif 4 == choice:
        dig()
    else:
        print("That wasn't a option! You instead implode from self conflict")

clear_screen()
def backDoor():
    print('you decide to go into the back door')
    time.sleep(2)
    print('You sneak over to the back door, and noticed its unlocked')
    time.sleep(2)
    print('as you enter the building, you notice a large amount of enemies and realise the factory is not abandoned')
    print("fortunately, you look like the other soldiers, so you are not spotted")
    time.sleep(5)
    print('you are easily able to walk past the guards and take a weapon')
    time.sleep(2)
    print('You exit the building as quickly as you snuck in')
    time.sleep(2)
    levelTwoWeapon()
    #########INSERT COPY OF ORIGINAL OPTIONS SO THAT THE PLAYER NOW HAS A WEAPON#########

clear_screen()
def frontDoor():
    print(f'{name} decides to go through the front because of how abandoned the factory looksee')
    time.sleep(1)
    print("you walk in the front door...")
    time.sleep(5)
    print("as you step through the entrance, multiple armed guard within the building looks directly at you then pause.")
    print("\033[1;31;40m You died! \n")

clear_screen()
def skyLight():
    print(f'{name} thinks they are sneaky, so they repel up to the roof and attempt to open the roof hatch')
    time.sleep(1)
    print('Unfortunately, you are not on the Impossible Mission Force so you fall through the hatch and hit the ground')

clear_screen()
def dig():
    print(f'{name} decides they will dig their way in.')
    print(f'this is going to take awhile {name} says as they take out their shovel')
    time.sleep(2)
    print('**2 DAYS LATER**')
    print('IVE BEEN DIGGING FOR SO LONG AND I HAVENT EVEN MADE A TUNNEL YET!')
    time.sleep(5)
    print('**2 MORE DAYS LATER**')
    time.sleep(1)
    print('...')
    time.sleep(1)

clear_screen()
# Find supplies 2 story
def findsupplies2():
    print(f'{name} needs supplies')
    time.sleep(3)
    mylist = ["Armour Plates", "Helmet"]
    result = random.choice(mylist)
    if (result) == "Armour Plates":
        print(f'{name} finds some Armour Plates...')
        time.sleep(1)
        print('what will you do now?')
        time.sleep(1)
        print('1 Find a weapon')
        print('2 Search for more enemies to attack')
        print('3 Try to establish a radio signal to extract')
        print('4 Leave')
        choice = chooseOption(4)
        print(choice)
        if choice == 1:
            findaWeapon()
        elif 2 == choice:
            searchforenemies()
        elif 3 == choice:
            radioSignal()
        elif 4 == choice:
            leave()

        else:
            print("That wasn't a option! You instead implode from self conflict")

    elif (result) == "Helmet":

        print(f'{name} finds a Helmet')
        time.sleep(0.5)
        print()
        print('You found a helmet, what will you do now?')
        time.sleep(1)
        print('1 Find a weapon')
        print('2 Search for more enemies to attack')
        print('3 Try to establish a radio signal to extract')
        print('4 Leave')
        choice = chooseOption(4)
        print(choice)
        if choice == 1:
            findaWeapon()
        elif 2 == choice:
            searchforenemies()
        elif 3 == choice:
            radioSignal()
        elif 4 == choice:
            leave()

clear_screen()
def findsupplies2_radio():
    print(f'{name} needs supplies')
    time.sleep(3)
    mylist = ["Armour Plates", "Helmet"]
    result = random.choice(mylist)
    if (result) == "Armour Plates":
        print(f'{name} finds some Armour Plates...')
        time.sleep(1)
        print('what will you do now?')
        time.sleep(1)
        print('1 Find a weapon')
        print('2 Search for more enemies to attack')
        print('3 Leave')
        choice = chooseOption(3)
        print(choice)
        if choice == 1:
            findaWeapon()
        elif 2 == choice:
            searchforenemies()
        elif 3 == choice:
            leave()

        else:
            print("That wasn't a option! You instead implode from self conflict")

    elif (result) == "Helmet":

        print(f'{name} finds a Helmet')
        time.sleep(0.5)
        print()
        print('You found a helmet, what will you do now?')
        time.sleep(1)
        print('1 Find a weapon')
        print('2 Search for more enemies to attack')
        print('3 Try to establish radio signal')
        print('4 Leave')
        choice = chooseOption(4)
        print(choice)
        if choice == 1:
            findaWeapon()
        elif 2 == choice:
            searchforenemies()
        elif 3 == choice:
            radioSignal()
        elif 4 == choice:
            leave()

clear_screen()
def escape():
    print(f'{name} has supplies and heal themselves. you go back to find a weapon')
    findaWeapon()

clear_screen()
# Search for bad enemies story
def searchforenemies():
    print(f'{name} chooses to search for more enemies to eliminate')
    time.sleep(3)
    print(f'{name} finds enemies, but they spot {name} first')
    time.sleep(2)
    print(f'The enemies start shooting at {name}')
    time.sleep(2)
    print(f'{name} tries to run away, but instead they hit their head on a doorway and pass out')
    time.sleep(3)
    print(f'{name} wakes up, and cant move.')
    print("do you have any supplies to help you?")
    choice = chooseOption(2)
    print(choice)
    if choice == 1:
        escape()
    else:
        print("That wasn't a option! You instead implode from self conflict")


def searchforenemies_weapon():
    print(f'{name} decides to search for enemies, now that they have a weapon')
    time.sleep(2)
    print(f'{name} spots the last groups of enemies off in the distance')
    time.sleep(2)
    print(f'{name} you engage one of the groups of enemies in a fire fight')
    time.sleep(3)
    print("the enemies fire back with precision")
    time.sleep(3)
    print("you get behind cover, with a new choice of options")
    time.sleep(3)
    print('1 Call in back up')
    print('2 Throw grenade')
    print('3 leave')
    choice = chooseOption(3)
    print(choice)
    if choice == 1:
        levelthree_backup()
    elif 2 == choice:
        levelthree_rambo()
    elif 3 == choice:
        leave()
    else:
        print("That wasn't a option! You instead implode from self conflict")
clear_screen()
def levelthree_backup():
    print(f'{name} decides to call in backup')
    time.sleep(2)
    print(f'as the enemies advance, {name} stays in cover, and waits for backup to arrive')
    time.sleep(4)
    print(f'the enemies hit {name} behind cover, injuring you')
    time.sleep(3)
    print("as you tend to your wounds, you hear the booming sound of a helicopters rotors")
    time.sleep(4)
    print("the helicopter zooms by, a side turret mounted on the chopper pulverises the enemies")
    time.sleep(4)
    print("the helicopter lands in a open field, and opens its side door")
    time.sleep(2)
    print("you get in the helicopter, and escape the warzone victorious")
    print(f'{name} escaped the warzone!')
clear_screen()
def levelthree_rambo():
    print(f'{name} decides to throw a grenade at the enemies')
    time.sleep(2)
    print(f'{name} snatches a nearby grenade')
    time.sleep(2)
    print("you take out the pin and throw it at the enemies")
    time.sleep(2)
    print("the grenade hits the ground near the enemies, they see this and throw the grenade back")
    time.sleep(4)
    print("the grenade explodes before reaching you and you use this as a distraction to run")
    time.sleep(4)
    print("you run into the jungle, the enemies dont follow as they are stunned...")
    time.sleep(6)
    print(f'after walking in the jungle for awhile, {name} realises that they hear the sounds of planes in the distance')
    time.sleep(4)
    print(f'{name} has found a enemy airbase')
    print(f'what should {name} do')
    print('1 sneak in air control tower for better view')
    print('2 take out ground crew for disguise')
    print('3 steal a plane and escape')
    choice = chooseOption(3)
    print(choice)
    if choice == 1:
        airControl()
    elif 2 == choice:
        disguise()
    elif 3 == choice:
        airEscape()
    else:
        print("That wasn't a option! You instead implode from self conflict")
clear_screen()
def airControl():
    print(f'{name} decides that they will get a better view from the air traffic control tower')
    time.sleep(2)
    print('you sneak around the perimeter of the base, and open the door to the stairs of the tower')
    time.sleep(3)
    print("you start to go up the stairs and make it to the top of the tower, with a view of the large jungle below you")
    time.sleep(4)
    print("as you look around, you realise there is a soldier sleeping in a chair right in front of you")
    time.sleep(3)
    print('1 RUN')
    print('2 JUMP')
    print('3 ATTACK')
    choice = chooseOption(3)
    print(choice)
    if choice == 1:
        run_tower()
    elif 2 == choice:
        jump_out_window()
    elif 3 == choice:
        attack()
    else:
        print("That wasn't a option!")

clear_screen()
def run_tower():
    print('YOU RUN DOWN THE STAIRS AS QUICKLY AS POSSIBLE')
    time.sleep(1)
    print("AS YOU JET OUT THE DOOR, THE ALARM SOUNDS")
    time.sleep(2)
    print("THE BASE IS ALERTED AND SOLDIERS IN THE DISTANCE SPOT YOU")
    print("\033[1;31;40m You died! \n")
clear_screen()
def attack():
    print("you attack the soldier, waking him up")
    time.sleep(2)
    print("you struggle with him, then eventually you overpower him")
    time.sleep(3)
    print("you throw the soldier out of the window")
    time.sleep(3)
    print("you leave the tower and go back to the front of the base")
clear_screen()
def jump_out_window():
    print("You jump out of the window")
    print("\033[1;31;40m You died! \n")
    print("what did you think was going to happen?")
clear_screen()
def disguise():
    print("you spot a solider reading a book by himself")
    time.sleep(3)
    print("you put the soldier to sleep and start to take his army fatigues")
    time.sleep(3)
    print("as you are taking the soldiers jacket off, his friend comes back from the washroom")
    time.sleep(4)
    print("Hows the book billy- WHAT THE HELL")
    print("\033[1;31;40m You died! \n")
clear_screen()
def airEscape():
    print("you sneak over to a hanger by the end of the air base")
    time.sleep(3)
    print("there are no soldiers around, you make sure the small fighter jet has gas, then get in")
    time.sleep(3)
    print("you start up the jet and taxi to the run way")
    time.sleep(3)
    print("A air traffic controller starts talking to you through the planes radio, he asks you where you are going, and if you got permission to take the plane")
    time.sleep(5)
    print("you ignore him and take off anyway, but a enemy jet follows you")
    print('1 Dogfight')
    print('2 Fly as fast as you can')
    choice = chooseOption(2)
    print(choice)
    if choice == 1:
        dogFight()
    elif 2 == choice:
        flyAway()
clear_screen()
def dogFight():
    print("you gain some altitude then slow down to get behind the enemy plane")
    time.sleep(3)
    print("The pilot does not suspect you to be hostile and acts friendly, but you shoot off his rudder")
    time.sleep(4)
    print("the pilot tries to attack you but you have already done too much damage")
    time.sleep(3)
    print("you shoot at the plane once more, the plane explodes like a firework, then plummets to the jungle below")
    print("you fly the jet to safety, surviving")
    print(f'{name} escaped the warzone!')
clear_screen()
def flyAway():
    print("You try to fly away, but the pilot follows and asks you what you are doing through the radio")
    time.sleep(3)
    print("the pilot gets inpatient and shoots you out of the sky")
    print("\033[1;31;40m You died! \n")






clear_screen()
# Try to establish a radio signal story
def radioSignal_Weapon():
    print(f'{name} chooses to establish a signal to extract')
    time.sleep(2)
    print('You start to set up...')
    time.sleep(2)
    print(f'{name} successfully set up a radio')
    print(f'enemies can now see you {name}, but this means you can extract!')
    radioSignalChoice_weapon()

clear_screen()
def radioSignalChoice_weapon():
    print('You make up 3 decisions in your head, and try to pick the best one')
    time.sleep(2)
    print('1 fight the squads that now see you')
    print('2 Take down radio')
    print('3 leave')
    choice = chooseOption(3)
    print(choice)
    if choice == 1:
        searchforenemiesradio()
    elif 2 == choice:
        destroyRadio()
    elif 3 == choice:
        leave()
    else:
        print("That wasn't a option! You instead implode from self conflict")

clear_screen()
def radioSignal():
    print(f'{name} chooses to establish a signal to extract')
    time.sleep(2)
    print('You start to set up...')
    time.sleep(2)
    print(f'{name} successfully set up a radio')
    print(f'enemies can now see you {name}, but this means you can extract!')
    radioSignalChoice()

clear_screen()
# Variable story parts
def radioSignalChoice():
    print('You make up 3 decisions in your head, and try to pick the best one')
    time.sleep(2)
    print('1 Find a weapon to fight the squads that now see you')
    print('2 Take down radio')
    print('3 leave')
    choice = chooseOption(3)
    print(choice)
    if choice == 1:
        findaweapon_radio()
    elif 2 == choice:
        destroyRadio()
    elif 3 == choice:
        leave()
    else:
        print("That wasn't a option! You instead implode from self conflict")

clear_screen()
def destroyRadio():
    print(f'{name} chooses to take the radio down')
    print('Hold on...')
    time.sleep(4)
    levelTwo()

clear_screen()
def findaweapon_radio():
    print('After being spotted by every squad, you choose to find a weapon')
    time.sleep(2)
    print('you find the building marked armory, how will you get in')
    time.sleep(3)
    print('1 Back door')
    print('2 Front door')
    print('3 roof hatch')
    print('4 dig..')
    choice = chooseOption(4)
    print(choice)
    if choice == 1:
        backDoor_Radio()
    elif 2 == choice:
        frontDoor()
    elif 3 == choice:
        skyLight()
    elif 4 == choice:
        dig()
    else:
        print("That wasn't a option! You instead implode from self conflict")

clear_screen()
def findaweapon_radio_again():
    print(f'{name} wants another weapon')
    time.sleep(2)
    print('you find the building marked armory, how will you get in')
    time.sleep(3)
    print('1 Back door')
    print('2 Front door')
    print('3 skylight')
    print('4 dig..')
    choice = chooseOption(4)
    print(choice)
    if choice == 1:
        backDoor_Radio_again_death()
    elif 2 == choice:
        frontDoor()
    elif 3 == choice:
        skyLight()
    elif 4 == choice:
        dig()
    else:
        print("That wasn't a option! You instead implode from self conflict")

clear_screen()
def backDoor_Radio():
    print('you decide to go into the back door')
    time.sleep(1)
    print('You sneak over to the back door, and noticed its unlocked')
    time.sleep(1)
    print('as you enter the building, you notice a large amount of enemies, fortunately, you sneak your way past, they dont pick up your radio signal for some reason')
    time.sleep(1)
    print('you are easily able to walk past the guards and take a weapon')
    print('You exit the building as quickly as you snuck in')
    time.sleep(1)
    levelTwoWeapon_Radio()

clear_screen()
def backDoor_Radio_again_death():
    print('you decide to go into the back door... again.')
    time.sleep(3)
    print('You sneak over to the back door, and noticed its unlocked... because it was before')
    time.sleep(4)
    print(
        'as you enter the building, you notice the large amount of enemies is still there, but this time, they instantly spot you')
    time.sleep(1)
    print("\033[1;31;40m You died! \n")

clear_screen()
def levelTwoWeapon():
    print('1 Find supplies (and go back)')
    print('2 Search for more enemies to attack')
    print('3 Try to establish radio signal')
    print('4 Leave')
    choice = chooseOption(4)
    print(choice)
    if 1 == choice:
        findsupplies2()
    elif 2 == choice:
        searchforenemies_weapon()
    elif 3 == choice:
        radioSignal_Weapon()
    elif 4 == choice:
        leave()

    else:
        print("That wasn't a option! You instead implode from self conflict")

clear_screen()
def levelTwoWeapon_Radio():
    print('1 Search for more enemies to attack')
    print('2 Find a weapon')
    print('3 Leave')
    choice = chooseOption(3)
    print(choice)
    if 1 == choice:
        searchforenemiesradio()
    elif 2 == choice:
        findaweapon_radio_again()
    elif 3 == choice:
        leave()

    else:
        print("That wasn't a option! You instead implode from self conflict")

clear_screen()
def searchforenemiesradio():
    print(f'{name} needs to search for enemies')
    time.sleep(1)
    print(
        f'while {name} makes their decision, you spot enemies in the distance, however, you notice they are already looking at you. wait a minute, they spotted you from your radio signal!')
    time.sleep(5)
    print("what was that loud pop?-")
    time.sleep(3)
    print('...')
    time.sleep(3)
    print(f'{name} was attacked, does {name} have a bandage, helmet, or armour plates?')
    print('1 Yes')
    print('2 No')
    choice = chooseOption(2)
    print(choice)
    if choice == 1:
        levelthree_attacked()

    elif 2 == choice:
        print(f'{name} does not have anything to protect them...')
        print("\033[1;31;40m You died! \n")



    else:
        print("You dont remember fast enough")

clear_screen()
def levelthree_attacked():
    print(f'{name} is wounded, but still alive')
    print("what will you do")
    time.sleep(1)
    print('1 Run for cover')
    print('2 Run into jungle')
    print('3 Stay put and fight')
    choice = chooseOption(3)
    print(choice)
    if 1 == choice:
        coverending()
    elif 2 == choice:
        runinjungle()
    elif 3 == choice:
        stayinjungle()

    else:
        print("That wasn't a option! You instead implode from self conflict")

clear_screen()
def coverending():
    print(f'{name} chooses to stay in cover')
    time.sleep(2)
    print("while in cover, you start to hear a sound booming in the distance")
    time.sleep(2)
    print("the extraction helicopter zooms by overhead, parting the trees with its rotor wash")
    time.sleep(2)
    print("the enemy squad flees panic-stricken as you run to the extraction helicopter")
    time.sleep(2)
    print("you get in the helicopter, and escape the warzone victorious")
    print(f'{name} escaped the warzone!')

clear_screen()
def runinjungle():
    print(f'{name} runs into jungle, leaving their weapon behind')
    time.sleep(3)
    print("as you jolt into the trees you find a small building to hide in")
    time.sleep(3)
    print("you bolt through the door of the building, inside, you find a motorcycle")
    time.sleep(3)
    print("You start the motorcycle and escape deeper into the jungle, you have escaped danger, but are now lost in the jungle")
    print(f'{name} escaped death, but not the warzone')
    time.sleep(3)

clear_screen()
def stayinjungle():
    print(f'{name} decides to stay in cover')
    print("you start to fight back, the enemies advance")
    time.sleep(3)
    print('The enemies know your location, you run out of ammo.')
    time.sleep(2)
    print("as you try and run, the enemies catch you and hold you captive")
    time.sleep(2)
    print(f'{name} is now subject to being held in the jungle by their captives!')
    print(f'you got the bad ending {name}!')


###################### SOME ASCII ART ############################

# ascii art citation
ASCII_ART = r"""

"""

###################### THE MAIN GAME LOOP ############################
# ------------------Game Loop ------------------------


while True:
    # introduce the game
    game_intro()

    # "Play again" user option
    print('\nWould you like to play again? Y/N')
    playAgain = input()
    if playAgain == 'Y' or playAgain == 'y':
        continue  # continue loop
    elif playAgain == 'N' or playAgain == 'n':
        break  # leave while loop
    else:
        print("Please read the instructions next time. Goodbye...")
        break

# End the game...
print("Quitting...")
sys.exit(0)
quit()
