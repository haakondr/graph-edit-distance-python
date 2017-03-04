# -*- coding: UTF-8 -*-

from algorithm.munkres import Munkres
import sys


def normalized_distance(g1, g2):
    ged = GraphEditDistance(g1, g2)
    ged.print_matrix()
    return ged.normalized_distance()

def distance(g1, g2):
    ged = GraphEditDistance(g1, g2)
    return ged.distance()

class GraphEditDistance(object):
    def __init__(self, g1, g2):
        self.g1 = g1
        self.g2 = g2

    def normalized_distance(self):
        """
        Returns the graph edit distance between graph g1 & g2
        The distance is normalized on the size of the two graphs.
        This is done to avoid favorisation towards smaller graphs
        """
        avg_graphlen = (len(self.g1) + len(self.g2)) / 2.
        return self.distance() / avg_graphlen

    def distance(self):
        return sum(self.edit_costs())

    def edit_costs(self):
        m = Munkres()
        cost_matrix = self.create_cost_matrix()
        index = m.compute(cost_matrix)
        return [cost_matrix[i][j] for i, j in index]

    def create_cost_matrix(self):
        """
        Creates a |N+M| X |N+M| cost matrix between all nodes in
        graphs g1 and g2
        Each cost represents the cost of substituting,
        deleting or inserting a node
        The cost matrix consists of four regions:

        substitute 	| insert costs
        -------------------------------
        delete 		| delete -> delete

        The delete -> delete region is filled with zeros
        """
        n = len(self.g1)
        m = len(self.g2)
        cost_matrix = [[0 for i in range(n + m)] for j in range(n + m)]

        nodes1 = self.g1.nodes()
        nodes2 = self.g2.nodes()

        for i in range(n):
            for j in range(m):
                cost_matrix[i][j] = self.substitute_cost(nodes1[i], nodes2[j])

        for i in range(m):
            for j in range(m):
                cost_matrix[i+n][j] = self.insert_cost(i, j)

        for i in range(n):
            for j in range(n):
                cost_matrix[j][i+m] = self.delete_cost(i, j)

        self.cost_matrix = cost_matrix
        return cost_matrix

    def insert_cost(self, i, j):
        if i == j:
            return 1.
        return sys.maxint

    def delete_cost(self, i, j):
        if i == j:
            return 1.
        return sys.maxint

    def substitute_cost(self, node1, node2):
        if node1 == node2:
            return 0.
        return 1.

    def print_matrix(self):
        print "cost matrix:"
        for column in self.create_cost_matrix():
            for row in column:
                if row == sys.maxint:
                    print "inf\t",
                else:
                    print "%.2f\t" % float(row),
            print ""
