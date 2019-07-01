
class NxNspiral:
    def __init__(self, size):
        self.size = size
        self.data = [[None for x in range(size)] for y in range(size)]

    def display(self):
        fmt_str = "{: >" + str(len(str(self.size ** 2))) + "}"
        for line in self.data:
            print ("[" + (fmt_str + ", ") * (self.size-1) + fmt_str + "]").format(*line)

    def fill_spiral(self):
        count = 1
        x = -1
        y = 0
        dx = 1
        dy = 1
        hr = self.size
        vr = self.size - 1
        while count <= self.size**2:
            for hi in range(hr):
                x += dx
                self.data[y][x] = count
                count += 1
            hr -= 1
            dx *= -1
            for vi in range(vr):
                y += dy
                self.data[y][x] = count
                count += 1
            vr -= 1
            dy *= -1


for i in [5, 10, 20]:  # range(1,10):
    mySpiral = NxNspiral(i)
    mySpiral.fill_spiral()
    mySpiral.display()
    print
