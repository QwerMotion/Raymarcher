class Vec:
    def __init__(self,x=None, y=None, z=None, name=None):
        self.x = x
        self.y = y
        self.z = z
        self.name = name
        self.xID = None
        self.yID = None


    def setPos(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def getPos(self):
        return self.x, self.y, self.z

    def pretty(self):
        print("----------------------")
        print("Vectorname: ", self.name)
        print("Vectorlength: ", self.getLength())
        print("|x:  ", self.x, "|")
        print("|y:  ", self.y, "|")
        print("|z:  ", self.z, "|")
        print("|xID:", self.xID, "|")
        print("|zID:", self.yID, "|")
        print("----------------------")

    def getLength(self):
       
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def norm(self):
        length = self.getLength()
        if (length == 0):
            print("WARNING! DEVISION BY ZERO ENCOUNTERED IN: norm() FOR VECTOR NAMED:", self.name)
            return -1
        self.x *= 1 / length
        self.y *= 1 / length
        self.z *= 1 / length

    def multiply(self, t):
        self.x *= t
        self.y *= t
        self.z *= t
        return self

    def add(self, v):
        self.x += v.x
        self.y += v.y
        self.z += v.z
        return self

    

