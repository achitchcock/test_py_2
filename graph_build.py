from typing import Union, List, Optional
from random import randint, choice
import networkx as nx  # type: ignore
import matplotlib.pyplot as plt  # type: ignore


class node(object):
    def __init__(self, id):
        # type: (int) -> None
        self.id = id  # type: int
        self.color = None  # type: Optional[str]
        self.neighbors = []  # type: List[node]


def generate_graph():
    nodes = []  # type: List[node]
    count = 0  # type: int
    for i in range(randint(20, 60)):
        nodes.append(node(count))
        count += 1
    print "Generated {} nodes".format(count + 1)
    while disconnected(nodes):
        # for i in range(randint(count, count*4)):
        n1 = choice(nodes)  # type: node
        n2 = n1
        while n1 == n2:
            n2 = choice(nodes)  # type: node
        if n1 not in n2.neighbors:
            n2.neighbors.append(n1)
            n1.neighbors.append(n2)
    return nodes


def disconnected(nodes):
    for n in nodes:
        if len(n.neighbors) <= 1:
            return True
    return False


def print_graph(graph):
    # type: (List[node]) -> None
    for node in graph:
        print "Node:", node.id, node.color
        print "\tNeighbors:", [n.id for n in node.neighbors]


def color_graph(graph):
    # type: (List[node]) -> bool
    for n in graph:
        if n.color is not None:
            continue
        else:
            colors = ["red", "green", "blue"]  # type: List[str]
            for c in n.neighbors:
                if c.color is None:
                    continue
                else:
                    try:
                        colors.remove(c.color)  # type: ignore
                    except ValueError:
                        pass
            if len(colors) == 0:
                print "Impossible graph"
                return False
            else:
                n.color = choice(colors)
    return True


def validate_color(graph):
    for n in graph:
        for c in n.neighbors:
            if n == c.color:
                print "Invalid Coloring. Node {} and {} are both {}".format(n.id, c.id, n.color)


def draw_graph(graph):
    grph = nx.Graph()
    edges = set()
    colors = []
    for n in graph:
        grph.add_node(n.id)
        colors.append(n.color)
        for c in n.neighbors:
            edges.add(tuple(sorted((n.id, c.id))))
    for a, b in edges:
        grph.add_edge(a, b)
    nx.draw(grph, node_color=colors, with_labels=True)
    plt.show()


def graph_build():
    graph = generate_graph()
    while not color_graph(graph):
        graph = generate_graph()
    validate_color(graph)
    print_graph(graph)
    draw_graph(graph)


graph_build()
