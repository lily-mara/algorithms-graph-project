Graph Algorithms
================

:author: Nate Mara & Evan Baker
:date: 2016-04-14

Dijkstra's Algorithm
--------------------

Psuedocode:

.. code:: python

    def dijkstra(G, node):
        v = {n}
        predecessor = {}
        distance = {}

        while v != G.nodes:
            node, weight, pre = G.nearest_neighbor(v)
            v.add(node)
            weight += distance[pre]
            predecessor[node] = pre

        return predecessor, weight

The time complexity for our implementation of Dijkstra's algorithms is :math:`O\left( N ^3 \right)` where :math:`N` is the number of nodes in our graph. This is because our while loop iterates through all of the nodes in the graph and the nearest_neighbor function runs in :math:`O\left( N ^2 \right)` because it searches through every possible edge pair. The nearest_neighbor function is inside of the while loop so their time complexities are multiplied giving us :math:`O\left( N ^3 \right)`.

Prims Algorithm
---------------

Psuedocode

.. code:: python

    def prims(G):
        x = {random node from G}
        y = G.nodes - x
        t = []

        while x != G.nodes:
            u, v, weight = G.cheapest_cut_edge(x, y)
            x.add(v)
            y.remove(v)
            t.push((u, v, weight))

        return t

The time complexity for our implementation of Prim's algorithms is :math:`O\left( N ^3 \right)` where :math:`N` is the number of nodes in our graph. This is because our while loop iterates through all of the nodes in the graph and the cheapest_cut_edge function calls the nearest_neighbor function, which runs in :math:`O\left( N ^2 \right)` because it searches through every possible edge pair. The nearest_neighbor function is indirectly inside of the while loop so their time complexities are multiplied giving us :math:`O\left( N ^3 \right)`.

Graph Representation
--------------------

We used an adjacency-matrix to represent a graph in our code.
