# -*- coding: UTF-8 -*-


class Edge():

    def __init__(self, start, end, deprel):
        self.start = start
        self.end = end
        self.deprel = deprel

    def __repr__(self):
        return self.deprel

    def __hash__(self):
        return hash(self.deprel)

    def __eq__(self, other):
        return self.deprel == other.deprel


def create_from(json_node, graph):
    start = graph.node(json_node['id'])
    end = graph.node(json_node['rel'])
    return Edge(start, end, json_node['deprel'])
