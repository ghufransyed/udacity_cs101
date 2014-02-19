"""
Graph module.
"""


class Graph(object):
    """
    Represents a directed graph.
    """

    def __init__(self):
        """
        Initializes the Graph to an empty graph with no nodes or edges.
        """
        self._nodes = {}

    def add_node(self, node):
        """
        If node is already in the graph, returns False and does not modify the graph.
        Otherwise, adds node to the graph and returns True.
        """
        if node in self._nodes:
            return False
        else:
            self._nodes[node] = set()
            return True

    def has_node(self, node):
        """
        Returns True if node is a node in the graph.
        """
        return node in self._nodes

    def add_edge(self, node1, node2):
        """
        Requires: node1 and node2 are nodes in self.
        Modifies: self
        Adds an edge from node1 to node2 to self.
        """
        assert self.has_node(node1)
        assert self.has_node(node2)
        self._nodes[node1].add(node2)

    def get_nodes(self):
        """
        Returns a frozenset containing the nodes in the graph.
        """
        return frozenset(self._nodes.keys())

    def get_outlinks(self, node):
        """
        Requires: node is a node in self.
        Returns a frozenset of the nodes to which node is connected.
        """
        assert self.has_node(node)
        return frozenset(self._nodes[node])

    def get_inlinks(self, target):
        """
        Requires: node is a node in self.
        Returns a set of the nodes that are connected by and edge to node.
        """
        assert self.has_node(target)
        links_set = set([])
        for node in self._nodes:
            if target in self._nodes[node]:
                links_set.add(node)
        return links_set

    def __str__(self):
        """
        Returns a string representation of the graph.
        """
        return str(self._nodes)
