import time
#shortcuts

# option tags
opts3=input
opts4=input 
class Character:
    name = ""
    dead = False
    vamp = True or False

gv=Character()#genevive uses green speaking text
gv.name = "Genevive"
gv.dead = False
gv.vamp = False
rm=Character()#ringmaster uses purple speaking text
rm.name="The Ringmaster"
rm.dead=False
rm.vamp=False
sil=Character()#silas uses Red speaking text
sil.name="Silas"
sil.dead=False
sil.vamp=True
ar=Character()#arthur uses cyan speaking text
ar.name="Arthur"
ar.dead=False
ar.vamp=False
cas=Character()
cas.name="Casper"
cas.dead=False
cas.vamp=False
#annabelle speaks in pink text. she thinks in a darker pink


print("")
print("you run towards the hill, sprinting as it chases you. the lights get closer, and a house comes into view. The door swings open, and you dive through it, hearing scratching on the door as it swings shut behind you. ")
print("")
print("the house is bright on the inside. someone is moving around, but you're too tired to care.  your feet hurt from running, and your stomache rumbles from something that isn't quite hunger")
print("")
time.sleep(2)
print("")
print("A bright voice sounds from behind you")
print('\033[32mWell hello there!\033[0m')

time.sleep(1)
print("you struggle to your feet as you take in your surroundings. the room is lit up with bright lamps,")
print("and windows covered by heavy white and gold curtains line one wall. you can see the beautiful tapestries")
print("along the other wall, and the open double doors on the other end of the room")
time.sleep(3)
print("\033[32myou know, its polite to greet your host\033[0m")
print("you spin in surprise. the voice is coming from a woman standing in front of the door. she's dressed in a grey skirt and white top, with a black apron")
time.sleep(1)
print("Who are you / STAY AWAY")
opts3("")
if (opts3 == "Who are you") or (opts3=="who are you") or (opts3 == "who"):
    print("\x1b[38;5;200mOh.... who are you?\033[0m")
    time.sleep(1)
    print("\033[32m oh, how unpolite of me! My name is Genevive.\033[0m")
elif (opts3 == "STAY AWAY") or (opts3=="Stay Away") or (opts3 == "stay away"):
    print("\x1b[38;5;200mSTAY AWAY FROM ME!!!!\033[0m")
    time.sleep(1)
    print("\033[32m oh,you don't need to be afraid of me. My name is Genevive.\033[0m")
    print("something about how homely and nice she looks makes you feel safe.")
else:
    print("\x1b[38;5;200mSTAY AWAY FROM ME!!!!\033[0m")
    time.sleep(1)
    print("\033[32m oh,you don't need to be afraid of me. My name is Genevive.\033[0m")
    print("something about how homely and nice she looks makes you feel safe.")
