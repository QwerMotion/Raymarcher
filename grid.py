from vector import *
from Operations import *

def buildGrid(startScreen, direction1, direction2, GRID_WIDTH, GRID_HEIGHT):

    

    finished = GRID_WIDTH * GRID_HEIGHT
    print("[GRIDBUILDER]", 0 , "/", finished)

    grid = []
    v1 = vecSub(direction1, startScreen)
    v2 = vecSub(direction2, startScreen)

    




    counter = 0
    for y in range(GRID_HEIGHT):
      
        for x in range(GRID_WIDTH):

            addVector = vecAdd( vecMul(direction1, x) , vecMul(direction2, y) )
            newGridpoint = vecAdd(addVector, startScreen)
            newGridpoint.xID = x
            newGridpoint.yID = y
            grid.append(newGridpoint)
            counter += 1

            if (counter % 100000 == 0):
                print("[GRIDBUILDER]", counter , "/", finished)
                

    print("[GRIDBUILDER]", "done.")
    print("-"*35)
           
    return grid

def buildCameraRays(grid, camera):
    """
for each entry of the grid this function will calculate
a vector from the camera to the gridpoint and then normalize it

"""
    normalizedCameraDirections = []

    for i in range(len(grid)):

        gridXID = grid[i].xID
        gridYID = grid[i].yID
        
        fromCamToGrid = vecSub(grid[i], camera)
        fromCamToGrid.norm()

        fromCamToGrid.xID = gridXID
        fromCamToGrid.yID = gridYID
        
        normalizedCameraDirections.append(fromCamToGrid)

        if (i % 100000 == 0):
            
            print("[CAMERA_RAYBUILDER]", i, "/", len(grid))

    print("[CAMERA_RAYBUILDER]", "done.")
    print("-"*35)

    return normalizedCameraDirections
        

