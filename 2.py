import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
mc.setBlocks(pos.x, pos.y, pos.z, pos.x+20, pos.y+3, pos.z+20,0)