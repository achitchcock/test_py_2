from Tkinter import *
from random import randint, choice


class point_obj(object):
    def __init__(self, loc):
        self.id = id
        self.dx = choice((1,2,3)) + randint(1,100)/100.0
        self.dy = choice((1,2,3)) + randint(1,100)/100.0
        self.loc = loc


class graphical_app(Frame):
    def __init__(self, master):
        self.master = master
        self.canvas_size = 800
        self.canvas = Canvas(master=self.master, width=self.canvas_size, height=self.canvas_size, bg='white')
        self.canvas.grid(row=0, column=0)
        self.points = []
        self.lines = []
        self.colors = ['red','orange','yellow','green','blue','indigo','violet']
        self.count = 0
        for i in range(2):
            size = 20 #choice([20,30,40,50])
            self.points.append(point_obj([randint(0,self.canvas_size),randint(0,self.canvas_size)]))
        self.update()

    def update(self):
        #self.canvas.delete("all")
        for i in range(0,len(self.points)-1,2):
            self.lines.append(self.canvas.create_line(self.points[i].loc + self.points[i+1].loc,
                                                      fill="#{:06x}".format(self.count)))
        for point in self.points:
            point.loc[0] += point.dx
            point.loc[1] += point.dy
            if point.loc[0] < 0 or point.loc[0] > self.canvas_size:
                point.dx *= -1
            if point.loc[1] < 0 or point.loc[1] > self.canvas_size:
                point.dy *= -1
        self.count += 50
        #print "#{:06x}".format(self.count)
        if len(self.lines) > 200 * len(self.points)//2:
            for i in range(len(self.points)//2):
                self.canvas.delete(self.lines.pop(0))
        self.master.after(10, self.update)

root = Tk()
myApp = graphical_app(root)
root.mainloop()