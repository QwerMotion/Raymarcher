from vector import *
from Operations import *

def buildGrid(startScreen, direction1, direction2, GRID_WIDTH, GRID_HEIGHT):

    grid = []
    v1 = vecSub(direction1, startScreen)
    v2 = vecSub(direction2, startScreen)

    





    for y in range(GRID_HEIGHT):
      
        for x in range(GRID_WIDTH):

            addVector = vecAdd( vecMul(direction1, x) , vecMul(direction2, y) )
            newGridpoint = vecAdd(addVector, startScreen)
            grid.append(newGridpoint)            


           
    return grid
        

