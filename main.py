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
    mylist = ["Death" , "landing"]
    if (random.choice(mylist)) == "Death" :
        print(f'{name} forgot to pull their parachute!')
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
        print('  3 Go towards strange fog...')
        choice = chooseOption(2)
        print(choice)
        if choice == 1:
            seekEnemies()
        elif 2 == choice:
            amazingChoice()
        else:
            print("That wasn't a option! You died from a enemy squad.")
        
    elif random.choice(mylist) == "Bandage":
        
        print(f'{name} finds a bandage, Hopefully wont need it...')
        time.sleep(0.5)
        print()
        print('You have now have a bandage, but still a objective to complete, what will you do?')
        print('  1 Seek Enemies')
        print('  2 Build shelter')
        print('  3 Go towards strange fog...')
        choice = chooseOption(3)
        time.sleep(0.5)
        print(choice)
        if choice == 1:
            seekEnemies()
        elif 2 == choice:
            buildShelter()
        elif 3 == choice:
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

def leave():
    mylist = ["leave", "death"]
    if (random.choice(mylist)) == "leave" :
        print(f'although {name} has just landed, they have decided to leave')
    else:
        print(f'{name} was attacked trying to flee!')
        # handle player's selection to jump to other locations/scenes/actions
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
def anotherLocation3():
    print('continue your story...')

# rename function to reflect your actual location/scene/action
def anotherLocation4():
    print('continue your story...')







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
