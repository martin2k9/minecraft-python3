
import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff

mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)
size = 10

def line():
    pos = mc.player.getTilePos()
    mcdrawing.drawLine(pos.x, pos.y, pos.z, pos.x+size, pos.y+size, pos.z+size, block.WOOL.id, 3)


while True:
    for a in range(3):
        line()
        size+=1

 #在玩家面前出现一条阶梯。       