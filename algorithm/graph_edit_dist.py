# -*- coding: UTF-8 -*-

from algorithm.munkres import Munkres
import sys
from utils.misc import list_diff
from math import sqrt 

def compare(graph1, graph2, print_details=False, relabel_cost=1, del_cost=1, ins_cost=1):

    if use_edge_edit_dist(graph1, graph2):
        if graph1.size() == 0 or graph2.size() == 0:
            """
            hackfix when neither of the graphs contain edges.
            will probably return bad edit distance, 
            TODO: rewrite to something sane
            """
            return 15.
        ged = EdgeEditDistance(graph1, graph2, relabel_cost, del_cost,
        ins_cost)
    else:
        ged = GraphEditDistance(graph1, graph2, relabel_cost, del_cost,ins_cost)
    if print_details:
        ged.print_matrix()
    
    return ged.distance()


def use_edge_edit_dist(graph1, graph2):
    m1 = graph1.graph['mode']
    m2 = graph2.graph['mode']

    return (m1 == 'numeric' and m2 == 'numeric')


class GraphEditDistance():

    def __init__(self, graph1, graph2, relabel_cost, del_cost, ins_cost):
        self.graph1 = graph1
        self.graph2 = graph2
        self._relabel_cost = relabel_cost
        self._del_cost = del_cost
        self._ins_cost = ins_cost
        self.edge_costs = self.get_edge_costs()

    def initialize(self):
        self.matrix = self.create_cost_matrix(self.graph1.nodes(),
        self.graph2.nodes())

    def distance(self):
        self.initialize()

        m = Munkres()
        indexes = m.compute(self.matrix)
        edit_costs = [self.matrix[i][j] for i, j in indexes]

        return sum(edit_costs)

    def get_edge_costs(self):
        edge_costs = {}

        for edge1 in self.graph1.edges(data=True):
            for edge2 in self.graph2.edges(data=True):
                edgename = edge1[0].id_+":"+edge1[1].id_
                edge_costs[edgename] = self.edge_diff(edge1, edge2)

        return edge_costs

    def create_cost_matrix(self, nodes1, nodes2):
        n = max(len(nodes1), len(nodes2))
        cost_matrix = [[0 for i in range(n*2)] for j in
        range(n*2)]
    
        for i in range(n):
            for j in range(n):
                try:
                    cost_matrix[i][j] = self.substitute_cost(nodes1[i], nodes2[j])
                except IndexError:
                    cost_matrix[i][j] = self._ins_cost
                cost_matrix[i + n][j] = self.insert_cost(i, j)
                cost_matrix[i][j + n] = self.delete_cost(i, j)
        
        return cost_matrix
         
    def edge_diff(self, edge1, edge2):
        diff = list_diff(edge1[2]['attr'], edge2[2]['attr'])
        if len(diff) == 0:
            return 0.
        return len(edge1[2]['attr']) / float(len(diff))


    def insert_cost(self, i, j):
        if i == j:
            return self._ins_cost
        return sys.maxint

    def delete_cost(self, i, j):
        if i == j:
            return self._del_cost
        return sys.maxint   

    def substitute_cost(self, node1, node2):
        try:
            edgecost = self.edge_costs[node1.id_+":"+node2.id_]
        except KeyError:
            return self.relabel_cost(node1, node2)
        return self.relabel_cost(node1, node2) + edgecost

    def relabel_cost(self, node1, node2):
        return node1.diff(node2) * self._relabel_cost

    def print_matrix(self):
        print "cost matrix:" 
        for column in self.matrix:
            for row in column:
                if row == sys.maxint:
                    print "inf\t",
                else:
                    print "%.2f\t" % float(row),
            print ""

class EdgeEditDistance(GraphEditDistance):

    def __init__(self, graph1, graph2, relabel_cost=1, del_cost=1, ins_cost=1):
        GraphEditDistance.__init__(self, graph1, graph2, relabel_cost, del_cost,
        ins_cost)
    
    def initialize(self):
        self.matrix = self.create_cost_matrix(self.graph1.edges(),
        self.graph2.edges())

    def substitute_cost(self, edge1, edge2):
        vec1 = edge_vector(edge1)
        vec2 = edge_vector(edge2)
        return float(self._relabel_cost) * dist(vec1, vec2)

def edge_vector(edge):    
    attr1 = edge[0].attributes
    attr2 = edge[1].attributes
    return [a.var - b.var for a, b in zip(attr1, attr2)] 

def dist(vec1, vec2):
    def _pow2(v1, v2):
        return (v1 - v2) * (v1 - v2)
    return sqrt(sum([(_pow2(vec1[i], vec2[i])) for i in range(len(vec1))]))

