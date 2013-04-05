##!/usr/bin/env python
#
#import unittest
#import xml.etree.ElementTree as ET
#import utils.xml_parser as xml_parser 
#import utils.misc
#
#class ParserTest(unittest.TestCase):
#    
#   def setUp(self):
#       root = ET.parse('data/Fingerprint/data/f0001_01.gxl').getroot()
#       self.graph = root[0]
#
#    def test_parse(self):
#        pass
#
#commented out due to its long processing time    
#    def test_retrieve_graphs(self):
#        """
#        Makes sure none of the test, train and validation 
#        sets are equal, which would give too good results
#        """
#        d1 = xml_parser.retrieve_graphs('data/Letter/LOW/')
##        d2 = xml_parser.retrieve_graphs('data/AIDS/data/')
##        d3 = xml_parser.retrieve_graphs('data/Letter/MED/')
#
#        test = d1['test']
#        train = d1['train']
#        val = d1['val']
#        
#        for te in test:
#            for tr in train:
#                for v in val:
#                    self.assertNotEqual(te, tr) 
#                    self.assertNotEqual(tr, v)
#                    self.assertNotEqual(v ,te)
#                    self.assertNotEqual(tr, v)

#    def test_find_nodes(self):
#        nodes = xml_parser.find_nodes(self.graph)
#        self.assertEqual(len(nodes), 7)
#    
#        for node in nodes:
#            self.assertNotEqual(node.attributes, None)
#            self.assertNotEqual(node.id_, None)
#
#    def test_find_edges(self):                       
#        edges = xml_parser.find_edges(self.graph)
#        self.assertEqual(len(edges), 10) 
#        for edge in edges:
#            self.assertNotEqual(edge.attributes, None)
#            self.assertNotEqual(edge.start , None)
#            self.assertNotEqual(edge.end, None)
#
#    def test_find_node_attributes(self):
#        for node in self.graph.findall('node'):
#            attributes = xml_parser.find_attributes(node)
#            for a in attributes:
#                self.assertNotEqual(a, None)
#     
#    def test_find_edge_attributes(self):
#        for edge in self.graph.findall('edge'):
#            attributes = xml_parser.find_attributes(edge)
#            for a in attributes:
#                self.assertNotEqual(a, None)
#
#    def test_chunks(self):
#        l = range(750)
#        chunks = utils.misc.chunks(l, 8)
#        i = 0
#        for chunk in chunks:
#            for n in chunk:
#                self.assertEqual(i, n)
#                i += 1
#
