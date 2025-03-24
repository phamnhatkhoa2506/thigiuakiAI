# 102190017_VoTuanManhHung bài 3

import heapq


class Node:
    def __init__(self, label, goal_cost):
        self.label = label
        self.cost = 10000
        self.goal_cost = goal_cost
        self.save_cost = None
        self.pr = []
        self.chld = []

    def __repr__(self):
        return str(dict({
            "label": self.label,
            "cost": self.cost,
            "goal cost": self.goal_cost
        }))

    def __eq__(self, other):
        return self.label == other.label

    def __lt__(self, other):
        if self.save_cost == 10000:
            return self.goal_cost + self.cost < other.goal_cost + other.cost
        else:
            return self.cost < other.cost

    def get_label(self):
        return self.label

    def neighbors(self):
        return self.chld + self.pr


class Tree:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_nodes(self, data):
        for node in data:
            self.nodes.append(node)

    def add_node(self, node):
        self.nodes.append(node)

    def get_index(self, node):
        for i, n in enumerate(self.nodes):
            if n.get_label() == node.get_label():
                return i
        return -1

    def add_edges(self, tuple_edges):
        for t in tuple_edges:
            start_label = t[0]
            end_label = t[1]
            w = t[2]
            index_start_label = self.get_index(Node(start_label, None))
            index_end_label = self.get_index(Node(end_label, None))
            self.nodes[index_start_label].chld.append(
                self.nodes[index_end_label])
            self.nodes[index_end_label].pr.append(
                self.nodes[index_start_label])
            self.edges.append(
                (self.nodes[index_start_label], self.nodes[index_end_label], t[2]))

    def show_nodes(self):
        return [node.get_data() for node in self.nodes]

    def get_edge(self, start_node, end_node):
        try:
            return [edges for edges in self.edges if edges[0] == start_node and edges[1] == end_node][0]
        except:
            return None


def update_cost(tree, current_node, prev_node):
    if tree.get_edge(prev_node, current_node) is not None:
        # print("OK")
        if current_node.cost > prev_node.cost + tree.get_edge(prev_node, current_node)[2]:
            current_node.cost = prev_node.cost + \
                tree.get_edge(prev_node, current_node)[2]


def A_Star(tree, start, end):
    frontier = [start]
    heapq.heapify(frontier)
    explored = []
    while len(frontier) > 0:
        state = heapq.heappop(frontier)
        explored.append(state)
        print(state)
        if state == end:
            return explored
        for child in state.neighbors():
            update_cost(tree, child, state)
            if child.get_label() not in list(set(node.get_label() for node in frontier + explored)):
                heapq.heappush(frontier, child)
    return False


if __name__ == "__main__":
    tree = Tree()
    tree.add_nodes([
        Node("S", 10),
        Node("A", 9),
        Node("B", 8),
        Node("C", 7),
        Node("D", 6),
        Node("E", 5),
        Node("F", 4),
        Node("G", 10),
        Node("H", 10),
        Node("K", 3),
        Node("M", 0),
        Node("N", 10),
        Node("I", 6),
        Node("J", 0),
        Node("L", 9),
        Node("Z", 8)
    ])
    tree.add_edges([
        ("S", "A", 5),
        ("S", "B", 6),
        ("S", "C", 5),
        ("A", "D", 6),
        ("A", "E", 7),
        ("B", "F", 3),
        ("B", "G", 4),
        ("C", "H", 6),
        ("C", "K", 4),
        ("D", "M", 5),
        ("D", "N", 8),
        ("E", "I", 8),
        ("F", "J", 4),
        ("F", "L", 4),
        ("K", "Z", 4)
    ])
    tree.nodes[0].cost = 0
    print("Dinh thu 1-------\n")
    result = A_Star(tree, tree.nodes[0], tree.nodes[10])
    if result:
        s = 'explored: '
        for i in result:
            s += i.label + " "
            print(s)
    else:
        print('404 Not Found!')
    print("Dinh thu 2-------\n")
    result = A_Star(tree, tree.nodes[0], tree.nodes[13])
    if result:
        s = 'explored: '
        for i in result:
            s += i.label + " "
            print(s)
    else:
        print('404 Not Found!')
