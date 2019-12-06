import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
mc.setBlocks(pos.x-1, pos.y, pos.z-1, pos.x, pos.y+5, pos.z+10,426)
mc.setBlocks(pos.x-1, pos.y, pos.z-1, pos.x+10, pos.y+5, pos.z, 426)
mc.setBlocks(pos.x+10, pos.y, pos.z, pos.x, pos.y+5, pos.z+10,426)
mc.setBlocks(pos.x+10, pos.y, pos.z, pos.x+10, pos.y+5, pos.z, 426)
mc.setBlocks(pos.x, pos.y, pos.z, pos.x, pos.y+4, pos.z+9,0)
mc.setBlocks(pos.x, pos.y, pos.z, pos.x+9, pos.y+4, pos.z,0)
mc.setBlocks(pos.x+9, pos.y, pos.z, pos.x, pos.y+4, pos.z+9, 0)
mc.setBlocks(pos.x+9, pos.y, pos.z, pos.x+9, pos.y+4, pos.z,0)

    