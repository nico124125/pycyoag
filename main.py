######################### IMPORTING MODULES/PACKAGES ###############################
import random
import time, sys
# add other imports like sound, math, etc. here

#test push
#tes pull


# pauses game until user presses enter



name = input("Enter your name soilder! ")



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
    #time.sleep(0.5)
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
    mylist = ["Death" , "landing" , "landing" , "landing" , "landing" , "landing" , "landing"]
    if (random.choice(mylist)) == "Death" :
        print(f'{name}s parachute ripped!')
        print("You Died!")
        
    else:
        print('You have successfully landed')
    
        # list players options
        print()
        print('You are now in the warzone, What will you do?')
        print('  1 Seek Enemies')
        print('  2 Find Supplies')  
        print('  3 leave')
        print('  4 Go towards strange fog...')
    
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
            print("That wasn't a option! You died from a enemy squad.")


def warZone_nointro():
    print()
    print('You are now in the warzone, What will you do?')
    print('  1 Seek Enemies')
    print('  2 Find Supplies')
    print('  3 leave')
    print('  4 Go towards strange fog...')

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
        print("That wasn't a option! You died from a enemy squad.")

def findSupplies(): 
    print("You find it best to find supplies")
    mylist = ["Water" , "Water" , "Water" , "Water" , "Water" , "Bandage" , "Bandage" , "Bandage" , "Bandage" , "Bandage" , "Nuke Detonator"]
    result = random.choice(mylist)
    if (result) == "Water" :
        print(f'{name} finds some water, Should be useful...')
        time.sleep(0.5)
        print()
        print('You have now have some water, but still a objective to complete, what will you do?')
        print('  1 Seek Enemies')
        print('  2 Go towards strange fog...')
        choice = chooseOption(2)
        print(choice)
        if choice == 1:
            seekEnemies()
        elif 2 == choice:
            amazingChoice()
        else:
            print("That wasn't a option! You died from a enemy squad.")
        
    elif (result) == "Bandage":
        
        print(f'{name} finds a bandage, Hopefully wont need it...')
        time.sleep(0.5)
        print()
        print('You have now have a bandage, but still a objective to complete, what will you do?')
        print('  1 Seek Enemies')
        print('  2 Go towards strange fog...')
        choice = chooseOption(3)
        time.sleep(0.5)
        print(choice)
        if choice == 1:
            seekEnemies()
        elif 2 == choice:
         amazingChoice()
        else:
            print("That wasn't a option! You died from a enemy squad.")
        
    if  (random.choice(mylist)) == "Nuke Detonator":
        print(f'{name} finds a.. Nuke Detonator??')
        print(f'after getting to a safe distance, {name} won the game.')
    


  
# rename function to reflect your actual location/scene/action
def seekEnemies():
    print('You think its best to find enemy squads and eliminate them')
    time.sleep(2)
    print('as you sneek around the corner of a building, You spot a enemy squad. What will you do?')
    print('1 Use your supplied weapon')
    print('2 Throw a rock')  
    print('3 airstrike')
    choice = chooseOption(3)
    print(choice)
    if choice == 1:
        UseWeapon()
    elif 2 == choice:
        RockThrow()
    elif 3 == choice:
        airStrike1()

    else:
        print("That wasn't a option! You died from a enemy squad.")

def leave():
    mylist = ["leave", "death"]
    if (random.choice(mylist)) == "leave" :
        print(f'although {name} has just landed, they have decided to leave')
    else:
        print(f'{name} was attacked trying to flee!')
        # handle player's selection to jump to other locations/scenes/actions

        
def UseWeapon():
    print('Of course! You will use your supplied weapon')
    time.sleep(1)
    print('wait a minute, I dont have a supplied weapon.')
    print("the squad spots you.")
    print(f'{name} died!')
    
def RockThrow():
    print(f'{name} thinks it is best to throw a rock at the squad')
    time.sleep(1)
    print(f'{name} throws the rock')
    time.sleep(2)
    mylist = ["Hit" , "Miss"]
    if (random.choice(mylist)) == "Miss":
        print(f'{name} missed!')
        print("you died!")
        
    else:
        print(f'{name} hits a squad member with the rock')
        time.sleep(1)
        print ('they fall to the ground unconscious, but now the squad can see you')
        time.sleep(1)
        print ('You need to call in a airstrike!')
        airStrike()
    
