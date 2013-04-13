# -*- coding: UTF-8 -*-

from algorithm.abstract_graph_edit_dist import AbstractGraphEditDistance
from algorithm.edge_edit_dist import EdgeEditDistance
from graph.edge_graph import EdgeGraph
import sys


def compare(g1, g2, pos_weights, deprel_weights, print_details=False):
    ged = GraphEditDistance(g1, g2, pos_weights, deprel_weights)

    if print_details:
        ged.print_matrix()

    return ged.normalized_distance()


class GraphEditDistance(AbstractGraphEditDistance):

    def __init__(self, g1, g2, pos_weights, deprel_weights):
        AbstractGraphEditDistance.__init__(self, g1, g2)
        self.pos_weights = pos_weights
        self.deprel_weights = deprel_weights

    def substitute_cost(self, node1, node2):
        return self.relabel_cost(node1, node2) + self.edge_diff(node1, node2)

    def relabel_cost(self, node1, node2):
        if node1 == node2:
            return 0.
        else:
            try:
                return self.pos_weights[node1.pos+"-"+node2.pos]
            except KeyError:
                return 1.

    def delete_cost(self, i, j, nodes1):
        if i == j:
            try:
                return self.pos_weights[nodes1[i].pos]
            except KeyError:
                return 1.
        return sys.maxint

    def insert_cost(self, i, j, nodes2):
        if i == j:
            try:
                return self.pos_weights[nodes2[j].pos]
            except KeyError:
                return 1.
        else:
            return sys.maxint

    def pos_insdel_weight(self, node):
        return self.pos_weights(node.pos)

    def edge_diff(self, node1, node2):
        edges1 = self.g1.edges[node1.id_]
        edges2 = self.g2.edges[node2.id_]
        if len(edges1) == 0 or len(edges2) == 0:
            return max(len(edges1), len(edges2))

        edit_edit_dist = EdgeEditDistance(EdgeGraph(edges1), EdgeGraph(edges2), self.deprel_weights)
        return edit_edit_dist.normalized_distance()
