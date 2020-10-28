read = input ("You have one new message. Do you want to read it? (y/n) ").lower()
if read == "y":
  print("Welcome Agent Pepper, read the information with care. You do not want to mis any information. ")
  rules = input ("There are some ground rules. If you make a mistake, you will die. So keep following the instructions. Do you understand? (y/n) ").lower()
  if rules == "y":
    print("Ok, let's do this...")
    print("You are about to meet Lady B in the café downstairs. She is member of a foreign secret service. So you need to be carefull. They might know that about your operation... ")
    alias = input ("Tell me, what name do you want to use if she asks your name? ")
    print("Oke,", alias, "that is a solid name. I like it" )
    country = input ("So we know your alias, but what is your nationality? ")
    print("You know that", country, "is a bit of a risk to take? But I trust you on this one." )
    hallway = print("We need to start moving. You need to go outside this room.")
    ans = input("You open the door and walk outside in to the hallway. Do you want go to the left side or the right? (left/right)? ")  
    if ans == "right":
      print("You bumb in to a house maid. She dropped something. You pick it up and say sorry to her.")
    elif ans == "left":
      print("You are going towards the elevator...")  
    ans = input ("You notice somebody in a suit staring at you. You can walk away or you can run? (walk/run) ")
    if ans == "walk":
      print("you manage to walk in to an open elevator and press the button. You look over your shoulder. The suited stranger opens the door accros your room. And walks in...")
      
    elif ans == "run": 
      print("You start to run... he screams that you need to stop. You try to reach the staircase. But he shoots... you died.")
       
  elif rules =="n":
      print("To bad. Now you die...")
    
else:
  print("Ok. Goodbey...")
