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
    options = [33040, 30060, 32350, 33170, 30210, 33100, 30610, 30440, 30920, 30830, 30810, 30360, 30160, 30130, 30050, 30020]
else: # Female
    options = [32360, 34400, 31820, 34270, 31860, 34210, 34250, 34490, 31360]
options = list(map(lambda x: x + hairColour, options))
answer = sm.sendAskAvatar("Choose your new hairstyle!", False, False, options)

if answer < len(options):
    sm.changeCharacterLook(options[answer])
