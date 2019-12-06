import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time
import mcpi.minecraftstuff as minecraftstuff
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)
mcdrawing.drawSphere(pos.x+10, pos.y+20, pos.z,50,block.TNT.id)

#在玩家上空生成一个TNT圆球。（慎用）