import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
while True:
    pos = mc.player.getTilePos()
    mc.setBlock(pos.x, pos.y-1, pos.z, block.GLASS.id)  

    #当玩家在海面上或者陆地行走时，会在玩家脚下生成一个玻璃。