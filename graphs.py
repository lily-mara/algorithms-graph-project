#!/usr/bin/env python3
# coding: utf-8

import re
import sys
import os.path

LINE = re.compile(r'\s*(\w+)\s*-\s*(\w+)\s*=\s*(\d+)')


def main(args):
    if len(args) < 1:
        print('Must provide filename as argument. Exiting.')
        sys.exit(1)

    filename = args[0]
    if not os.path.exists(filename):
        print('File  {} does not exist. Exiting.'.format(filename))
        sys.exit(1)

    g = Graph(filename)
    print('Loaded graph with {} nodes'.format(len(g.nodes)))
    interact(g)


def interact(graph):
    while True:
        print('[1] Compute shortest paths from nodes')
        print('[2] Compute minimum spanning tree')
        choice = input('Enter a selection: ')
        if choice == '1':
            interact_dijstras(graph)
        else:
            interact_prims(graph)


def interact_prims(graph):
    graph.print_prims()


def interact_dijstras(graph):
    print('Chose a starting node')
    print(', '.join(graph.nodes))
    node = None
    while node not in graph.nodes:
        node = input('Pick a node: ')
    graph.print_dijkstra(node)


def parse_line(line):
    m = LINE.match(line)
    if m:
        node1 = m.group(1)
        node2 = m.group(2)
        weight = int(m.group(3))

        return node1, node2, weight
    return None


def parse_lines(lines):
    relations = []
    for i, line in enumerate(lines):
        p = parse_line(line)
        if p is None:
            raise ValueError('Invalid syntax on line {}: "{}"'.format(i + 1, line))
        relations.append(p)
    return relations


def node_names(relations):
    nodes = set()
    idx = 0
    for i in relations:
        nodes.add(i[0])
        nodes.add(i[1])
    return nodes


def node_index_table(nodes):
    tab = {}
    idx = 0

    for i in nodes:
        if i not in tab.keys():
            tab[i] = idx
            idx += 1

    return tab


class Graph(object):
    def __init__(self, filename):
        with open(filename, 'r') as f:
            l = f.readlines()

        self.relations = parse_lines(l)
        self.nodes = node_names(self.relations)
        self.index = node_index_table(self.nodes)
        self._matrix()

    def _matrix(self):
        self.mat = [[-1 for _ in self.nodes] for _ in self.nodes]
        for a, b, w in self.relations:
            self._set_weight(a, b, w)
            self._set_weight(b, a, w)
            self._set_weight(a, a, 0)
            self._set_weight

    def get_weight(self, x, y):
        x_idx = self.index[x]
        y_idx = self.index[y]

        return self.mat[x_idx][y_idx]

    def _set_weight(self, x, y, w):
        x_idx = self.index[x]
        y_idx = self.index[y]

        self.mat[x_idx][y_idx] = w

    def dijkstra(self, n):
        v = {n}
        path = {n: (0,n)}

        while v != self.nodes:
            node, weight, pre = self.nearest_neighbor(v)
            v.add(node)
            weight += path[pre][0]
            path[node] = (weight, pre)
        return path

    def prims(self):
        y = self.nodes.copy()
        x = {y.pop()}
        t = []

        while x != self.nodes:
            u, v, w = self.cheapest_cut_edge(x, y)
            x.add(v)
            y.remove(v)
            t.append((u, v, w))

        return t

    def print_prims(self):
        p = self.prims()

        for pre, node, weight in p:
            print('{}->{} {}'.format(pre, node, weight))

    def cheapest_cut_edge(self, X, Y):
        v, w, u = self.nearest_neighbor(X)
        return u, v, w

    def print_dijkstra(self, n):
        d = self.dijkstra(n)

        for node, (weight, pre) in d.items():
            print('{}->{} {}'.format(pre, node, weight))

    def nearest_neighbor(self,v):
        return min(self.neighbors(v), key = lambda x:x[1])

    def neighbors(self, v):
        neighbors = []
        for v_node in v:
            for self_node in self.nodes:
                weight = self.get_weight(v_node, self_node)
                if weight != 0 and weight != -1 and self_node not in v:
                    neighbors.append((self_node, weight, v_node))
        return neighbors

if __name__ == '__main__':
    main(sys.argv[1:])