def airStrike():
    print(f'{name} calls in a airstrike')
    time.sleep(1)
    print('The airstrike is inbound, so you take cover')
    time.sleep(1)
    print('the airstrike wipes the squad!')
    levelTwo()
    
    
def airStrike1():
    print(f'{name} calls in a airstrike')
    time.sleep(2)
    mylist = ["Hit" , "Miss"]
    if (random.choice(mylist)) == "Miss":
        print('the pilot missed the airstrike!')
        print(f'The squad spots {name} and starts firing')
        print("you died!")
    else:
        print("You spot the jet in the distance, it bursts through the sky and releases it's payload")
        time.sleep(2)
        print("Direct hit! the squad is no more!")
        levelTwo()
    
    
    # handle player's selection to jump to other locations/scenes/actions
def amazingChoice():
    print(f'{name} finds it best to go into the strange looking green fog for some reason.')
    time.sleep(3)
    print(f'{name} finds the fog smells kind of funny. Im sure its fine.')
    time.sleep(1)
    print()
    print('Well, that was a waste fo teim')
    print('1 toward foog')
    
    # handle player's selection to jump to other locations/scenes/actions
    choice = chooseOption(205)
    print(choice)
    if choice == 1:
        amazingChoice1()
    else:
        print("htat wsnt na topion! ouy iedd form sqad")


def amazingChoice1():
    print(f'{name} fiend best fog. some.. reason..')
    time.sleep(3)
    print(f'{name} fog funny')
    time.sleep(1)
    print()
    print('wallethatwasaswasteoftiem')
    print(' e')
    print(' efiandsupl')  
    print('a')
    print('foog')
    print(f'{name} Died from fog!')
 


# rename function to reflect your actual location/scene/action

    


# rename function to reflect your actual location/scene/action
def levelTwo():
    print("you have made it past the first squad, what will you do now")
    time.sleep(3)
    print('1 Find a weapon')
    print('2 Find supplies')
    print('3 Search for more enemies to attack')
    print('4 Try to establish radio signal')
    print('5 Leave')
    choice = chooseOption(3)
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



# Find A weapon story
def findaWeapon():
    print('You decide that to be in a warzone you probably need a weapon')
    time.sleep(2)
    print('you find a building marked armory, so you assume its a armory, how will you get in')
    time.sleep(3)
    print('1 Back door')
    print('2 Front door')
    print('3 skylight')
    print('4 dig..')
    choice = chooseOption(3)
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

def backDoor():
    print('you decide to go into the back door')
    time.sleep(1)
    print('You sneek over to the back door, and noticed its unlocked')
    time.sleep(1)
    print('as you enter the building, you notice a large amount of enemies, fortunately, you look the part')
    time.sleep(1)
    print('you are easily able to walk past the gaurds and take a weapon')
    print('You exit the building as quickly as you snuck in')
    time.sleep(1)
    levelTwoWeapon()
    #########INSERT COPY OF ORIGINAL OPTIONS SO THAT THE PLAYER NOW HAS A WEAPON#########
def frontDoor():
    print(f'In the movies they always gaurd the back door, so {name} decides to go through the front')
    time.sleep(1)
    print("you walk in the front door...")
    time.sleep(5)
    print("as you step through the entrance, every single gaurd within the building looks directly at you then pauses.")
def skyLight():
    print(f'{name} thinks they are sneaky, so they repel up to the roof and attempt to open the skylight')
    time.sleep(1)
    print('Unfortunately, you are not on the Impossible Mission Force so you fall through the glass and hit the ground')
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
        print('3 Try to establish radio signal')
        print('4 Leave')
        choice = chooseOption(3)
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
        print('3 Try to establish radio signal')
        print('4 Leave')
        choice = chooseOption(3)
        print(choice)
        if choice == 1:
            findaWeapon()
        elif 2 == choice:
            searchforenemies()
        elif 3 == choice:
            radioSignal()
        elif 4 == choice:
            leave()

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
        choice = chooseOption(3)
        print(choice)
        if choice == 1:
            findaWeapon()
        elif 2 == choice:
            searchforenemies()
        elif 3 == choice:
            radioSignal()
        elif 4 == choice:
            leave()


