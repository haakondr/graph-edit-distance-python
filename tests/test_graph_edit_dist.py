#import unittest
#import algorithm.graph_edit_dist as g
#import utils.xml_parser as p 
#import classes.models
#import networkx as nx
#import decimal
#
#
#class GraphEditTest(unittest.TestCase):
#
#    def setUp(self):
#        self.graph1 = p.parse('data/AIDS/data/41.gxl')[0]
#        self.graph2 = p.parse('data/AIDS/data/4901.gxl')[0]
#        self.graph3 = p.parse('data/AIDS/data/5461.gxl')[0]
#        self.graph4 = p.parse('data/AIDS/data/426.gxl')[0]
#        self.attr1 = classes.models.Attribute('x', '149.0', 'float')
#        self.attr2 = classes.models.Attribute('y', '139.5', 'float')
#        self.attr3 = classes.models.Attribute('x', '129.0', 'float')
#        self.attr4 = classes.models.Attribute('y', '100.5', 'float')
#        self.node1 = classes.models.Node('_1', [self.attr1, self.attr2])
#        self.node2 = classes.models.Node('_2', [self.attr3, self.attr4])

#    def test_cost_matrix(self):
#        ged = g.GraphEditDistance(self.graph1, self.graph2,
#        relabel_fn=g.relabel_diff)
#        cost_matrix = ged.matrix
#        n = max(self.graph1.number_of_nodes(), self.graph2.number_of_nodes())
#
#        self.assertEqual(len(cost_matrix), n * 2)
#        self.assertEqual(len(cost_matrix[0]), n * 2)
#        for i in range(len(cost_matrix)):
#            for j in range(len(cost_matrix[0])):
#                self.assertNotEqual(cost_matrix[i][j], None)

#    def test_distance(self):
#        self.assertEqual(
#        g.compare(self.graph1, self.graph1, relabel_fn=g.relabel_diff), 0)
#        self.assertEqual(
#        g.compare(self.graph1, self.graph2, relabel_fn=g.relabel_diff), 12)
#
#    def test_relabel_cost(self):
#        ged = g.GraphEditDistance(self.graph1, self.graph2,
#        relabel_fn=g.relabel_diff)
#         
#        self.assertEqual(ged.relabel_cost(self.node1, self.node1), 0)
#        self.assertEqual(ged.relabel_cost(self.node1, self.node2), 0) 
#        self.assertEqual(ged.relabel_cost(self.node1, self.node3), 2)
#        self.assertEqual(ged.relabel_cost(self.node4, self.node3), 3)
#          
#    def test_neighbour_cost(self):
#       pass
#    def test_diff(self):
#        self.assertEqual(g.diff([1, 2, 3], [1, 2, 3]), 0)
#        self.assertEqual(g.diff([1, 4, 7], [5, 7, 4, 1]), 1)
#        self.assertEqual(g.diff([], []), 0)
#
#        a = classes.models.Attribute('symbol', 5, 'int')
#        b = classes.models.Attribute('x', 'text', 'String')
#        c = classes.models.Attribute('symbol', 5, 'int')
#
#        self.assertEqual(g.diff([a, b], [a]), 1)
#        self.assertEqual(g.diff([a, b], [a, b]), 0)
#        self.assertEqual(g.diff([a], [c]), 0)
#
#    def test_dist(self):
#        a1 = classes.models.Attribute('x', 0., 'float')
#        a2 = classes.models.Attribute('x', 1.2, 'float')
#        a3 = classes.models.Attribute('x', 1.1, 'float')
#        a4 = classes.models.Attribute('x', 5.0, 'float')
#        a5 = classes.models.Attribute('y', 1.0, 'float')
#        a6 = classes.models.Attribute('y', 1.3, 'float')
#        a7 = classes.models.Attribute('y', 5.4, 'float')
#        a8 = classes.models.Attribute('y', 3.3, 'float')
#        node1 = classes.models.Node('1', [a1,a5])
#        node2 = classes.models.Node('2', [a2,a6])
#        node3 = classes.models.Node('3', [a3,a7])
#
#        self.assertAlmostEqual(g.relabel_distance(node1, node2), 1.2369317)
#        self.assertAlmostEqual(g.relabel_distance(node2, node3), 4.1012193)

#    def test_edge_vector(self):
#        graph = nx.Graph()
#        graph.add_node(self.node1)
#        graph.add_node(self.node2)
#        graph.add_edge(self.node1, self.node2)
#    
#        edges = graph.edges()
#        
#        self.assertEqual(g.edge_vector(edges[0]), [-20.0, -39.])
