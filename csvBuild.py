import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
GAP = block.AIR.id
WALL = block.GOLD_BLOCK.id
FLOOR = block.GRASS.id
FILENAME = "mazel.csv"
f = open(FILENAME,"r")
pos = mc.player.getTilePos()
ORIGIN_x = pos.x+1
ORIGIN_y = pos.y
ORIGIN_z = pos.z+1
z = ORIGIN_z
for line in f.readlines():
    data = line.split(",")
    x = ORIGIN_x
    for cell in data:
        if cell == "0":
            b = GAP
        else:
            b = WALL
        mc.setBlock(x, ORIGIN_y, z, b)
        mc.setBlock(x, ORIGIN_y+1, z, b)
        mc.setBlock(x, ORIGIN_y-1, z, FLOOR)
        x = x+1
    z = z+1

