from Operations import vecSub, vecAdd, vecMul
from vector import Vec
from grid import buildGrid




#COORDINATE SYSTEM AS FOLLOWS
"""

z increases towards your face

z--------------------->x+
|
|
|
|
|
|
y +

"""

GRID_WIDTH = 1920
GRID_HEIGHT = 1080
GRID_SIZE = 0.01

startScreen = Vec(0, 0, 0, "topLeft")
direction1 = Vec(GRID_SIZE, 0, 0, "left_right")
direction2 = Vec(0, GRID_SIZE, 0, "up_down")



#build a grid of points
grid = buildGrid(startScreen, direction1, direction2, GRID_WIDTH, GRID_HEIGHT)



"""

v1 = vecSub(direction1, startScreen)
v2 = vecSub(direction2, startScreen)

grid = [startScreen]





for y in range(GRID_HEIGHT):
    v1.add(v1)
    for x in range(GRID_WIDTH):
        v2.add(v2)
        
        gridPointv1 = vecAdd(startScreen, v1)
        gridPointv2 = vecAdd(startScreen, v2)

        finalGridPoint = vecAdd(gridPointv1, gridPointv2)
        grid.append(finalGridPoint)
"""
        
  
        
        
        
        
            
           
    
