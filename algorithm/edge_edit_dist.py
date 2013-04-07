from algorithm.abstract_graph_edit_dist import AbstractGraphEditDistance
import sys


class EdgeEditDistance(AbstractGraphEditDistance):
	"""
	Calculates the graph edit distance between two edges.
	A node in this context is interpreted as a graph,
	and edges are interpreted as nodes.
	"""

	def insert_cost(self, i, j):
		if i == j:
			return deprel_insdel_weight(self.g2.nodes[j])
		return sys.maxint


	def delete_cost(self, i, j):
		if i == j:
			return deprel_insdel_weight(self.g1.nodes[i])
		return sys.maxint

   	def substitute_cost(self, edge1, edge2):
   		if edge1 == edge2:
   			return 0.
   		return deprel_sub_weight(edge1, edge2) 


def deprel_sub_weight(edge1, edge2):
    #TODO: fetch weights from file 
    return 1.

def deprel_insdel_weight(edge):
    #TODO: fetch weights from file 
    return 1.
