from vector import Vec
import math


def vecMul(v, t):
    """
returns a new vecktor that has been scaled by t (eg. v*t)

"""
    newx = v.x * t
    newy = v.y * t
    newz = v.z * t

    try:
        newName = "(" + v1.name + "*" + t + ")"
    except:
        newName = None
        pass

    vnew = Vec(newx, newy, newz, newName)
    return vnew

def vecSub(v1, v2):
    """
returns a vector that leads from v2 to v1 eg. it does v1 - v2


"""
    newx = v1.x - v2.x
    newy = v1.y - v2.y
    newz = v1.z - v2.z
    
    try:
        newName = "(" + v1.name + ")" + " - " + "(" + v2.name + ")"
    except:
        newName = None
        pass

    vnew = Vec(newx, newy, newz, newName)
    return vnew

def vecAdd(v1, v2):
    """
returns a vector that is v1 + v2


"""
    newx = v1.x + v2.x
    newy = v1.y + v2.y
    newz = v1.z + v2.z
    
    try:
        newName = "(" + v1.name + ")" + " + " + "(" + v2.name + ")"
    except:
        newName = None
        pass

    vnew = Vec(newx, newy, newz, newName)
    return vnew

def vecTimesVec(v1, v2):
    return (v1.x * v2.x) + (v1.y * v2.y) + (v1.z * v2.z)

def skalar(v1, v2):
    return vecTimesVec(v1, v2) * (1 / (v1.getLength() * v2.getLength()))
