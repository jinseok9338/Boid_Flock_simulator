import tkinter as tk
from bird import Bird


root = tk.Tk()
root.title("Boid Simulator")
root.geometry("1000x1000")
canvas = tk.Canvas(root, width=1000, height=1000, borderwidth=0, highlightthickness=0, bg="white")
bird = Bird(canvas,30,30)
print(bird.move_randomly())
canvas.grid()

#root.mainloop()

