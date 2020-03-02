import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import time 
mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)
def drawLine(x1,y1,z1,x2,y2,z2,blockType,blockData):
pos = mc.player.getTilePos()
mcdrawing.drawLine(pos.x,pos.y,pos.z,pos.x,pos.y+20,pos.z,35,1)
mcdrawing.drawLine(pos.x,pos.y,pos.z,pos.x,pos.y+20,pos.z,35,2)
mcdrawing.drawLine(pos.x,pos.y,pos.z,pos.x,pos.y+20,pos,z,35,3)
time.sleep(5)
def drawCircle(x,y,z,blockType,blockData):
pos = mc.player.getTilePos()
mcdrawing.drawCircle(pos.x,pos.y+20,pos.z,426,4)
time.sleep(5)
def drawSpheres(x,y,z,radius,blockType,blockData):
pos = mc.player.getTilePos()
mcdrawing,drawSpheres(pos.x,pos.y+20,pos,z,15,30,5)
    

 


