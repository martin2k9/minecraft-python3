import mcpi.minecraft as minecraft
import mcpi.block as block
import random
while True:
    mc = minecraft.Minecraft.create()
    pos = mc.player.getTilePos()
    mc.setBlock(pos.x, pos.y-1, pos.z,18,random.randint(0,3))
    #