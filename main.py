from Operations import vecSub, vecAdd, vecMul
from vector import Vec
from grid import buildGrid, buildCameraRays
from sphere import Sphere
from raymarcher import marchRays





"""
COORDINATE SYSTEM AS FOLLOWS


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

s1 = Sphere(400, 240, -1000, 800, [255, 0, 0])
s2 = Sphere(600, 840, -400, 300, [255, 0, 255])


objectsInScene = [s1]

GRID_WIDTH = 1920
GRID_HEIGHT = 1080
GRID_SIZE = 1

startScreen = Vec(0, 0, 0, "topLeft")
direction1 = Vec(GRID_SIZE, 0, 0, "left_right")
direction2 = Vec(0, GRID_SIZE, 0, "up_down")

camera = Vec(GRID_WIDTH // 2, GRID_HEIGHT // 2, 1000, "Cam") #should be in the middle of screen but 1000 units away



#build a grid of points
grid = buildGrid(startScreen, direction1, direction2, GRID_WIDTH, GRID_HEIGHT)


"""now for every point of the grid calculate
a vector from the camera to the said point and normalize
those vectors"""

normalizedCameraDirections = buildCameraRays(grid, camera)

marchRays = marchRays(normalizedCameraDirections, camera, objectsInScene, 0.01, 20, GRID_WIDTH, GRID_HEIGHT)




        
  
        
        
        
        
            
           
    
