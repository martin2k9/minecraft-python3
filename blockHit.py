import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()
diamond_pos = mc.player.getTilePos()
diamond_pos.x = diamond_pos.x + 1
mc.setBlock(diamond_pos.x, diamond_pos.y, diamond_pos.z, block.DIAMOND_BLOCK.id)
def checkHit():

    print(diamond_pos)
    events = mc.events.pollBlockHits()
    for e in events:
        print("e:" + e)
        pos2 = e.pos
        print("pos2:" + pos2)
        if pos2.x == diamond_pos.x and pos2.y == diamond_pos.y and pos2.z == diamond_pos.z:
            mc.postToChat("HIT")
while True:
    time.sleep(1)
   #checkHit()
    es1 = mc.events.pollBlockHits()
    print(es1)
