# -*- coding: UTF-8 -*-

from algorithm.abstract_graph_edit_dist import AbstractGraphEditDistance
from algorithm.edge_edit_dist import EdgeEditDistance
import sys


class GraphEditDistance(AbstractGraphEditDistance):

    def substitute_cost(self, node1, node2):
        return self.relabel_cost(node1, node2) + edge_diff(node1, node2)

    def delete_cost(self, i, j):
        if i == j:
            return pos_insdel_weight(self.g1.node[i])
        return sys.maxint

    def insert_cost(self, i, j):
        if i == j:
            return pos_insdel_weight(self.g2.node[j])
        else:
            return sys.maxint


def edge_diff(node1, node2):
    eed = EdgeEditDistance(node1.edges, node2.edges)
    return eed.normalized_distance()


def pos_sub_weight(node1, node2):
    #TODO: fetch weights from file
    return 1.


def pos_insdel_weight(node):
    #TODO: fetch weights from file
    return 1.
