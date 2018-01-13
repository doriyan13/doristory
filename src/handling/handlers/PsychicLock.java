package handling.handlers;

import client.character.skills.PsychicLockBall;
import connection.OutPacket;

import java.util.ArrayList;
import java.util.List;

/**
 * Created on 1/13/2018.
 */
public class PsychicLock {
    public int skillID;
    public short slv;
    public int action;
    public int actionSpeed;
    public List<PsychicLockBall> psychicLockBalls = new ArrayList<>();

    public void encode(OutPacket outPacket) {
        outPacket.encodeInt(skillID);
        outPacket.encodeShort(slv);
        outPacket.encodeInt(action);
        outPacket.encodeInt(actionSpeed);
        for(PsychicLockBall plb : psychicLockBalls) {
            outPacket.encodeByte(1);
            plb.encode(outPacket);
        }
        outPacket.encodeByte(0);
    }
}
