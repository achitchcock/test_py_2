from Tkinter import *
from random import randint



class Thing(object):
    def __init__(self, id, static=False):
        self.id = id
        self.dx = 0
        self.dy = 0
        self.static = static



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
        t = self.canvas.create_oval(10,10,50,50,fill='green', outline='black')

        self.things[t] = Thing(t)
        self.things[t].dx = 0.3
        t = self.canvas.create_rectangle(0,700,200,750,fill='blue')
        self.things[t]= (Thing(t,True))





    def update(self):
        for thing in self.things.values():
            if not thing.static:
                self.canvas.move(thing.id, thing.dx,thing.dy)
                thing.dy += (9.8 * (self.delay * self.ms))
        for thing in self.things.values():
            overlap = self.canvas.find_overlapping(*self.canvas.coords(thing.id))
            if len(overlap) > 1:
                for item in overlap:
                    self.collide(thing,self.things[item])
        self.tk.after(self.delay, self.update)

    def collide(self,thing1, thing2):
        #print "collide!",thing1,thing1
        if thing2.static:
            thing1.dy *= -0.8
            self.canvas.move(thing1.id, thing1.dx, thing1.dy)


    @property
    def ms(self):
        return 0.001

    @staticmethod
    def get_color():
        return "#{:06X}".format(randint(0, 256**3))


root = Tk()
myApp = GraphicalApp(root)
myApp.mainloop()
