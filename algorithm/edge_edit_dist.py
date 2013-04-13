from algorithm.abstract_graph_edit_dist import AbstractGraphEditDistance
import sys


class EdgeEditDistance(AbstractGraphEditDistance):
    """
    Calculates the graph edit distance between two edges.
    A node in this context is interpreted as a graph,
    and edges are interpreted as nodes.
    """

    def __init__(self, g1, g2, deprel_weights):
        AbstractGraphEditDistance.__init__(self, g1, g2)
        self.deprel_weights = deprel_weights

    def insert_cost(self, i, j, nodes2):
        if i == j:
            return self.deprel_insdel_weight(nodes2[j])
        return sys.maxint

    def delete_cost(self, i, j, nodes1):
        if i == j:
            return self.deprel_insdel_weight(nodes1[i])
        return sys.maxint

    def substitute_cost(self, edge1, edge2):
        if edge1 == edge2:
            return 0.
        return self.deprel_sub_weight(edge1, edge2)

    def deprel_sub_weight(self, edge1, edge2):
        return self.deprel_weights[edge1.deprel+"-"+edge2.deprel]

    def deprel_insdel_weight(self, edge):
        return self.deprel_weights[edge.deprel]
