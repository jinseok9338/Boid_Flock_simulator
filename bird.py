from random import randrange as rd
from random import randint
from math import sqrt


class Bird():
    def __init__(self,canvas,pos_x,pos_y):
        self.canvas = canvas
        self.pos_x = pos_x
        self.radius = 5
        self.pos_y = pos_y
        self.bird = canvas.create_oval(self.pos_x,self.pos_y,self.pos_x+self.radius,self.pos_y+self.radius)
        self.velocityX = randint(1, 10) / 10.0
        self.velocityY = randint(1, 10) / 10.0
        self.MAX_VELOCITY = 10

    def distance(self, prey):
        '''Return the distance from another prey'''

        distX = self.pos_x - prey.pos_x
        distY = self.pos_y - prey.pos_y

        return sqrt(distX * distX + distY * distY)

    def move_closer(self, prey_list):
        '''Move closer to a set of prey_list'''

        if len(prey_list) < 1:
            return

        # calculate the average distances from the other prey_list
        avgX = 0
        avgY = 0
        for prey in prey_list:
            if prey.pos_x == self.pos_x and prey.pos_y == self.pos_y:
                continue

            avgX += (self.pos_x - prey.pos_x)
            avgY += (self.pos_y - prey.pos_y)

        avgX /= len(prey_list)
        avgY /= len(prey_list)

        # set our velocity towards the others
        distance = sqrt((avgX * avgX) + (avgY * avgY)) * -1.0

        self.velocityX -= (avgX / 100)
        self.velocityY -= (avgY / 100)


    def move_with(self, prey_list):
        '''Move with a set of prey_list'''

        if len(prey_list) < 1:
            return
        # calculate the average velocities of the other prey_list
        avgX = 0
        avgY = 0

        for prey in prey_list:
            avgX += prey.velocityX
            avgY += prey.velocityY

        avgX /= len(prey_list)
        avgY /= len(prey_list)

        # set our velocity towards the others
        self.velocityX += (avgX / 40)
        self.velocityY += (avgY / 40)

    def move_away(self, prey_list, minDistance):
        '''Move away from a set of prey_list. This avoids crowding'''

        if len(prey_list) < 1:
            return

        distanceX = 0
        distanceY = 0
        numClose = 0

        for prey in prey_list:
            distance = self.distance(prey)

            if  distance < minDistance:
                numClose += 1
                xdiff = (self.pos_x - prey.pos_x)
                ydiff = (self.pos_y - prey.pos_y)

                if xdiff >= 0:
                    xdiff = sqrt(minDistance) - xdiff
                elif xdiff < 0:
                    xdiff = -sqrt(minDistance) - xdiff

                if ydiff >= 0:
                    ydiff = sqrt(minDistance) - ydiff
                elif ydiff < 0:
                    ydiff = -sqrt(minDistance) - ydiff

                distanceX += xdiff
                distanceY += ydiff

        if numClose == 0:
            return

        self.velocityX -= distanceX / 5
        self.velocityY -= distanceY / 5




    def update(self):
        '''Perform actual movement based on our velocity'''

        if abs(self.velocityX) > self.MAX_VELOCITY or abs(self.velocityY) > self.MAX_VELOCITY:
            scaleFactor = self.MAX_VELOCITY / max(abs(self.velocityX), abs(self.velocityY))
            self.velocityX *= scaleFactor
            self.velocityY *= scaleFactor

        self.pos_x += self.velocityX
        self.pos_y += self.velocityY
        coords = [self.pos_x,self.pos_y,self.pos_x+self.radius,self.pos_y+self.radius]
        self.canvas.coords(self.bird, coords[0], coords[1], coords[2], coords[3])







