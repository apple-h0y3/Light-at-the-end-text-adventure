#this is a text video game. 
import time# this will help with the suspensful pauses

startgame=input
opts1=""
opts2=""

print("In this game, decision points will show up like this: YES/NO Type your answer")
print("ready to start?")
print("START/START")
startgame("")
time.sleep(3)
print("\x1b[38;5;124m Annabelle. The eyes and mouth are windows to the soul.... ")
print("Never let anyone see inside unless you trust them to know what you are and not use it against you. \033[m")
time.sleep(5)
print("It's dark. A forest comes in and out of focus as you struggle to stand")
print("Annabelle...")
time.sleep(3)
print("\x1b[38;5;160m         Cover your face....\033[m")
print()
print()
print("you stand shakily. the voice sounds familiar for some reason.")
print("the forest is dark around you. tall trees stretchup towards the sky.")
print("The leaves rustle in the wind, and something waving in the wind catches your attention")
print("Its a piece of white fabric. it flutters in the breeze, and you have the urge to Grab it")
print("Type Grab")#this introduces how the player will be making decisions
opts1=input().lower()

if (opts1== "GRAB") or (opts1 == "grab") or (opts1 == "Grab"): #this works now!
    print("you grab the fabric and pull it over your face. it settles over your eyes.")
    print("check") # remove this later
else:
   print("you grab the fabric and pull it over your face. it settles over your eyes.")
   print()

print("Through the trees, you see lights flickering on a hill. they seem close.")
print("...")
print("...")
time.sleep(2)
print("... you hear a scratching noise ...")
print("...")
print("...")
time.sleep(2)
print("... you hear something moving in the forest behind you. It sounds like it's getting closer. ")
print("...")
print("RUN/STAY")g
opts2=input().lower()

if opts2 == "run":
    print("you run towards the hill, sprinting as it chases you. the lights get closer, and a house comes into view. The door swings open, and you dive through it, hearing scratching on the door as it swings shut behind you. ")
    print("")
    print("the house is bright on the inside. someone is moving around, but you're too tired to care.  your feet hurt from running, and your stomache rumbles from something that isn't quite hunger")
    print("")

# end of tutorial    
else:
    print("you stay rooted to the spot. Something lunges from the dark. you feel an intense pain, and then everything goes dark")
    print("GAME OVER...")
