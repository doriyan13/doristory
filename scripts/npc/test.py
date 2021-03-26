# ParentID: 9010017
# ObjectID: 1000020
# Character field ID when accessed: 180000000
# Object Position X: -179
# Object Position Y: 95

response = sm.sendAskYesNo("Do you wanna Job Advance?")

if(response):
    sm.jobAdvance(sm.getChr())