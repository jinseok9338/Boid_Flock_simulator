import tkinter as tk
from bird import Bird
import random

NUM_BOIDS = 100
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 1200
BORDER = 0

root = tk.Tk()
root.title("Boid Simulator")
root.geometry("1000x1000")
canvas = tk.Canvas(root, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, borderwidth=0, highlightthickness=0, bg="white")
canvas.pack()


bird_list = []
for i in range(NUM_BOIDS):
    bird = Bird(canvas,random.randint(0, 1000), random.randint(0, 1000))
    # Add the prey to the list of objects
    bird_list.append(bird)
    canvas.update()

    for prey in bird_list:
        closeBoids = []
        for otherBoid in bird_list:
            if otherBoid == prey:
                continue
            distance = prey.distance(otherBoid)
            if distance < 100:
                closeBoids.append(otherBoid)


        prey.move_closer(closeBoids)
        prey.move_with(closeBoids)
        prey.move_away(closeBoids, 40)

        # ensure they stay within the screen space
        # if we roubound we can lose some of our velocity

        if prey.pos_x < BORDER and prey.velocityX < 0:
            prey.velocityX = -prey.velocityX * random.random()
        if prey.pos_x > SCREEN_WIDTH - BORDER and prey.velocityX > 0:
            prey.velocityX = -prey.velocityX * random.random()
        if prey.pos_y < BORDER and prey.velocityY < 0:
            prey.velocityY = -prey.velocityY * random.random()
        if prey.pos_y > SCREEN_HEIGHT - BORDER and prey.velocityY > 0:
            prey.velocityY = -prey.velocityY * random.random()
        prey.update()






tk.mainloop()




