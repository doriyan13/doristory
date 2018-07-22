# Middle of the Strait | 141060000
from net.swordie.ms.client.character.skills.temp import CharacterTemporaryStat
mount = CharacterTemporaryStat.RideVehicle
rienaSkiff = 1930000

def init():
    if sm.hasCTS(mount) and sm.getnOptionByCTS(mount) != rienaSkiff:
        sm.removeCTS(mount)
    sm.rideVehicle(rienaSkiff)
    sm.dispose()