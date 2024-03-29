# ObjectID: 1000013
# ParentID: 9000386
# Character field ID when accessed: 180000000
# Object Position X: 23
# Object Position Y: -104
if (sm.getChr().getLevel() >= 200):
    maps = [000,100,112,122,132,200,212,222,232,300,312,322,400,412,422,434,500,532,522,512,572,1000,1112,1212,1312,1412,1512,2000,2112,2218,2312,2412,2512,2712,3112,3122,3212,3312,3512,3712,3612,4112,4212,5112,6112,6512]
    selection = sm.sendNext("Which job would you like? "
                        +"\r\n #L0# Beginner #l "
                        +"\r\n #L1# Warrior #l "
                        +"\r\n #L2# Hero #l "
                        +"\r\n #L3# Paladin #l "
                        +"\r\n #L4# DarkKnight #l "
                        +"\r\n #L5# Magical Girl #l "
                        +"\r\n #L6# Toxic Mage #l "
                        +"\r\n #L7# OP Mage #l "
                        +"\r\n #L8# Big Healer #l "
                        +"\r\n #L9# BowMan <DaBoki~> #l "
                        +"\r\n #L10# Bow Master #l "
                        +"\r\n #L11# CrossBow Master #l "
                        +"\r\n #L12# Thief #l "
                        +"\r\n #L13# Night Lord #l "
                        +"\r\n #L14# Shadower #l "
                        +"\r\n #L15# Kirito #l "
                        +"\r\n #L16# Pirate #l "
                        +"\r\n #L17# Big Cannon #l "
                        +"\r\n #L18# Corsair aka Jack Sparrow #l "
                        +"\r\n #L19# Buccanneer aka Goku #l "
                        +"\r\n #L20# Jett #l "
                        +"\r\n #L21# Noblesse #l "
                        +"\r\n #L22# Dawn Warrior #l "
                        +"\r\n #L23# Blaze Wizard #l "
                        +"\r\n #L24# Wind Archer #l "
                        +"\r\n #L25# Night Walker #l "
                        +"\r\n #L26# Thunder Breaker #l "
                        +"\r\n #L27# Legend aka The last Air-Bander #l "
                        +"\r\n #L28# Aran #l "
                        +"\r\n #L29# Evan #l "
                        +"\r\n #L30# Mercedes #l "
                        +"\r\n #L31# Phantom #l "
                        +"\r\n #L32# Shade #l "
                        +"\r\n #L33# Lumi is love <3 #l "
                        +"\r\n #L34# Demon Slayer #l "
                        +"\r\n #L35# Demon Avanger #l "
                        +"\r\n #L36# Battle Mage #l "
                        +"\r\n #L37# Wild Hunter #l "
                        +"\r\n #L38# Mechanic #l "
                        +"\r\n #L39# Blaster #l "
                        +"\r\n #L40# Xenon #l "
                        +"\r\n #L41# Hayato #l "
                        +"\r\n #L42# Kanna #l "
                        +"\r\n #L43# Mihile #l "
                        +"\r\n #L44# Kaiser #l "
                        +"\r\n #L45# Angelic Buster #l ")
    sm.setJob(maps[selection])
    sm.getChr().maxSkills()
else:
    maps = [0,100,200,300,400,430,500,501,508,1000,1100,1200,1300,1400,1500,2000,2001,2100,2210,2300,2410,2500,2700,3100,3101,3200,3300,3500,3700,3600,4100,4200,6100,6500]
    selection = sm.sendNext("Which job would you like? "
                        +"\r\n #L0# Beginner #l "
                        +"\r\n #L1# Warrior #l "
                        +"\r\n #L2# Magician #l "
                        +"\r\n #L3# Bowman #l "
                        +"\r\n #L4# Thief #l "
                        +"\r\n #L5# Start Kirito #l "
                        +"\r\n #L6# Pirate #l "
                        +"\r\n #L7# Cannonneer #l "
                        +"\r\n #L8# Jett #l "
                        +"\r\n #L9# Nobless #l "
                        +"\r\n #L10# Dawn Warrior #l "
                        +"\r\n #L11# Blaze Wizard #l "
                        +"\r\n #L12# Wind Archer #l "
                        +"\r\n #L13# Thunder Breaker #l "
                        +"\r\n #L14# Legend #l "
                        +"\r\n #L15# Aran #l "
                        +"\r\n #L16# Evan #l "
                        +"\r\n #L17# Mercedes #l "
                        +"\r\n #L18# Phantom #l "
                        +"\r\n #L19# Shade #l "
                        +"\r\n #L20# Luminous #l "
                        +"\r\n #L21# Demon Slayer #l "
                        +"\r\n #L22# Demon Avenger #l "
                        +"\r\n #L23# Battle Mage #l "
                        +"\r\n #L24# Wild Hunter #l "
                        +"\r\n #L25# Blaster #l "
                        +"\r\n #L26# Xenon #l "
                        +"\r\n #L27# Hayato #l "
                        +"\r\n #L28# Kanna #l "
                        +"\r\n #L29# Kaiser #l "
                        +"\r\n #L30# Angelic Buster #l")
    sm.setJob(maps[selection])

sm.dispose()
#print(selection)

#if selection == 0:
 #   sm.giveItem(4000313, 1)
#elif selection == 1:
 #   sm.giveItem(4001129, 1)
#elif selection == 2:
 #   sm.giveItem(4001126, 1)
