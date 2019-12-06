import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
while True:
    pos = mc.player.getTilePos()
    mc.setBlocks(pos.x, pos.y, pos.z, pos.x+30, pos.y+30, pos.z+30, block.AIR.id)

    #清空玩家附近的物体，主要利用mcpi的setBlocks。