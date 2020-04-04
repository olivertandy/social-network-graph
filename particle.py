from math import sqrt

class Vector2D :
    def __init__(self, x = 0, y = 0) :
        self.position = (x, y)
        self.x = x
        self.y = y
        
    def __str__(self) :
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def add(self, other) :
        return Vector2D(self.x + other.x, self.y + other.y)

    def sub(self, other) :
        return Vector2D(self.x - other.x, self.y - other.y)

    def multiply(self, factor) :
        return Vector2D(factor * self.x, factor * self.y)

    def divide(self, factor) :
        return Vector2D(self.x / factor, self.y / factor)

    def getTuple(self) :
        return (self.x, self.y)

def testDistance() :
    print(pythagoras(3, 4))
    print(pythagoras(1, 1))
    A = Vector2D(1, 1)
    B = Vector2D(4, 5)
    print(distanceBetween(A, B))

class Particle :
    def __init__(self, position=(0., 0.), velocity=(0., 0.), force=(0., 0.), mass = 1.) :
        self.mass = mass
        self.force = Vector2D(*force)
        self.velocity = Vector2D(*velocity)
        self.position = Vector2D(*position)

    def __str__(self) :
        def position() :
            return "Position = " + str(self.position)
        def mass() :
            return "Mass = " + str(self.mass)
        def force() :
            return "Force = " + str(self.force)
        
        return position() + "\n" + mass() + "\n" + force()

    def updatePosition(self) :
        f = self.force
        acceleration = f.divide(self.mass)
        self.velocity = self.velocity.add(acceleration)
        self.position = self.position.add(self.velocity)

    def updateForce(self, force = Vector2D(0, 0)) :
        self.force = force

def pythagoras(A = 0, B = 0) :
    return sqrt(pow(A, 2) + pow(B, 2))
    
def distanceBetween(A = Vector2D(0, 0), B = Vector2D(0, 0)) :
    xDifference = B.x - A.x
    yDifference = B.y - A.y
    return pythagoras(xDifference, yDifference)

def distanceBetweenParticles(A = Particle(), B = Particle()) :
    return distanceBetween(A.position, B.position)
