package net.swordie.ms;

/**
 * Created on 2/18/2017.
 */
public class ServerConfig {

    public static final int USER_LIMIT = 500;
    public static final byte WORLD_ID = 2; // bera -1
    public static final String SERVER_NAME = "DoriStory";
    public static final String EVENT_MSG = "#bDoriStory#k v176\r\nThe Boss";
    public static final String RECOMMEND_MSG = "I recommend this world to you.";
    public static final int MAX_CHARACTERS = 30;

    public static final boolean DEBUG_MODE = true;
    public static final boolean AUTO_CREATE_UNCODED_SCRIPTS = true; // if this is enabled then when a player runs into uncoded scripts a file with basic info will be created
    public static final char ADMIN_COMMAND = '!';
    public static final char PLAYER_COMMAND = '@';
}
