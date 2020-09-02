from random import randrange as rd
from math import sqrt


class Bird():
    def __init__(self,canvas,pos_x,pos_y):
        self.canvas = canvas
        self.pos_x = pos_x
        self.radius = 20
        self.pos_y = pos_y
        self.bird = canvas.create_oval(self.pos_x,self.pos_y,self.pos_x+self.radius,self.pos_y+self.radius)
        self.canvas.pack()

    def move_randomly(self):
        coordinate_of_the_bird =(self.canvas.coords(self.bird)[0]+self.canvas.coords(self.bird)[2],self.canvas.coords(self.bird)[1]+self.canvas.coords(self.bird)[3])
        random_point_list = []  # inizialize a void lists for red point coordinates
        random_point_list_x = []
        random_point_list_y = []
        point_counter = 0  # initizlize counter for the while loop
        min_dist = 40  # set the minimum euclidean distance beyond you want to create the points
        max_dist = 45  # set the maximum euclidean distance redpoint can have from blu point
        max_coodeinate_dist = int(sqrt((max_dist ** 2) / 2))  # from the euclidean distance formula you can get the max coordinate


        while True:  # create a potentailly infinite loop! pay attention!
            if point_counter < 20:  # set the number of point you want to add (in this case 20)
                x_RedPtshift = rd(-max_coodeinate_dist, max_coodeinate_dist, 1)  # x shift of a red point
                y_RedPtshift = rd(-max_coodeinate_dist, max_coodeinate_dist, 1)  # y shift of a red point
                if sqrt(x_RedPtshift ** 2 + y_RedPtshift ** 2) > min_dist:  # if the point create go beyond the minimum distance
                    ptRedx = coordinate_of_the_bird[0] + x_RedPtshift  # x coordinate of a red point
                    ptRedy = coordinate_of_the_bird[1] + y_RedPtshift  # y coordinate of a red point
                    ptRed = [ptRedx, ptRedy]  # list with the x,y,z coordinates
                    print(ptRed)
                    if ptRed not in random_point_list:  # avoid to create red point with the same coordinates
                        random_point_list.append(ptRed)  # add to a list with this notation [x1,y1],[x2,y2]
                        random_point_list_x.append(ptRedx)  # add to a list with this notation [x1,x2,x3...] for plotting
                        random_point_list_y.append(ptRedy)  # add to a list with this notation [y1,y2,y3...] for plotting
                        point_counter += 1  # add one to the counter of how many points you have in your list
            else:  # when point_counter reach the number of points you want the while cicle ends
                break
            return random_point_list

