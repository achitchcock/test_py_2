from Tkinter import *
from random import randint


class PointObject(object):
    def __init__(self, loc):
        self.id = id
        self.dx = 0
        self.dy = 0
        self.loc = loc

    def __add__(self, other):
        return self.loc + other.loc


class GraphicalApp(object, Frame):
    def __init__(self, master):
        super(GraphicalApp, self).__init__()
        self.tk = master
        self.canvas_size = 800
        self.canvas = Canvas(master=self.tk, width=self.canvas_size, height=self.canvas_size, bg='white')
        self.canvas.grid(row=0, column=0)
        self.points = []
        self.lines = []
        self.color = self.get_color()
        self.count = 0
        self.gap = 10
        self.p1 = PointObject([0, 400])
        self.p2 = PointObject([400, 400])
        self.sector = 0
        self.update()

    def update(self):
        if self.sector != 4:
            self.canvas.create_line(self.p1+self.p2, fill=self.color)
            self.count += 1
        if self.sector == 0:
            self.p1.loc[0] += self.gap
            self.p2.loc[1] -= self.gap
            if self.p2.loc[1] < 0:
                self.sector = 1
        elif self.sector == 1:
            self.p1.loc[0] += self.gap
            self.p2.loc[1] += self.gap
            if self.p1.loc[0] > 800+self.gap:
                self.sector = 2
        elif self.sector == 2:
            self.p1.loc[0] -= self.gap
            self.p2.loc[1] += self.gap
            if self.p2.loc[1] > 800+self.gap:
                self.sector = 3
        elif self.sector == 3:
            self.p1.loc[0] -= self.gap
            self.p2.loc[1] -= self.gap
            if self.p1.loc[0] < -self.gap:
                self.p1 = PointObject([0, 400])
                self.p2 = PointObject([400, 400])
                self.color = self.get_color()
                self.sector = 4
        elif self.sector == 4:
            if len(self.canvas.find_all()) > 0:
                self.canvas.delete(self.canvas.find_all()[0])
            else:
                self.sector = 0
        self.tk.after(10, self.update)

    @staticmethod
    def get_color():
        return "#{:06X}".format(randint(0, 256**3))


root = Tk()
myApp = GraphicalApp(root)
myApp.mainloop()
