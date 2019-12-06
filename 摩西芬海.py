import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
mc.setBlocks(pos.x, pos.y, pos.z, pos.x+50, pos.y+50, pos.z+50, block.LAVA.id)
while True:
    pos = mc.player.getTilePos()
    mc.setBlocks(pos.x, pos.y, pos.z, pos.x+10, pos.y+70, pos.z+10, block.AIR.id)

#进海后，由于block变化，会出现一条路。

