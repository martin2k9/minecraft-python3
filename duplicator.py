import glob
import random
import time

import mcpi.block as block
import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()
SIZEX = 10
SIZEY = 10
SIZEZ = 10
roomx = 1
roomy = 1
roomz = 1
def buildRoom(x,y,z):
    print("buildRoom")
def demolishRoom():
    print("demolisRoom")
def cleanRoom():
    print("cleaRoom")
def listFiles():
    print("listFiles")
def scan3D(filename,originx,originy,originz):
    print("scan3D")
def print3D(filename,originx,originy,originz):
    print("print3D")
# def menu():
#     print("menu")
#     time.sleep(1)
#     return random.randint(1,7)

def menu():
    while True:
        print("DOPLICATOR MENU")
        print("1.BULLD the duplicator")
        print("2.LIST files")
        print("3.SCAN from duplicator room to fileee")
        print("4.LOAD from file into duplicator room ")
        print("5.PRINT from  duplicalitor room to player.pos")
        print("6.CLEAN the duplocalitor room")
        print("7.DEMOLISH the duplocalitor room")
        print("8.QUIT")
        choice = int(input("please choose:"))
        if choice < 1 or choice > 8:
            print("Soory,pease choose a number between 1 and 8")
        else:
            return choice
def buildRoom(x,y,z):
    global roomx,roomy,roomz
    roomx = x
    roomy = y
    roomz = z
    mc.setBlocks(roomx,roomy,roomz,roomx+SIZEX+2,roomy+SIZEY+2,roomz+SIZEZ+2,block.GLASS.id)
    mc.setBlocks(roomx+1,roomy+1,roomz+1,roomx+SIZEX+1,roomy+SIZEY+1,roomz+SIZEZ+1,block.AIR.id)

anotherGo = True
while anotherGo:
    choice = menu()
    if choice == 1:
        pos = mc.player.getTilePos()
        buildRoom(pos.x,pos.y,pos.z)
    elif choice == 2:
        listFiles()
    elif choice == 3:
        filename = input("filename?")
        scan3D(filename,roomx+1,roomy+1,roomz+1)
    elif choice == 4:
        filename = input("filename?")
        print3D(filename,roomx+1,roomy+1,roomz+1)
    elif choice == 5:
        scan3D("scantemp",roomx+1,roomy+1,roomz+1)
        pos = mc.player.getTilePos()
        print3D("scantemp",roomx+1,roomy,roomz+1)
    elif choice == 6:
        cleanRoom()
    elif choice == 7:
        demolishRoom()
    elif choice == 8:
        anotherGo = False

    