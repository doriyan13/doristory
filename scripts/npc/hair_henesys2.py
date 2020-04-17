# Character field ID when accessed: 100000104
# ObjectID: 1000001
# ParentID: 1012104
# Object Position Y: 132
# Object Position X: -151
#henesys hair salon - Brittany

#Eye selection:
#20044 -bright eyes (my favorite)
#20037 - evan eyes
#20040 - Piercing gaze
options = []

al = chr.getAvatarData().getAvatarLook()
faceColour = al.getFace() % 10

if al.getGender() == 0: # Male
    options = [20044, 20045, 20046, 20044]
else: # Female
    options = [20044] # sorry ladies, i care about the boys only

options = list(map(lambda x: faceColour + x, options))
answer = sm.sendAskAvatar("Choose your new eyes!", False, False, options)

mesos = chr.getLevel() * 2000000 # Taking my lvl and multiply it by 2,000,000 | for example lvl200 * 2,000,000 = 400,000,000

# ----------------------------------------------------------------------------------------------------------------------
# getting my char meso amount (Int)-
charMoney = chr.getMoney();

# configuring all the parts of the char meso:
chrBillions = charMoney / 1000000000 # getting the Billions
chrMillions = ((charMoney - (chrBillions*1000000000)) /1000000) # getting the millions
chrThousants = ((charMoney - (chrBillions * 1000000000) - (chrMillions * 1000000)) / 1000) # getting the thousents
chrHunderds = (charMoney - (chrBillions*1000000000) - (chrMillions*1000000) - (chrThousants * 1000)) # getting the hunderds

# if the value isn't 3 figures(Millions) -
if chrMillions < 100:
    if chrMillions > 10: chrMillionsExtra = str("0" + str(chrMillions)) # In Python you can't really have few conditions in the same if, so you must nest them!
elif chrMillions < 10: chrMillionsExtra = "00" + str(chrMillions)
else: chrMillionsExtra = chrMillions

# if the value isn't 3 figures(Thousents) -
if chrThousants < 100:
    if chrThousants > 10: chrThousentsExtra = str("0" + str(chrThousants))
elif chrThousants < 10: chrThousentsExtra = "00" + str(chrThousants)
else: chrThousantsExtra = chrThousants

# if the value isn't 3 figures(Hunderds) -
if chrHunderds < 100:
    if chrHunderds > 10: chrHunderdsExtra = str("0" + str(chrHunderds))
elif chrHunderds < 10: chrHunderdsExtra = "00" + str(chrHunderds)
else: chrHunderdsExtra = chrHunderds

chrDisplay= ""
if charMoney > 999999999: chrDisplay = str(chrBillions) + "," +str(chrMillionsExtra) + "," + str(chrThousants) + "," + str(chrHunderdsExtra) #converting it to a String for display
elif charMoney > 999999: chrDisplay = str(chrMillions) + "," + str(chrThousants) + "," + str(chrHunderdsExtra)
elif charMoney > 999: chrDisplay = str(chrThousants) + "," + str(chrHunderdsExtra)
elif charMoney < 1000: chrDisplay = str(chrHunderds)

# ----------------------------------------------------------------------------------------------------------------------
# display the amount of meso you must pay in  pretty way -
mesoDisplay = str(mesos/1000000) + ",000,000"

response = sm.sendAskYesNo("it's cost #r" + mesoDisplay + "#k mesos if you want to change\r\nYou have #b" + str(chrDisplay) + "#k")
if response:
    if sm.getMesos() > mesos:
        sm.deductMesos(mesos)
        al.setFace(options[answer])
        sm.changeCharacterLook(options[answer])
        sm.sendSayOkay("Enjoy the new look:D")
    else:
        sm.sendSayOkay("you don't have enough meso, sorry")
else:
    sm.sendSayOkay("you cheap Fuck!")
