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

class map:
    name=""
    info=""
    open=True or False

#genevives manor
gmFront=map()
gmFront.name=("Genevives Front Entrance")
gmFront.info=("""A big room with floor to ceiling windows on one side, covered with heavy white a curtnd goldains.
The room is lit up with bright silver lamps, and the room smells faintly of flowers.
There’s a set of  ornate double doors on one end of the room. The cross above the door makes you uneasy.
Something in this room makes you uncomfortable.""")
gmFront.open=(True)
gmDining=map()
gmDining.name=("Genevives dining room")
gmDining.info=(""" a large room with a massive dining table in the centre. The table is always set, and all but one of the plates has a thick coating of dust,
 the clean setting being situated at the table’s head. The chandelier hanging above the table is sculpted to appear as twisting vines dotted with flowers in multiple shapes and colourings.""")
gmDining.open=(True)
gmBed=map()
gmBed.name=("The Bedroom Genevive gave you")
gmBed.info=("""a completely luxurious room where everything is freshly cleaned in a very meticulous manner. The bed is almost imposing with its size and is covered in thick, silky sheets, blankets and pillows.
 It almost looks like a cloud. A wardrobe sits against the opposite wall filled with wonderfully frilly dresses, though upon closer inspection sections of the wood appear rotted. 
Best not to try and move the furniture lest it collapse. The framed mirror in the corner, though it seems in better condition than the rest of the room, seems to taunt you with the room’s reflection. But somehow, you do not see yourself. """)
gmBed.open=(True)
gmHall=map()
gmHall.name=("The hallway")
gmHall.info=("")
gmHall.open=(True)
gmFood=map()
gmFood.name=("Genevives Kitchen")
gmFood.info=("")
gmFood.open=(True)
gmLounge=map()
gmLounge.name=("Genevives living room")
gmLounge.info=("")
gmLounge.open=(True)

#Cherry Pie forest
fClearing=map()
fClearing.name=("The Forest")
fClearing.info=("")
fClearing.open=(True)
fPath=map()
fPath.name=("The Forest")
fPath.info=("")
fPath.open=(True)



#circus
cOutside=map()
cOutside.name=("Outside the big tent")
cOutside.info=("")
cOutside.open=(True)
cTent=map()
cTent.name=("Inside the big Tent")
cTent.info=("")
cTent.open=(True)
cBstage=map()
cBstage.name=("Behind the curtains of the Tent")
cBstage.info=("")
cBstage.open=(True)
cDorms=map()
cDorms.name=("Inside the small tent")
cDorms.info=("")
cDorms.open=(True)
cAnimal=map()
cAnimal.name=("Behind the small tent")
cAnimal.info=("")
cAnimal.open=(True)
cOffice=map()
cOffice.name=("In the trailer")
cOffice.info=("")
cOffice.open=(True)


#Silas's estate
sGarden=map()
sEntrance=map()
slounge=map()
skitchen=map()
sBasement=map()
sCloset=map()

#arthurs cottage
aGarden=map()
aCottage=map()

print(gmFront.name)
print(gmFront.info)

print(gmDining.name)
print(gmDining.info)
