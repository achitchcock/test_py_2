from Tkinter import *
from random import randint, choice


class ball_obj(object):
    def __init__(self, id):
        self.id = id
        self.dx = choice((0,1,2,3)) + randint(10,100)/100.0
        self.dy = choice((0,1,2,3)) + randint(10,100)/100.0
        self.bbox = [10,10,50,50]


class graphical_app(Frame):
    def __init__(self, master):
        self.master = master
        self.canvas_size = 800
        self.canvas = Canvas(master=self.master, width=self.canvas_size, height=self.canvas_size, bg='white')
        self.canvas.grid(row=0, column=0)
        self.balls = []
        self.colors = ['red','orange','yellow','green','blue','indigo','violet']
        for i in range(100):
            size = 20 #choice([20,30,40,50])
            self.balls.append(ball_obj(self.canvas.create_oval([1,1,size,size], fill=choice(self.colors))))
        self.update()

    def update(self):
        for ball in self.balls:
            self.canvas.move(ball.id, ball.dx, ball.dy)
            ball.bbox = self.canvas.bbox(ball.id)
            if ball.bbox[0] < 0 or ball.bbox[2] > self.canvas_size:
                ball.dx *= -1
            if ball.bbox[1] < 0 or ball.bbox[3] > self.canvas_size:
                ball.dy *= -1

        self.master.after(10, self.update)

root = Tk()
myApp = graphical_app(root)
root.mainloop()