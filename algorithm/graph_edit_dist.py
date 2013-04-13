# -*- coding: UTF-8 -*-

from algorithm.abstract_graph_edit_dist import AbstractGraphEditDistance
from algorithm.edge_edit_dist import EdgeEditDistance
import sys


def compare(g1, g2, pos_weights, deprel_weights, print_details=False):
    ged = GraphEditDistance(g1, g2, pos_weights, deprel_weights)

    if print_details:
        ged.print_matrix()

    return ged.normalized_distance()


class GraphEditDistance(AbstractGraphEditDistance):

    def __init__(self, g1, g2, pos_weights, deprel_weights):
        AbstractGraphEditDistance.__init__(g1, g2)
        self.pos_weights = pos_weights
        self.deprel_weights = deprel_weights

    def substitute_cost(self, node1, node2):
        return self.relabel_cost(node1, node2) + self.edge_diff(node1, node2)

    def delete_cost(self, i, j):
        if i == j:
            try:
                return self.pos_weights[self.g1.node[i]['pos']]
            except KeyError:
                return 1.
        return sys.maxint

    def insert_cost(self, i, j):
        if i == j:
            try:
                return self.pos_weights[self.g2.node[j]['pos']]
            except KeyError:
                return 1.
        else:
            return sys.maxint

    def pos_sub_weight(self, node1, node2):
        try:
            return self.pos_weights[node1.pos+"-"+node2.pos]
        except KeyError:
            return 1.

    def pos_insdel_weight(self, node):
        return self.pos_weights(node.pos)

    def edge_diff(self, node1, node2):
        edit_edit_dist = EdgeEditDistance(node1.edges, node2.edges, self.deprel_weights)
        return edit_edit_dist.normalized_distance()
