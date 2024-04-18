from Operations import vecSub, vecAdd, vecMul, skalar
from vector import Vec
from grid import buildGrid, buildCameraRays
from sphere import Sphere
from raymarcher import marchRays
import math

v1 = Vec(-50, 0, -104)
v2 = Vec(-7.824462945706642, -33.993774625208786, -84.4077157617773)

print(skalar(v1, v2))
