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
gmFront.name("Genevives Front Entrance")
gmFront.info("")
gmFront.open(True)
gmDining=map()
gmDining.name("Genevives dining room")
gmDining.info("")
gmDining.open(True)
gmBed=map()
gmBed.name("The Bedroom Genevive gave you")
gmBed.info("")
gmBed.open(True)
gmHall=map()
gmHall.name("The hallway")
gmHall.info("")
gmHall.open(True)
gmFood=map()
gmFood.name("Genevives Kitchen")
gmFood.info("")
gmFood.open(True)
gmLounge=map()
gmLounge.name("Genevives living room")
gmLounge.info("")
gmLounge.open(True)

#Cherry Pie forest
fClearing=map()
fClearing.name("The Forest")
fClearing.info("")
fClearing.open(True)
fPath=map()
fPath.name("The Forest")
fPath.info("")
fPath.open(True)



#circus
cOutside=map()
cOutside.name("Outside the big tent")
cOutside.info("")
cOutside.open(True)
cTent=map()
cTent.name("Inside the big Tent")
cTent.info("")
cTent.open(True)
cBstage=map()
cBstage.name("Behind the curtains of the Tent")
cBstage.info("")
cBstage.open(True)
cDorms=map()
cDorms.name("Inside the small tent")
cDorms.info("")
cDorms.open(True)
cAnimal=map()
cAnimal.name("Behind the small tent")
cAnimal.info("")
cAnimal.open(True)
cOffice=map()
cOffice.name("In the trailer")
cOffice.info("")
cOffice.open(True)


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