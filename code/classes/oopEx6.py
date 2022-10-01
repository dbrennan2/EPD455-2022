import math

class point:
    """
    point: A class used to define a point in 2D.
    
    Instantiated as e = point(xPos,yPos).
    xPos: the x-position of the circle center
    yPos: the y-position of the circle center

    The __call__ operator returns distance to origin.
    """
    def __init__(self, xPos = 0, yPos = 0):
        self.x = xPos
        self.y = yPos

    def __call__(self):
        return math.sqrt(self.x*self.x + self.y*self.y)


pt = point(2,3)
print("How far the point is from origin: %5.3f" % pt())
print(pt.__doc__)
