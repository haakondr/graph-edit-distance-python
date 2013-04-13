# -*- coding: UTF-8 -*-

from algorithm.munkres import Munkres
import sys


class AbstractGraphEditDistance(object):
    def __init__(self, g1, g2):
        self.g1 = g1
        self.g2 = g2

    def normalized_distance(self):
        """
        Returns the graph edit distance between graph g1 & g2
        The distance is normalized on the size of the two graphs.
        This is done to avoid favorisation towards smaller graphs
        """
        avg_graphlen = (self.g1.size() + self.g2.size()) / 2.
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
        n = self.g1.size()
        m = self.g2.size()
        cost_matrix = [[0 for i in range(n + m)] for j in range(n + m)]

        nodes1 = self.g1.node_list()
        nodes2 = self.g2.node_list()

        for i in range(n):
            for j in range(m):
                cost_matrix[i][j] = self.substitute_cost(nodes1[i], nodes2[j])

        for i in range(m):
            for j in range(m):
                cost_matrix[i+n][j] = self.insert_cost(i, j, nodes2)

        for i in range(n):
            for j in range(n):
                cost_matrix[j][i+m] = self.delete_cost(i, j, nodes1)

        self.cost_matrix = cost_matrix
        return cost_matrix

    def insert_cost(self, i, j):
        raise NotImplementedError

    def delete_cost(self, i, j):
        raise NotImplementedError

    def substitute_cost(self, nodes1, nodes2):
        raise NotImplementedError

    def print_matrix(self):
        print "cost matrix:"
        for column in self.create_cost_matrix():
            for row in column:
                if row == sys.maxint:
                    print "inf\t",
                else:
                    print "%.2f\t" % float(row),
            print ""
