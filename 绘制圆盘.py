import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)
mcdrawing.drawCircle(pos.x, pos.y+20, pos.z,10,block.WOOL.id, 3)

#在玩家面前绘制圆环。