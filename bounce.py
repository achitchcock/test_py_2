from Tkinter import *
from random import randint
from collections import namedtuple

xypair = namedtuple("normal", ["x", "y"])


class Thing(object):
    def __init__(self, id, canvas, static=False):
        self.id = id
        self.canvas = canvas
        self.dx = 0
        self.dy = 0
        self.xv = 0
        self.yv = 0
        self.static = static

    def collide(self, other):
        # print "collide!",thing1,thing1
        if other.static:
            total = self.dx + self.dy
            print total, self.dx, self.dy, self.norm(other).x * 0.8, self.norm(other).y * 0.8
            self.dy *= (self.norm(other).y * 0.7)
            self.dx *= (self.norm(other).x * 0.7)
            self.canvas.move(self.id, self.dx, self.dy)

    @property
    def center(self):
        x1, y1, x2, y2 = self.canvas.coords(self.id)
        return xypair((x1 + x2) / 2, (y1 + y2) / 2)

    @property
    def top(self):
        return self.canvas.coords(self.id)[1]

    @property
    def bottom(self):
        return self.canvas.coords(self.id)[3]

    @property
    def left(self):
        return self.canvas.coords(self.id)[0]

    @property
    def right(self):
        return self.canvas.coords(self.id)[2]

    def norm(self, other):
        x = 0
        y = 0
        if other.left < self.center.x < other.right:
            return xypair(1,-1)
        elif other.bottom > self.center.y > other.top:
            return xypair(-1,1)
        else:
            h_comp = other.center.x - self.center.x
            v_comp = other.center.y - self.center.y
            total = abs(h_comp) + abs(v_comp)
            print "H: {}  V:{}  Hc:{} Vc:{} T:{}".format(h_comp/total, v_comp/total, h_comp, v_comp, total)
            return xypair(-h_comp/total, -v_comp/total)


        '''
        if other.center.y > self.center.y and other.center.x > self.center.x:
            return xypair(-1,1)
        elif other.center.y > self.center.y and other.center.x < self.center.x:
            return xypair(1,1)
        elif other.center.y < self.center.y and other.center.x > self.center.x:
            return xypair(-1,-1)
        elif other.center.y < self.center.y and other.center.x < self.center.x:
            return xypair(1,-1)
        else:
            print self.center, other.center
            return xypair(1,1)
        '''


class GraphicalApp(object, Frame):
    def __init__(self, master):
        super(GraphicalApp, self).__init__()
        self.tk = master
        self.delay = 10
        self.canvas_size = 800
        self.canvas = Canvas(master=self.tk, width=self.canvas_size, height=self.canvas_size, bg='white')
        self.canvas.grid(row=0, column=0)
        self.things = {}
        self.init_objects()
        self.update()

    def init_objects(self):
        t = self.canvas.create_oval(15, 50, 55, 90, fill='green', outline='black')
        self.things[t] = Thing(t, self.canvas)
        self.things[t].dx = 12
        self.things[t].dy = -5

        t = self.canvas.create_oval(415, 50, 455, 90, fill='orange', outline='black')
        self.things[t] = Thing(t, self.canvas)
        self.things[t].dx = -10
        self.things[t].dy = -8

        t = self.canvas.create_rectangle(500, 200, 520, 750, fill='blue')
        self.things[t] = (Thing(t, self.canvas, True))
        t = self.canvas.create_rectangle(10, 700, 520, 750, fill='blue')
        self.things[t] = (Thing(t, self.canvas, True))
        t = self.canvas.create_rectangle(10, 70, 20, 750, fill='blue')
        self.things[t] = (Thing(t, self.canvas, True))
        t = self.canvas.create_rectangle(150, 540, 350, 640, fill='blue')
        self.things[t] = (Thing(t, self.canvas, True))

    def update(self):
        for thing in self.things.values():
            if not thing.static:
                self.canvas.move(thing.id, thing.dx, thing.dy)
                thing.dy += ((9.8 ** 2) * (self.delay * self.ms))/2
        for thing in self.things.values():
            if not thing.static:
                overlap = self.canvas.find_overlapping(*self.canvas.coords(thing.id))
                if len(overlap) > 1:
                    for item in overlap[1:]:
                        thing.collide(self.things[item])
        self.canvas.update()
        self.tk.after(self.delay, self.update)

    @property
    def ms(self):
        return 0.001

    @staticmethod
    def get_color():
        return "#{:06X}".format(randint(0, 256 ** 3))


root = Tk()
myApp = GraphicalApp(root)
myApp.mainloop()