# Search for bad enemies story
def searchforenemies():
    print("Not done yet :)")

# Try to establish a radio signal story
def radioSignal():
    print(f'{name} chooses to establish a radio signal')
    time.sleep(2)
    print('You start to set up...')
    time.sleep(2)
    print(f'{name} successfully set up a radio')
    print(f'enemies can now see you {name}')
    radioSignalChoice()

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

def destroyRadio():
    print(f'{name} chooses to take the radio down')
    print('Hold on...')
    time.sleep(4)
    levelTwo()

def findaweapon_radio():
    print('After being spotted by every squad, you choose to find a weapon')
    time.sleep(2)
    print('you find a building marked armory, so you assume its a armory, how will you get in')
    time.sleep(3)
    print('1 Back door')
    print('2 Front door')
    print('3 skylight')
    print('4 dig..')
    choice = chooseOption(3)
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

def findaweapon_radio_again():
    print(f'{name} wants another weapon')
    time.sleep(2)
    print('you find a building marked armory, so you assume its a armory, how will you get in')
    time.sleep(3)
    print('1 Back door')
    print('2 Front door')
    print('3 skylight')
    print('4 dig..')
    choice = chooseOption(3)
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

def backDoor_Radio():
    print('you decide to go into the back door')
    time.sleep(1)
    print('You sneak over to the back door, and noticed its unlocked')
    time.sleep(1)
    print('as you enter the building, you notice a large amount of enemies, fortunately, you sneak your way past, they dont spot your radio signal for some reason')
    time.sleep(1)
    print('you are easily able to walk past the guards and take a weapon')
    print('You exit the building as quickly as you snuck in')
    time.sleep(1)
    levelTwoWeapon_Radio()
def backDoor_Radio_again_death():
    print('you decide to go into the back door... again.')
    time.sleep(3)
    print('You sneak over to the back door, and noticed its unlocked... because it was before')
    time.sleep(4)
    print('as you enter the building, you notice the large amount of enemies is still there, but this time, they instantly spot you')
    time.sleep(1)
    print('you died!')






def levelTwoWeapon():
    print('1 Find supplies (and go back)')
    print('2 Search for more enemies to attack')
    print('3 Try to establish radio signal')
    print('4 Leave')
    choice = chooseOption(3)
    print(choice)
    if 1 == choice:
        findsupplies2()
    elif 2 == choice:
        searchforenemies()
    elif 3 == choice:
        radioSignal()
    elif 4 == choice:
        leave()

    else:
        print("That wasn't a option! You instead implode from self conflict")

def levelTwoWeapon_Radio():
    print('1 Find supplies')
    print('2 Search for more enemies to attack')
    print('3 Leave')
    choice = chooseOption(3)
    print(choice)
    if 1 == choice:
        findsupplies2()
    elif 2 == choice:
        searchforenemiesradio()
    elif 3 == choice:
        leave()

    else:
        print("That wasn't a option! You instead implode from self conflict")

def searchforenemiesradio():
    print(f'{name} needs to search for enemies')
    time.sleep(1)
    print(f'while {name} makes their decision, you spot enemies in the distance, however, you notice they are already looking at you. wait a minute, they spotted you from your radio signal!')
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
        print('you died!')



    else:
        print("You dont remember fast enough")

def levelthree_attacked():
    print(f'{name} is wounded, but still alive')
    print("what will you do")
    time.sleep(1)
    print('1 Find supplies')
    print('2 Search for more enemies to attack')
    print('3 Try to establish radio signal')
    print('4 placeholders^')
    choice = chooseOption(3)
    print(choice)











###################### SOME ASCII ART ############################

# ascii art citation
ASCII_ART = r"""
    
"""



              

###################### THE MAIN GAME LOOP ############################
#------------------Game Loop ------------------------



while True:
    # introduce the game
    game_intro()

    # "Play again" user option
    print('\nWould you like to play again? Y/N')
    playAgain = input()
    if playAgain == 'Y' or playAgain == 'y':
        continue    #continue loop
    elif playAgain == 'N' or playAgain == 'n':
        break       #leave while loop
    else:
        print("Please read the instructions next time. Goodbye...")
        break



# End the game...
print("Quitting...") 
sys.exit(0)
quit()
