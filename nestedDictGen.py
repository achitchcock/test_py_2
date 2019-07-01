from collections import defaultdict

class NestedDict(dict):
    def __init__(self, depth):
        self.depth = depth
    def __getitem__(self, key):
        if key in self: return self.get(key)
        if self.depth > 1:
             return self.setdefault(key, NestedDict(self.depth-1))
        else:
            return self.setdefault(key, [])


d = NestedDict(5)

d[1][2][3][4][5].append(6)
d[1][2][3][4][6].append(7)
print d


