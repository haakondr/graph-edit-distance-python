
import unittest
import algorithm.graph_edit_distance as ged
import networkx as nx


class GraphEditDistanceTest(unittest.TestCase):

    def test_two_deletes(self):
        g1 = bob_kissed_mary()
        g2 = mary_was_kissed_by_bob()

        self.assertEqual(ged.distance(g2, g1), 2.)
        self.assertEqual(ged.normalized_distance(g2, g1), 2./4.)

    def test_two_inserts(self):
        g1 = bob_kissed_mary()
        g2 = mary_was_kissed_by_bob()

        self.assertEqual(ged.distance(g1, g2), 2.)
        self.assertEqual(ged.normalized_distance(g1, g2), 2./4.)

    def test_one_substitute(self):
        g1 = bob_kissed_mary()
        g2 = bob_killed_mary()

        self.assertEqual(ged.distance(g1, g2), 1.)
        self.assertEqual(ged.normalized_distance(g1, g2), 1./3.)


def bob_kissed_mary():
    g1 = nx.Graph()
    g1.add_nodes_from(["Bob", "kissed", "Mary"])
    g1.add_edge("Bob", "kissed")
    g1.add_edge("Mary", "kissed")

    return g1

def mary_was_kissed_by_bob():
    g2 = nx.Graph()
    g2.add_nodes_from(["Mary", "was", "kissed", "by", "Bob"])
    g2.add_edge("Mary", "kissed")
    g2.add_edge("was", "kissed")
    g2.add_edge("by", "kissed")
    g2.add_edge("Bob", "by")

    return g2

def bob_killed_mary():
    g = nx.Graph()
    g.add_nodes_from(["Bob", "killed", "Mary"])
    g.add_edge("Bob", "killed")
    g.add_edge("Mary", "killed")

    return g

g1 = bob_kissed_mary()
g2 = mary_was_kissed_by_bob()
print g1.nodes()
print g2.nodes()
d = ged.normalized_distance(g1, g2)
