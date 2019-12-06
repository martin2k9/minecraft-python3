#当玩家站在白地毯时，会被传送到红地毯上。
import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()
while True:
    time.sleep(3)
    pos = mc.player.getTilePos()  
    print(pos.x, pos.y, pos.z)
    if pos.x>=14 and pos.z>=-2:
        mc.player.setTilePos(13,6,5) 
        mc.postToChat('change!!!')  
    else:
        pass


