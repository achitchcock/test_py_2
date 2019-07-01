from random import randint
from collections import namedtuple, defaultdict

result = namedtuple('result',['sides','max','min','avg'])

def rset(sides):
    x = set()
    count =0
    while len(x) < sides:
        x.add(randint(1,sides))
        count += 1
    return count

def r_op():
    rez_set = {}
    for sides in range(2,21):
        counts = []
        for i in range(100):
            counts.append(rset(sides))
        r = result(sides,max(counts),min(counts),sum(counts)/len(counts))
        rez_set[sides] = [r]
        print "Sides: {} Max: {}  Min: {} Avg: {}".format(*r)
    return rez_set

data = defaultdict(list)
for i in range(3):
    r = r_op()
    for t in r:
        for k in r[t]:
            for i in k:
                print i
    data.update(r)
print(data)
    
