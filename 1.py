import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
mc.setblocks(pos.x+100,pos.y,pos.z+100,pos.x-100,pos.y,pos.z-100,0)