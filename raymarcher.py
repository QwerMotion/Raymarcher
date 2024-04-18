from Operations import vecSub, vecAdd, vecMul, skalar
from vector import Vec
from grid import buildGrid, buildCameraRays
from sphere import Sphere
from imageSaver import save_array_as_ppm, generateEmptyImage, write_pixel

def marchRays(cameraDirections, camera, objectsInScene, hitDistance, maxSteps, width, height):

    

    counter = 0
    hitcounter = 0
    lowestDist = 1000000
    imageArray = generateEmptyImage(0, 0, 0, width, height)

    lightSource = Vec(500, 539, -700)

    for i in range(len(cameraDirections)):
        
    
        minDistance, minDistanceObject = getMinDistance(camera, objectsInScene)
        
            
        marchPoint = vecAdd(camera, vecMul(cameraDirections[i], minDistance))


        for j in range(maxSteps):
            
            minDistance, minDistanceObject = getMinDistance(marchPoint, objectsInScene)
            if minDistance < lowestDist or lowestDist == None:
                lowestDist = minDistance
            if minDistance <= hitDistance:
                #hit did happen, marchPoint is the position where it happend and minDistanceObject is who got hit

                #get vector from sphere to lightsorge and determine how that differs from sphere normal at that marchPoint
                sphereVec = Vec(minDistanceObject.x, minDistanceObject.y, minDistanceObject.z)
                
                sphereToLight = vecSub(lightSource, sphereVec)
                normal = vecSub(marchPoint, sphereVec)
                
                result = (skalar(sphereToLight, normal) + 1) / 2

               
               

                hitcolor = minDistanceObject.getColor().copy()
                

                #print("skalarwerte", result)
                #print("hitcolor[0]", hitcolor[0])
                #print("product of that: ", result * hitcolor[0])
                #print("roundet of that: ", round(result * hitcolor[0]))
                #print("--------------")

                
                hitcolor[0] = round(abs(result) * hitcolor[0])
                hitcolor[1] = round(abs(result) * hitcolor[1])  
                hitcolor[2] = round(abs(result) * hitcolor[2])

                
                
                #print("result of rounding is: ", hitcolor[1])
                
                hitcounter += 1
                
                hitXid = cameraDirections[i].xID
                hitYid = cameraDirections[i].yID
                write_pixel(imageArray, hitXid, hitYid, hitcolor)
                
                break
            marchPoint = vecAdd(marchPoint, vecMul(cameraDirections[i], minDistance))
            

           
                
        counter += 1
        if (counter % 100000 == 0):
            print("[RAYMARCHER]", counter, "/", len(cameraDirections))

    print("hits / rays: ", hitcounter, "/", len(cameraDirections))
    print("lowestDistance: ", lowestDist)
    save_array_as_ppm(imageArray, "raytest.ppm")

def getMinDistance(point, objectsInScene):
    
    startPoint = point
    distances = []
    for i in range(len(objectsInScene)):
        
        distanceX = startPoint.x - objectsInScene[i].x
        distanceY = startPoint.y - objectsInScene[i].y
        distanceZ = startPoint.z - objectsInScene[i].z

        sumDist = (distanceX**2 + distanceY**2 + distanceZ**2)**0.5 - objectsInScene[i].r
        distances.append(sumDist)

    minDistance = min(distances)
    minDistanceObject = None
    for j in range(len(distances)):
        if (distances[j] == minDistance):
            minDistanceObject = objectsInScene[j]
            
    return minDistance, minDistanceObject

    
