# Author: Tyler Mestery
#
import random
import server
import time

import mcpi.minecraft as minecraft
import mcpi.block as block

layers = 10 # how high our volcano is going to be
vec = (0, 0, 0) # the starting point for our volcano

mc = minecraft.Minecraft.create()
mc.setBlocks(vec[0], vec[1], vec[2],100,100,100,block.AIR) # let's make some space for our valcano

for layer in range(0,layers): # build the volcano
    mc.setBlocks(layer+vec[0], layer+vec[1], layer+vec[2], vec[0]+(2*layers)-layer, vec[1]+layer, vec[2]+(2*layers)-layer, block.STONE)
    time.sleep(1)

count = 0
while count < (layers*layers*3): # add some random blocks on the top to make it look a bit more real
    x = random.randint(vec[0], vec[0]+(2*layers)+1)
    z = random.randint(vec[2], vec[2]+(2*layers)+1)
    mc.setBlock(x, layers+10, z, block.GRAVEL)
    time.sleep(0.01)
    count+=1

while True: # get the lava flowing!
    mc.setBlocks(vec[0]+int(layers)-1, vec[1]+layers, layers-1, vec[0]+int(layers), vec[1]+layers, layers+1, block.LAVA_FLOWING)
    time.sleep(1)