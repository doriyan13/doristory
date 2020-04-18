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
# faceColour = al.getFace() % 10 # - maybe relevant to hair but in hair it's switch up the eye's you can see
faceColour = 0
if al.getGender() == 0: # Male
    options = [20000, 20001, 20002, 20003, 20004, 20005, 20006, 20007, 20044, 20045, 20046, 20047, 20048, 20049, 20050, 20051, 20052, 20053, 20054, 20055, 20056]
else: # Female
    options = [20044] # sorry ladies, i care about the boys only

options = list(map(lambda x: x + faceColour, options))
answer = sm.sendAskAvatar("Choose your new eyes!", False, False, options)

mesos = chr.getLevel() * 2000000 # Taking my lvl and multiply it by 2,000,000 | for example lvl200 * 2,000,000 = 400,000,000

# ----------------------------------------------------------------------------------------------------------------------
# getting my char meso amount (Int)-
charMoney = chr.getMoney();
chrDisplay = "" # the amount of meso the character have
counter = 0 # will count 3 figures for the ','
# I created a while that going to move through the meso the char have and every 3 num's from the lowest num it's going to add "," and will also check it's isn"t the first num (highest in the num)
while charMoney > 0:
    counter +=1
    chrDisplay = str(charMoney % 10) + str(chrDisplay)

    if counter == 3:
        if (charMoney / 10) > 0:
            chrDisplay = "," + str(chrDisplay)
            counter = 0

    charMoney = (charMoney / 10)

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
