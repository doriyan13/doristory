# Natalie - Henesys Hair Salon
# Male: Aran cut, Catalyst, Evan hair (m), gaga hair, shaggy wax, the coco, the mo rawk
# Female: Dual blade, front braid, grace, hime, laguna beach, lively wave, long with bangs, wavy bob, wavy ponytail
#30810 – Soft Wolf Hair
#30830 – Alex
#30920 – Short Top Tail
#37160 – Fluffy Fringe Hair - a girl hair style but you can give it to boy that way haha
#30440 – Fury
#30360 – Spiky Tail
#30340 – Tristan
#30330 - Cabana Boy
#30160 – Trip Scratch
#30130 – Antagonist
#30050 – Metro
#30020 – Rebel
options = []

al = chr.getAvatarData().getAvatarLook()
hairColour = al.getHair() % 10
if al.getGender() == 0: # Male
    options = [33150,33151,33154,33152,33040, 30060, 32350, 33170, 30210, 33100, 30610, 30440, 30920, 30830, 30810, 30360, 30160, 30130, 30050, 30020,33510,33440,33400,36490,34213,33270,36704,36597,37313,34372,34381,34450,32390,32410]
    #options = [30000, 30010, 30020, 30030, 30040, 30050, 30060, 30070, 30080, 30090, 30100, 30110, 30120, 30130, 30140, 30150, 30160, 30170, 30180, 30190, 30200, 30210, 30220, 30230, 30240, 30250, 30260, 30270, 30280, 30290, 30300, 30310, 30320, 30330, 30340, 30350, 30360, 30370, 30400, 30410, 30420, 30430, 30440, 30450, 30460, 30470, 30480, 30490, 30510, 30520, 30530, 30540, 30550, 30560, 30580, 30590, 30600, 30610, 30620, 30630, 30640, 30650, 30660, 30670, 30680, 30700, 30710, 30730, 30750, 30760, 30770, 30790, 30800, 30810, 30820, 30830, 30840, 30850, 30860, 30870, 30880, 30890, 30900, 30910, 30930, 30940, 30950, 30960, 30970, 30980, 30990, 33000, 33010, 33020, 33030, 33040, 33070, 33080, 33100, 33120, 33130, 33140, 33150, 33160, 33170, 33210, 33240, 33250, 33260, 33010, 33050, 33060, 33090, 33110, 33180, 33190, 33200, 33220, 33230, 33270, 33280, 33290, 33300, 33310, 33320, 33340, 33350, 33380, 33390, 33420, 33430, 33480, 33510, 33520]
else: # Female
    options = [32360, 34400, 31820, 34270, 31860, 34210, 34250, 34490, 31360]
options = list(map(lambda x: x + hairColour, options))
answer = sm.sendAskAvatar("Choose your new hairstyle!", False, False, options)

if answer < len(options):
    sm.changeCharacterLook(options[answer])

#hair colors change for the hair!
hair_Colors = []
for i in range(5):
    hair_Colors.append(options[answer] + i)

options2 = list(map(lambda x: x + 0, hair_Colors))
answer2 = sm.sendAskAvatar("Choose your new color", False, False, options2)

if answer2 < len(options2):
    sm.changeCharacterLook(options2[answer2])