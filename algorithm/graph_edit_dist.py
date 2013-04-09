# -*- coding: UTF-8 -*-

from algorithm.abstract_graph_edit_dist import AbstractGraphEditDistance
from algorithm.edge_edit_dist import EdgeEditDistance
import sys


class GraphEditDistance(AbstractGraphEditDistance):

    def __init__(self, g1, g2, pos_weights):
        AbstractGraphEditDistance.__init__(g1, g2)
        self.pos_weights = pos_weights

    def substitute_cost(self, node1, node2):
        return self.relabel_cost(node1, node2) + edge_diff(node1, node2)

    def delete_cost(self, i, j):
        if i == j:
            return self.pos_insdel_weight(self.g1.node[i])
        return sys.maxint

    def insert_cost(self, i, j):
        if i == j:
            return self.pos_insdel_weight(self.g2.node[j])
        else:
            return sys.maxint

    def pos_sub_weight(self, node1, node2):
        return self.pos_weights[node1.pos+"-"+node2.pos]

    def pos_insdel_weight(self, node):
        return self.pos_weights(node.pos)


def edge_diff(node1, node2):
    edit_edit_dist = EdgeEditDistance(node1.edges, node2.edges)
    return edit_edit_dist.normalized_distance()
