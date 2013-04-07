# -*- coding: UTF-8 -*-

from algorithm.munkres import Munkres
import sys

class GraphEditDistance():

    def __init__(self, graph1, graph2, relabel_cost, del_cost, ins_cost):
        self._relabel_cost = relabel_cost
        self._del_cost = del_cost
        self._ins_cost = ins_cost
        self.g1 = graph1
        self.g2 = graph2
        #TODO: pos edit weights
        #TODO: deprel edit weights
        self.matrix = self.create_cost_matrix()

    def normalized_distance(self):
        avg_graphlen = (self.g1.size() + self.g2.size()) / 2.
        return self.distance() / avg_graphlen

    def distance(self):
        m = Munkres()
        indexes = m.compute(self.matrix)
        edit_costs = [self.matrix[i][j] for i, j in indexes]

        return sum(edit_costs)

    def cost_matrix(self, nodes1, nodes2):
        n = len(nodes1)
        m = len(nodes2)
        #TODO: initialiser til 0 for alle?
        cost_matrix = [n+m][n+m]

        for i in range(n):
            for j in range(m):
                cost_matrix[i][j] = self.substitute_cost(nodes1[i], nodes2[j])

        for i in range(m):
            for j in range(m):
                cost_matrix[i+n][j] = self.insert_cost(i, j)


        for i in range(n):
            for j in range(n):
                cost_matrix[j][i+m] = self.delete_cost(i, j)

        return cost_matrix

    # def edge_diff(self, edge1, edge2):
    #     diff = list_diff(edge1[2]['attr'], edge2[2]['attr'])
    #     if len(diff) == 0:
    #         return 0.
    #     return len(edge1[2]['attr']) / float(len(diff))


    def insert_cost(self, i, j):
        if i == j:
            return self._ins_cost * pos_insdel_weight(self.g2.node[j])
        return sys.maxint

    def delete_cost(self, i, j):
        if i == j:
            return self._del_cost * pos_insdel_weight(self.g1.node[i])
        return sys.maxint

    def substitute_cost(self, node1, node2):
        diff = self.relabel_cost(node1, node2) + edge_diff(node1, node2) / 2.
        return diff * self._SUBSTITUTE_COST

    def relabel_cost(self, node1, node2):
        return node1.diff(node2) * pos_sub_weight(node1, node2)

    def print_matrix(self):
        print "cost matrix:" 
        for column in self.matrix:
            for row in column:
                if row == sys.maxint:
                    print "inf\t",
                else:
                    print "%.2f\t" % float(row),
            print ""

def edge_diff(node1, node2):
    #TODO: implement
    pass


def deprel_sub_weight(edge):
    #TODO: implement
    return 1.

def deprel_insdel_weight(edge):
    #TODO: implement
    return 1.

def pos_sub_weight(node1, node2):
    #TODO: implement
    return 1.

def pos_insdel_weight(node):
    #TODO: implement
    return 1.
