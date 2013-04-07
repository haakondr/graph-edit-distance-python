# -*- coding: UTF-8 -*-

from algorithm.munkres import Munkres

class AbstractGraphEditDistance():
	def __init__(self, g1, g2):
		self.g1 = g1
		self.g2 = g2

	def normalized_distance(self):
		avg_graphlen = (self.g1.size() + self.g2.size()) / 2.
		return self.distance() / avg_graphlen

	def distance(self):
        return sum(self.edit_costs())

  	def edit_costs(self):
		m = Munkres()
		index = m.compute(self.cost_matrix())
		return [self.matrix[i][j] for i, j in indexes]


	def cost_matrix(self):
		"""
		Creates a |N+M| X |N+M| cost matrix between all nodes in graphs g1 and g2
		Each cost represents the cost of substituting, deleting or inserting a node
		The cost matrix consists of four regions:
		
		substitute costs | insert costs
		-------------------------------
		delete costs     | delete -> delete 	

		The delete -> delete region is filled with zeros
		"""
        n = len(self.g1.nodes)
        m = len(self.g2.nodes)
        cost_matrix = [[0 for i in range(n+m)] for j in
        range(n+m)]

        """substitute costs for upper left region of cost_matrix"""
        for i in range(n):
            for j in range(m):
                cost_matrix[i][j] = self.substitute_cost(self.g1.nodes[i], self.g2.nodes[j])

        """insert costs for upper right region of cost_matrix"""
        for i in range(m):
            for j in range(m):
                cost_matrix[i+n][j] = self.insert_cost(i, j)

        """calculate delete costs for lower left region of cost_matrix"""
        for i in range(n):
            for j in range(n):
                cost_matrix[j][i+m] = self.delete_cost(i, j)

        return cost_matrix

   	def insert_cost(self, i, j):
   		raise NotImplementedError

   	def delete_cost(self, i, j):
   		raise NotImplementedError

   	def substitute_cost(self, nodes1, nodes2):
   		raise NotImplementedError
