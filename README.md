# Minecraft-NBot
Minecraft bot(s) program written in Javascript using Mineflayer.

# TODO 

Lumberjack command
\
Mineflayer/Discord.js communication
\
Disable what the bot is doing before executing the command to prevent it from crashing.
\
Make the bot walk every 10 minutes to prevent it from getting disconnected and back to its original position.

# 
\
https://github.com/PrismarineJS/mineflayer
\
\
it being used in game:\
https://www.youtube.com/watch?v=qJJU__idFao
\
\
what it should look like:\
https://www.youtube.com/watch?v=AYIcSEGx2EY

# Commands
all commands are only runnable by the botowner name\
You can also control the bot on https://localhost:5001 - https://localhost:5099 (meaning max 99 bots)\
command (args1) = required arguments\
command {args1} = not required but allowed\
\
bot show villagers\
    shows nearby villagers\
\
bot show inventory\
    shows nearby villagers' trading inventory\
    
say (message)\
    makes the bot chat the message\
\
bot comexyz (x) (y) (z)\
    makes the bot pathfind to the xyz coordinates\
\
bot come (botname), bot come all\
    makes the bot pathfind to your position\
\
eval (code)\
    runs a javascript code on the bot. if code errors, it will display in chat\
\
equiparmor\
    equips best armor. sometimes doesnt wear best armor\
\
bot roam\
    turns roaming on and off\
    walk randomly\
\
bot autototem\
    enables autototem, automatically equips totem\
\
bot autofish\
    turns autofishing on and off\
    makes the bot look at water and start auto fishing\
\
bot attack (targetname)\
    attacks a player using the item currently held by the bot\
    for better effect, equip a weapon first\
\
line up\
    makes the bots line up shoulder to shoulder\
\
equipblock (itemname)\
    equips an item onto the bot's hand\
\
throwblock (itemname)\
    drops an item from the bot's inventory\
\
tellinventory\
    tells what item is inside the bot's inventory\
\
bot mine (blockname)\
    mines the nearest block with that name\ 

