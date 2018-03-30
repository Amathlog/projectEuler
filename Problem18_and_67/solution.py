class Node(object):
    def __init__(self, value):
        self.value = value
        self.parent1 = None
        self.parent2 = None
        self.child1 = None
        self.child2 = None
        self.max = None

    def set_child(self, child):
        if self.child1 is None:
            self.child1 = child
        else:
            self.child2 = child

    def set_parent(self, parent):
        if self.parent1 is None:
            self.parent1 = parent
        else:
            self.parent2 = parent
        parent.set_child(self)

    def __repr__(self):
        return str(self.value)

files = ['number', 'p067_triangle.txt']

for file in files:
    with open(file) as f:
        data = f.readlines()

    triangle = []
    for i, line in enumerate(data):
        triangle.append([])
        for j, number in enumerate(line.split(' ')):
            triangle[i].append(Node(int(number)))
            if i == 0:
                continue
            if j != i:
                triangle[i][j].set_parent(triangle[i-1][j])
            if j != 0:
                triangle[i][j].set_parent(triangle[i-1][j-1])

    for line in triangle:
        for node in line:
            if node.parent1 is None and node.parent2 is None:
                node.max = node.value
            elif node.parent1 is None:
                node.max = node.value + node.parent2.max
            elif node.parent2 is None:
                node.max = node.value + node.parent1.max
            else:
                node.max = node.value + max(node.parent1.max, node.parent2.max)

    print("Answer for file " + file + " : ", 
        max(triangle[-1], key=lambda n: n.max).max)



